from machine import I2C, Pin
from drivers.pca9685 import PCA9685
from drivers.servo import Servos
import configurations
import time


class MotionPlanner:

    def __init__(self):
        self.i2c = I2C(0, scl=Pin(22), sda=Pin(21))
        self.pca = PCA9685(self.i2c)
        self.pca.freq(50)
        self.servos = Servos(self.i2c)
        self.channel_1 = configurations.CHANNEL_1
        self.channel_2 = configurations.CHANNEL_2
        self.channel_3 = configurations.CHANNEL_3
        self.channel_4 = configurations.CHANNEL_4
        self.channel_5 = configurations.CHANNEL_5
        self.default_angle = configurations.DEFAULT_ANGLE
        self.feedback = configurations.soft_feedback
        self.speed = configurations.SPEED

    def set_default_position(self):
        """Set all servos to their default position."""
        self.servos.position(index=self.channel_1, degrees=self.default_angle)
        time.sleep(0.25)
        self.servos.position(index=self.channel_2, degrees=self.default_angle)
        time.sleep(0.25)
        self.servos.position(index=self.channel_3, degrees=self.default_angle)
        time.sleep(0.25)
        self.servos.position(index=self.channel_4, degrees=self.default_angle)
        time.sleep(0.25)
        self.servos.position(index=self.channel_5, degrees=self.default_angle)
        time.sleep(0.25)

    def sweep(self, channel: int) -> bool:
        """Sweep a servo from 0 to 180 degrees and back to default position."""
        for angle in range(self.default_angle, 181, self.speed):
            self.servos.position(index=channel, degrees=angle)
            self.feedback["base"] = angle
            time.sleep(0.02)
        for angle in range(181, self.default_angle, -self.speed):
            self.servos.position(index=channel, degrees=angle)
            self.feedback["base"] = angle
            time.sleep(0.02)
        for angle in range(self.default_angle, 0, -self.speed):
            self.servos.position(index=channel, degrees=angle)
            self.feedback["base"] = angle
            time.sleep(0.02)
        for angle in range(0, self.default_angle, self.speed):
            self.servos.position(index=channel, degrees=angle)
            self.feedback["base"] = angle
            time.sleep(0.02)
        return True

    def move(self, channel: int, up_down_logic: bool, steps: int, arm: str) -> bool:
        """Move the Robotic Arm.

        Args:
            channel (int): select channel
            up_down_logic (bool): up or down logic which is True or False
            steps (int): number of steps to move
            arm (str): motor name

        Returns:
            bool: Boolean value indicating success
        """
        current_position = self.feedback[arm]
        to_positon = current_position  # Initialize to current position

        if up_down_logic is True:
            for step in range(1, steps, 1):
                to_positon = current_position + step
                self.servos.position(index=channel, degrees=to_positon)
                time.sleep(0.02)
                # print(step, to_positon)
            self.feedback[arm] = to_positon
            return True

        if up_down_logic is False:
            for step in range(1, steps, 1):
                to_positon = current_position - step
                self.servos.position(index=channel, degrees=to_positon)
                time.sleep(0.02)
                # print(step, to_positon)
            self.feedback[arm] = to_positon
            return True

    def difference_engine(self, final_position: dict) -> dict:
        """Calculate the difference between current and final positions."""
        base_diff = final_position["base"] - self.feedback["base"]
        shoulder_diff = final_position["shoulder"] - self.feedback["shoulder"]
        elbow_diff = final_position["elbow"] - self.feedback["elbow"]
        wrist_diff = final_position["wrist"] - self.feedback["wrist"]
        end_effector_diff = self.feedback["end_effector"]
        return {
            "base_diff": base_diff,
            "shoulder_diff": shoulder_diff,
            "elbow_diff": elbow_diff,
            "wrist_diff": wrist_diff,
            "end_effector_diff": end_effector_diff,
        }

    def software_feedback_control_system(self, final_position: dict) -> dict:
        """Feedback control system to move the arm to the final position.

        Args:
            final_position (dict): final position dictionary

        Returns:
            dict: software feedback dictionary
        """
        angle_difference = self.difference_engine(final_position=final_position)
        if angle_difference["base_diff"] > 0:
            self.move(self.channel_1, True, angle_difference["base_diff"], "base")
        else:
            self.move(self.channel_1, False, angle_difference["base_diff"] * -1, "base")
        if angle_difference["shoulder_diff"] > 0:
            self.move(
                self.channel_2,
                True,
                angle_difference["shoulder_diff"],
                "shoulder",
            )
        else:
            self.move(
                self.channel_2,
                False,
                angle_difference["shoulder_diff"] * -1,
                "shoulder",
            )
        if angle_difference["elbow_diff"] > 0:
            self.move(
                self.channel_3,
                True,
                angle_difference["elbow_diff"],
                "elbow",
            )
        else:
            self.move(
                self.channel_3,
                False,
                angle_difference["elbow_diff"] * -1,
                "elbow",
            )
        if angle_difference["wrist_diff"] > 0:
            self.move(
                self.channel_4,
                True,
                angle_difference["wrist_diff"],
                "wrist",
            )
        else:
            self.move(
                self.channel_4,
                False,
                angle_difference["wrist_diff"] * -1,
                "wrist",
            )
        if angle_difference["end_effector_diff"] > 0:
            self.move(
                self.channel_5,
                True,
                angle_difference["end_effector_diff"],
                "end_effector",
            )
        else:
            self.move(
                self.channel_5,
                False,
                angle_difference["end_effector_diff"] * -1,
                "end_effector",
            )
        return self.feedback
