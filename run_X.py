from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
def run_X(hub, db, amlB, amrF):
    db.use_gyro(True)
    # Usage db.use_gyro(True)
    db.settings(1080, 960, 800, 400)
    # Usage db.settings(speed_mm_per_s, turn_speed_deg_per_s, acceleration_mm_per_s, turn_acceleration_mm_per_s)
    db.straight(500)
    # Usage db.straight(distance_mm)
    db.turn(90, absolute=False)
    # Usage (turn_angle_deg, absolute=False)
    amlB.run_angle(1110, 90)
    # Usage motor.run_angle(speed_in_deg_per_s, run_angle)
if __name__=='__main__':
    hub = PrimeHub()
    lcsC = ColorSensor(Port.C)
    rcsD = ColorSensor(Port.D)
    dmA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    dmE = Motor(Port.E, Direction.CLOCKWISE)
    amlB = Motor(Port.B)
    amrF = Motor(Port.F)
    db = DriveBase(dmA, dmE, wheel_diameter=62.4, axle_track=105)
    run_X(hub, db, amlB, amlB)
"""Github upload instructions
1. Delete all comments like the ones labled # Usage xx.function.(x, xy, xyz) and this one
2. Add comments that tell what the block do like solving a mission or navigating to a mission
3. Upload it to Github"""