from flask import request
from HLEngine3.robsdk import RobSDK


class Handlers:

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
        feedback = RobSDK().robot_position(payload, "http://10.120.3.187/rob/move/")
        return feedback

    def robot_home_position(self, payload):
        feedback = RobSDK().robot_position(payload, "http://10.120.3.187/rob/move/")
        return feedback
