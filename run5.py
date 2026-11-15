"""Mission run 5: collect the keystone species."""

from pybricks.parameters import Stop


def run5(
    hub,
    robot,
    left_motor,
    right_motor,
    attachment_motor_left,
    attachment_motor_front,
):
    """Run the keystone-species mission using the shared robot hardware."""

    robot.use_gyro(True)
    robot.settings(straight_speed=150)
    robot.straight(-690, then=Stop.NONE)
    robot.turn(45, then=Stop.NONE)
    robot.straight(-160, then=Stop.NONE)
    attachment_motor_left.run_angle(400, -500, then=Stop.NONE)
    attachment_motor_left.run_angle(400, 400)
    robot.straight(160, then=Stop.NONE)
    robot.turn(-45, then=Stop.NONE)
    robot.straight(690, then=Stop.NONE)
    print("Run 5 completed.")
