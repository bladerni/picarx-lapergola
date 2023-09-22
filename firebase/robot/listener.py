import requests
import time
from firebase_admin import credentials, initialize_app, db

cred = credentials.Certificate("./serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL' : 'https://erni-hackathon-default-rtdb.europe-west1.firebasedatabase.app'
})

def listener(event):
    print(event.data)  # new data at /reference/event.path. None if deleted

ref = db.reference('/accelerate').listen(listener)
