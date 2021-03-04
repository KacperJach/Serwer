import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from app import db
from app.models import User
from datetime import datetime

def adding(nr):
    date = datetime.now()
    dt_string = date.strftime("%d/%m/%Y %H:%M:%S")
    u = User(card_id=nr, date=dt_string)
    db.session.add(u)
    db.session.commit()
    return

reader = SimpleMFRC522()
while True:
    try:
        print("Scan")
        nr = None
        while nr is None:
            nr, text = reader.read_no_block()
        nr = str(nr)
        adding(nr)
        print("Success")
    finally:
        GPIO.cleanup()
