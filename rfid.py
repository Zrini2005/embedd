from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time

reader = SimpleMFRC522()


authorized_users = {}



def register_user():
    print("\n[REGISTER MODE]")
    print("Scan new RFID card...")

    id, text = reader.read()

    if id in authorized_users:
        print("Already registered!")
        return

    name = input("Enter name: ")
    authorized_users[id] = name

    print(f"User {name} registered successfully with UID {id}")
    time.sleep(2)


def check_user():
    print("\n[CHECK MODE]")
    print("Scan your RFID card...")

    id, text = reader.read()

    if id in authorized_users:
        print(f"Access Granted: {authorized_users[id]}")
    else:
        print("Access Denied")

    time.sleep(2)


def view_users():
    print("\n[REGISTERED USERS]")
    
    if not authorized_users:
        print("No users registered.")
        return

    for uid, name in authorized_users.items():
        print(f"{uid} → {name}")


def delete_user():
    print("\n[DELETE MODE]")
    print("Scan card to delete...")

    id, text = reader.read()

    if id in authorized_users:
        print(f"Deleting {authorized_users[id]}")
        del authorized_users[id]
    else:
        print("Card not found!")

    time.sleep(2)



try:
    while True:
        print("\n====== RFID SYSTEM MENU ======")
        print("1. Register new card")
        print("2. Check access")
        print("3. View users")
        print("4. Delete user")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            register_user()

        elif choice == '2':
            check_user()

        elif choice == '3':
            view_users()

        elif choice == '4':
            delete_user()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

finally:
    GPIO.cleanup()


# RC522 Pin	Raspberry Pi Pin
# SDA	GPIO 8 (CE0)
# SCK	GPIO 11 (SCLK)
# MOSI	GPIO 10
# MISO	GPIO 9
# IRQ	Not connected
# GND	GND
# RST	GPIO 25
# 3.3V	3.3V


# sudo raspi-config
# Go to:

# Interface Options → SPI → Enable
# Reboot:

# sudo reboot


# sudo apt update
# sudo apt install python3-pip
# pip3 install spidev
# pip3 install mfrc522