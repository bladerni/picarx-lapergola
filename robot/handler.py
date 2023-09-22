# #!/usr/bin/env python3
from picarx import Picarx
from firebase_admin import credentials, initialize_app, db

cred = credentials.Certificate("./serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL' : 'https://erni-hackathon-default-rtdb.europe-west1.firebasedatabase.app'
})

speed = 0
angle = 0

px = Picarx()

def move(speed, angle):
    px.set_dir_servo_angle(angle)
    if speed == 0:
        px.stop()
    if speed > 0:
        px.forward(speed)
    else:
        px.backward(speed)

def acceleration_listener(event):
    speed = event.data
    move(speed, angle)

def car_direction_listener(event):
    angle = event.data
    move(speed, angle)

def car_disco_mode_listener(event):
    print(event.data)

def car_automatic_mode_listener(event):
    print(event.data)

def camera_direction_listener(event):
    print(event.data)

db.reference('/car/acceleration').listen(acceleration_listener)
db.reference('/car/direction').listen(car_direction_listener)
db.reference('/car/disco_mode').listen(car_disco_mode_listener)
db.reference('/car/automatic_mode').listen(car_automatic_mode_listener)
db.reference('/camera/direction').listen(camera_direction_listener)