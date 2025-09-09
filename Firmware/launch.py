import prepositions
from motion_planner import MotionPlanner

MotionPlanner().set_default_position()
MotionPlanner().software_feedback_control_system(prepositions.TEST_POS)
