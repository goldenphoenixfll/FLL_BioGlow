"""Mission run 3: move the back attachment and return to base."""


def run3(
    hub,
    robot,
    left_motor,
    right_motor,
    attachment_motor_left,
    attachment_motor_front,
):
    """Run the mission formerly exported from the SPIKE block editor."""

    robot.use_gyro(True)
    robot.straight(700)
    robot.turn(-90)
    robot.straight(400)
    robot.turn(-45)
    attachment_motor_left.run_angle(200, 265)
    robot.settings(straight_acceleration=100)
    robot.straight(-300)
    attachment_motor_left.run_angle(800, -300)
    robot.straight(115)
    robot.turn(-90)
    robot.settings(straight_speed=900)
    robot.straight(800)
