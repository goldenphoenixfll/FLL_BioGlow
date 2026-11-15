"""Mission run 1: travel to the vines and return through the field."""


def run1(
    hub,
    robot,
    left_motor,
    right_motor,
    attachment_motor_left,
    attachment_motor_front,
):
    """Run the vine mission using the shared robot hardware."""

    robot.use_gyro(True)
    robot.straight(720)
    robot.turn(90)
    robot.straight(290)
    robot.turn(-90)
    robot.straight(50)
    attachment_motor_front.run_angle(500, 200)
    robot.straight(-200)
    robot.turn(45)
    robot.straight(450)
    robot.turn(60)
    robot.straight(850)
    robot.turn(70)
    robot.straight(800)
