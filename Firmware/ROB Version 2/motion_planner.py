from machine import Pin
from time import sleep_us
import configurations as config
import prepositions


class MotionPlannet:

    def __init__(self) -> None:
        self.dir_pin1 = Pin(config.DIR_PIN_1, Pin.OUT)
        self.step_pin1 = Pin(config.STEP_PIN_1, Pin.OUT)
        self.dir_pin2 = Pin(config.DIR_PIN_2, Pin.OUT)
        self.step_pin2 = Pin(config.STEP_PIN_2, Pin.OUT)
        self.dir_pin3 = Pin(config.DIR_PIN_3, Pin.OUT)
        self.step_pin3 = Pin(config.STEP_PIN_3, Pin.OUT)
        self.pick1 = Pin(config.SERVO_PIN_1, Pin.OUT)
        self.pick2 = Pin(config.SERVO_PIN_2, Pin.OUT)
        self.default_position = prepositions.DEFAULT_POSITION
        self.software_feedback = prepositions.DEFAULT_POSITION
        self.direction_payload = {
            "Base": 1,
            "Left": 1,
            "Right": 1,
            "Pick": 1,
        }

    def move_single_stepper_motor(
        self,
        direction_pin,
        step_pin,
        steps,
        direction,
        step_delay_us,
    ):
        direction_pin.value(direction)
        for _ in range(steps):
            step_pin.value(1)
            sleep_us(step_delay_us)
            step_pin.value(0)
            sleep_us(step_delay_us)

    def direction_sense(self, payload):
        base_current_position = self.software_feedback["Base"]
        left_current_position = self.software_feedback["Left"]
        right_current_position = self.software_feedback["Right"]
        base_target_position = payload["Base"]
        left_target_position = payload["Left"]
        right_target_position = payload["Right"]
        if base_current_position > base_target_position:
            self.direction_payload["Base"] = 1
        elif base_current_position < base_target_position:
            self.direction_payload["Base"] = 0
        if left_current_position > left_target_position:
            self.direction_payload["Left"] = 1
        elif left_current_position < left_target_position:
            self.direction_payload["Left"] = 0
        if right_current_position > right_target_position:
            self.direction_payload["Right"] = 1
        elif right_current_position < right_target_position:
            self.direction_payload["Right"] = 0
        return self.direction_payload

    def move_robot(
        self,
        step_delay_us,
        payload,
    ):
        direction_payload = self.direction_sense(payload=payload)

        base_angle = payload["Base"]
        steps_to_move = int(base_angle / config.ANGLE_PER_STEP)
        self.move_single_stepper_motor(
            self.dir_pin1,
            self.step_pin1,
            steps_to_move,
            direction_payload["Base"],
            step_delay_us,
        )
        left_angle = payload["Left"]
        steps_to_move = int(left_angle / config.ANGLE_PER_STEP)
        self.move_single_stepper_motor(
            self.dir_pin2,
            self.step_pin2,
            steps_to_move,
            direction_payload["Left"],
            step_delay_us,
        )
        right_angle = payload["Right"]
        steps_to_move = int(right_angle / config.ANGLE_PER_STEP)
        self.move_single_stepper_motor(
            self.dir_pin3,
            self.step_pin3,
            steps_to_move,
            direction_payload["Right"],
            step_delay_us,
        )
        self.software_feedback = payload.copy()
        return self.software_feedback
