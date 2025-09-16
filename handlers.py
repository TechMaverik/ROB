from flask import request
from HLEngine3.robsdk import RobSDK


class Handlers:

    def __init__(self):
        self.robot_pos_storage = []
        self.robot_ip_address = ""

    def robot_position(self):
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
        feedback = RobSDK().robot_position(payload, "http://10.120.3.169/rob/move/")
        return feedback

    def robot_position_payload(self, payload):
        feedback = RobSDK().robot_position(payload, "http://10.120.3.169/rob/move/")
        return feedback

    def robot_position_storage(self):
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
        self.robot_pos_storage.append(payload)
        return payload

    def robot_position_clear(self):
        self.robot_pos_storage.clear()
