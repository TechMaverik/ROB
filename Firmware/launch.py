import prepositions
from motion_planner import MotionPlanner
from wifi_con import WifiCon

WifiCon().connect()
status = MotionPlanner().set_default_position()
print(status)
status = MotionPlanner().software_feedback_control_system(prepositions.HOME_POS)
print(status)
status = MotionPlanner().software_feedback_control_system(prepositions.TEST_POS_MAX)
print(status)
status = MotionPlanner().software_feedback_control_system(prepositions.TEST_POS_MIN)
print(status)
status = MotionPlanner().software_feedback_control_system(prepositions.HOME_POS)
print(status)
