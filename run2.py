"""Mission run 2: collect and push the exploding seeds."""

from pybricks.parameters import Stop


def run2(
    hub,
    robot,
    left_motor,
    right_motor,
    attachment_motor_left,
    attachment_motor_front,
):
    """Run the exploding-seeds mission using the shared robot hardware."""

    robot.use_gyro(True)
    robot.straight(50, then=Stop.HOLD)
    robot.turn(45, then=Stop.HOLD)
    robot.straight(440, then=Stop.HOLD)
    attachment_motor_front.control.limits(acceleration=5000)
    attachment_motor_front.run_angle(1050, -300, then=Stop.HOLD)
    robot.settings(straight_speed=1050)
    robot.straight(-450, then=Stop.HOLD)
    robot.turn(60, then=Stop.HOLD)
    robot.settings(straight_speed=200)
    robot.use_gyro(False)
    robot.straight(650, then=Stop.HOLD)
    robot.straight(-800, then=Stop.HOLD)
