from firebase_admin import credentials, initialize_app, db

cred = credentials.Certificate("./serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL' : 'https://erni-hackathon-default-rtdb.europe-west1.firebasedatabase.app'
})

def acceleration_listener(event):
    print(event.data)

def car_direction_listener(event):
    print(event.data)

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