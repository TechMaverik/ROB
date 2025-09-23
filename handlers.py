from flask import request
from HLEngine3.robsdk import RobSDK
from mappers import Mappers


class Handlers:

    def __init__(self):
        self.robot_pos_storage = []
        self.robot_ip_address = ""

    def robot_position(self) -> dict:
        base = request.form.get("slider1")
        shoulder = request.form.get("slider2")
        elbow = request.form.get("slider3")
        wrist_pitch = request.form.get("slider4")
        wrist_roll = request.form.get("slider5")
        gripper = request.form.get("slider6")
        payload = {
            "base": base,
            "shoulder": shoulder,
            "elbow": elbow,
            "wrist": wrist_pitch,
            "end_effector": wrist_roll,
            "pick": gripper,
        }
        ip = self.get_robot_ip()
        feedback = RobSDK().robot_position(payload, "http://" + ip + "/rob/move/")
        return feedback

    def robot_position_payload(self, payload: dict):
        ip = self.get_robot_ip()
        feedback = RobSDK().robot_position(payload, "http://" + ip + "/rob/move/")
        return feedback

    def robot_position_storage(self) -> dict:
        base = request.form.get("slider1")
        shoulder = request.form.get("slider2")
        elbow = request.form.get("slider3")
        wrist_pitch = request.form.get("slider4")
        wrist_roll = request.form.get("slider5")
        gripper = request.form.get("slider6")
        payload = {
            "base": base,
            "shoulder": shoulder,
            "elbow": elbow,
            "wrist": wrist_pitch,
            "end_effector": wrist_roll,
            "pick": gripper,
        }
        Mappers().record_position(
            base, shoulder, elbow, wrist_pitch, wrist_roll, gripper
        )
        self.robot_pos_storage.append(payload)
        return payload

    def robot_position_clear(self):
        self.robot_pos_storage.clear()
        Mappers().delete_record()

    def read_robot_position_records(self) -> list:
        records = Mappers().select_record()
        return records

    def play_recorded(self):
        records = Mappers().select_record()
        for record in records:
            base = record[1]
            shoulder = record[2]
            elbow = record[3]
            wrist_pitch = record[4]
            wrist_roll = record[5]
            gripper = record[6]
            payload = {
                "base": base,
                "shoulder": shoulder,
                "elbow": elbow,
                "wrist": wrist_pitch,
                "end_effector": wrist_roll,
                "pick": gripper,
            }
            ip = self.get_robot_ip()
            RobSDK().robot_position(payload, "http://" + ip + "/rob/move/")

    def add_robot_ip(self):
        ip = request.form.get("ip")
        self.robot_ip_address = ip
        Mappers().add_configurations((ip,))

    def delete_robot_ip(self) -> str:
        Mappers().delete_configuration()
        self.robot_ip_address = ""
        return "Deleted"

    def get_robot_ip(self) -> str:
        records = Mappers().select_configuration()
        for record in records:
            ip = record[1]
        return ip

    def test_robot_connection(self):
        ip = Mappers().select_configuration()
        status = RobSDK().get_status("http://" + ip)
        return status

    def select_configuration(self) -> str:
        records = Mappers().select_configuration()
        for record in records:
            ip = record[1]
        return ip
