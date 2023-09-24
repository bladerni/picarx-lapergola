from picarx import Picarx
from time import sleep
from robot_hat import TTS

px = Picarx()

def init_line_tracker():
    
    max_VEL = 130 # MAX Velocity
    max_ANG = 35 # MAX angle car rotation
    bias_ANG = -7 # Front direction servo bias
    # TO AUTOMATIZE CALIBRATION @!!@!!@!!@
    line =[35,35,35]
    cliff =[153,200,185]
    threshold = [(e1+e2)/2 for e1, e2 in zip(line,cliff)]
    range_sens= [e1-e2 for e1, e2 in zip(threshold,line)]
    calibrationCount = 5
    try:
        # Robot introduction
        tts_robot = TTS()
        speech1 = "Calibrating line tracker"
        speech2 = "Launching in"
        tts_robot.say(speech1)
        tts_robot.say(speech2)
        while calibrationCount >= 0:
            # Robot calibration sensors during 5 seconds
            tts_robot.say(calibrationCount)
            px.get_grayscale_data()
            measure = px.get_grayscale_data()
            line = [measure[1], measure[1], measure[1]]
            cliff = [measure[0], measure[0], measure[0]]
            calibrationCount -= 1
            sleep(1)
        last_step = "center"
        px.forward(max_VEL)
        while True:
            measure = px.get_grayscale_data()
            angulo=min(((((measure[0]-line[0])/range_sens[0])-((measure[2]-line[2])/range_sens[2]))*max_ANG/2),max_ANG) # P control. Ponderation equation to select the next angle based on the two sensors on the sides.
            diff=[e1-e2 for e1, e2 in zip(threshold,measure)]
            px.set_dir_servo_angle(angulo+bias_ANG)
            # Main algorithm, if the robot is turning a curve and its sensors leave the path, 
            # it stores the last state of the wheels and keeps it until it re-engages the line.
            if diff[0] < 0 and diff[1] < 0 and diff[2] > 0:         
                px.set_dir_servo_angle(max_ANG) # Max angle to the right to find asap the path
                last_step = "right"
            elif diff[0] > 0 and diff[1] < 0 and diff[2] < 0:  
                px.set_dir_servo_angle(-max_ANG) # Max angle to the left to find asap the path
                last_step = "left"
            elif diff[0] > 0 and diff[1] > 0 and diff[2] > 0:
                px.set_dir_servo_angle(bias_ANG)
                last_step = "center"
            elif diff[0] < 0 and diff[1] < 0 and diff[2] < 0:
                if last_step == "left":
                    px.set_dir_servo_angle(-max_ANG) # Max angle to the left to find asap the path
                elif last_step == "right":
                    px.set_dir_servo_angle(max_ANG) # Max angle to the left to find asap the path
    finally:
        px.stop()
        sleep(0.1)
        
init_line_tracker()