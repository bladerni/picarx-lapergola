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
        px.backward(speed * -1)

def car_listener(event):
    if (isinstance(event.data, dict)):
        acceleration = event.data.get('acceleration', 0)
        direction = event.data.get('direction', 0)
        move(acceleration, direction)

def car_disco_mode_listener(event):
    print(event.data)

def car_automatic_mode_listener(event):
    print(event.data)

def camera_direction_listener(event):
    print(event.data)

db.reference('/car').listen(car_listener)
#db.reference('/car/disco_mode').listen(car_disco_mode_listener)
#db.reference('/car/automatic_mode').listen(car_automatic_mode_listener)
#db.reference('/camera/direction').listen(camera_direction_listener)