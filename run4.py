"""Mission run 4: lift the vine and return from the mission area."""


async def run4(
    hub,
    robot,
    left_motor,
    right_motor,
    attachment_motor_left,
    attachment_motor_front,
):
    """Run the vine-lifting mission using the shared robot hardware."""
    del hub, left_motor, right_motor, attachment_motor_left

    robot.use_gyro(True)
    robot.straight(450)
    attachment_motor_front.run_angle(500, 200)
    robot.straight(-100)
    attachment_motor_front.run_angle(500, -200)
    robot.straight(-400)
