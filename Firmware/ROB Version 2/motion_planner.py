from machine import Pin
from time import sleep_us
import configurations as config


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

    def move_to_angle_base(
        self,
        target_angle,
        step_delay_us,
        direction,
        motor_selection,
    ):
        if motor_selection == "B":
            steps_to_move = int(target_angle / config.ANGLE_PER_STEP)
            self.move_single_stepper_motor(
                self.dir_pin1,
                self.step_pin1,
                steps_to_move,
                direction,
                step_delay_us,
            )
        if motor_selection == "L":
            steps_to_move = int(target_angle / config.ANGLE_PER_STEP)
            self.move_single_stepper_motor(
                self.dir_pin2,
                self.step_pin2,
                steps_to_move,
                direction,
                step_delay_us,
            )
        if motor_selection == "R":
            steps_to_move = int(target_angle / config.ANGLE_PER_STEP)
            self.move_single_stepper_motor(
                self.dir_pin3,
                self.step_pin3,
                steps_to_move,
                direction,
                step_delay_us,
            )
