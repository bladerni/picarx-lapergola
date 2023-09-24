# #!/usr/bin/env python3
from picarx import Picarx
from firebase_admin import credentials, initialize_app, db
from time import sleep
from robot_hat import TTS
import threading

cred = credentials.Certificate("./serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL' : 'https://erni-hackathon-default-rtdb.europe-west1.firebasedatabase.app'
})

speed = 0
angle = 0
thread_flag = False

px = Picarx()

def move_camera(Y_angle, X_angle):
    px.set_camera_tilt_angle(Y_angle + 10)
    px.set_cam_pan_angle(X_angle - 12)
    
def move(speed, angle):
    px.set_dir_servo_angle(angle)
    if speed == 0:
        px.stop()
    if speed > 0:
        px.forward(speed)
    else:
        px.backward(speed * -1)

def init_line_tracker():
    global thread_flag
    
    while thread_flag:
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
            while thread_flag:
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

def car_listener(event):
    global thread_flag

    if (isinstance(event.data, dict)):
        acceleration = event.data.get('acceleration', 0)
        direction = event.data.get('direction', 0)        
        move(acceleration, direction)

        automatic_mode = event.data.get('automatic_mode', 0)  
        line_tracker_thread = threading.Thread(target=init_line_tracker)

        if automatic_mode:
            line_tracker_thread.start()
            thread_flag = True
        elif line_tracker_thread.is_alive():
            thread_flag = False  # Detener el bucle de move()
            px.stop()
            line_tracker_thread.join()


def car_disco_mode_listener(event):
    print(event.data)

def car_automatic_mode_listener(event):
    print(event.data)

def camera_direction_listener(event):
    if (isinstance(event.data, dict)):
        xAngle = event.data.get('x', 0)
        yAngle = event.data.get('y', 0)
        move_camera(yAngle, xAngle)

db.reference('/car').listen(car_listener)
db.reference('/camera').listen(camera_direction_listener)
#db.reference('/car/automatic_mode').listen(car_automatic_mode_listener)