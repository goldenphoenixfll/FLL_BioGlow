from pybricks.parameters import Button, Color
from pybricks.tools import wait, hub_menu

from robot import (
    attachment_motor_front,
    attachment_motor_left,
    hub,
    left_motor,
    right_motor,
    robot,
)
from runs import RUNS


hub.system.set_stop_button(Button.BLUETOOTH)


def choose_run():
    if not RUNS:
        raise ValueError("Add at least one run to runs.py")

    run_number = hub_menu(*range(1, len(RUNS) + 1))
    return run_number, RUNS[run_number - 1]


def wait_for_imu():
    hub.display.char("G")
    while not hub.imu.ready():
        wait(100)


def run_selected(run_number, run_program):
    wait_for_imu()
    robot.use_gyro(True)
    robot.reset()
    hub.display.number(run_number)

    run_program(
        hub,
        robot,
        left_motor,
        right_motor,
        attachment_motor_left,
        attachment_motor_front,
    )

    robot.stop()
    robot.use_gyro(False)
    hub.light.on(Color.GREEN)
    hub.speaker.beep(880, 250)


while True:
    selected_run_number, selected_run = choose_run()
    run_selected(selected_run_number, selected_run)
