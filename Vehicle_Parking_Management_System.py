import json
import os
from datetime import datetime

FILE_NAME = "parking_data.json"
TOTAL_SLOTS = 10


# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


# Save data
def save_data(vehicles):
    with open(FILE_NAME, "w") as file:
        json.dump(vehicles, file, indent=4)


# Find available slot
def get_slot(vehicles):
    occupied = []

    for vehicle in vehicles:
        if vehicle["status"] == "Parked":
            occupied.append(vehicle["slot"])

    for i in range(1, TOTAL_SLOTS + 1):
        slot = "B-" + str(i)

        if slot not in occupied:
            return slot

    return None


# Park vehicle
def park_vehicle(vehicles):
    slot = get_slot(vehicles)

    if slot is None:
        print("\nParking is full!")
        return

    number = input("Enter vehicle number: ").upper()
    owner = input("Enter owner name: ")
    vehicle_type = input("Enter vehicle type: ")

    # Check duplicate vehicle
    for vehicle in vehicles:
        if vehicle["number"] == number and vehicle["status"] == "Parked":
            print("\nVehicle is already parked!")
            return

    vehicle = {
        "number": number,
        "owner": owner,
        "type": vehicle_type,
        "slot": slot,
        "entry": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "exit": "",
        "fee": 0,
        "status": "Parked"
    }

    vehicles.append(vehicle)
    save_data(vehicles)

    print("\nVehicle parked successfully!")
    print("Parking Slot:", slot)


# View parked vehicles
def view_vehicles(vehicles):
    found = False

    print("\n========== PARKED VEHICLES ==========")

    for vehicle in vehicles:
        if vehicle["status"] == "Parked":
            found = True

            print("Vehicle Number :", vehicle["number"])
            print("Owner          :", vehicle["owner"])
            print("Vehicle Type   :", vehicle["type"])
            print("Slot           :", vehicle["slot"])
            print("Entry Time     :", vehicle["entry"])
            print("-------------------------------------")

    if not found:
        print("No vehicles parked.")


# Search vehicle
def search_vehicle(vehicles):
    number = input("Enter vehicle number: ").upper()

    for vehicle in vehicles:
        if vehicle["number"] == number:
            print("\n========== VEHICLE DETAILS ==========")
            print("Vehicle Number :", vehicle["number"])
            print("Owner          :", vehicle["owner"])
            print("Vehicle Type   :", vehicle["type"])
            print("Slot           :", vehicle["slot"])
            print("Entry Time     :", vehicle["entry"])
            print("Status         :", vehicle["status"])
            print("Parking Fee    : ₹", vehicle["fee"])
            return

    print("\nVehicle not found!")


# Calculate parking fee
def calculate_fee(entry, exit_time):
    start = datetime.strptime(entry, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(exit_time, "%Y-%m-%d %H:%M:%S")

    seconds = (end - start).total_seconds()

    hours = int(seconds // 3600)

    if seconds % 3600 != 0:
        hours += 1

    if hours <= 1:
        fee = 20
    else:
        fee = 20 + (hours - 1) * 10

    return fee


# Remove vehicle
def remove_vehicle(vehicles):
    number = input("Enter vehicle number: ").upper()

    for vehicle in vehicles:

        if vehicle["number"] == number and vehicle["status"] == "Parked":

            exit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            fee = calculate_fee(
                vehicle["entry"],
                exit_time
            )

            vehicle["exit"] = exit_time
            vehicle["fee"] = fee
            vehicle["status"] = "Removed"

            save_data(vehicles)

            print("\n========== PARKING BILL ==========")
            print("Vehicle Number :", vehicle["number"])
            print("Owner          :", vehicle["owner"])
            print("Slot           :", vehicle["slot"])
            print("Entry Time     :", vehicle["entry"])
            print("Exit Time      :", exit_time)
            print("Parking Fee    : ₹", fee)
            print("==================================")

            return

    print("\nVehicle not found or already removed!")


# Available slots
def available_slots(vehicles):
    occupied = 0

    for vehicle in vehicles:
        if vehicle["status"] == "Parked":
            occupied += 1

    available = TOTAL_SLOTS - occupied

    print("\n========== PARKING STATUS ==========")
    print("Total Slots     :", TOTAL_SLOTS)
    print("Occupied Slots  :", occupied)
    print("Available Slots :", available)


# Parking history
def parking_history(vehicles):
    found = False

    print("\n========== PARKING HISTORY ==========")

    for vehicle in vehicles:
        if vehicle["status"] == "Removed":
            found = True

            print("Vehicle :", vehicle["number"])
            print("Owner   :", vehicle["owner"])
            print("Slot    :", vehicle["slot"])
            print("Entry   :", vehicle["entry"])
            print("Exit    :", vehicle["exit"])
            print("Fee     : ₹", vehicle["fee"])
            print("------------------------------------")

    if not found:
        print("No parking history.")


# Main program
def main():

    vehicles = load_data()

    while True:

        print("\n====================================")
        print("       VEHICLE PARKING SYSTEM")
        print("====================================")
        print("1. Park Vehicle")
        print("2. View Parked Vehicles")
        print("3. Search Vehicle")
        print("4. Remove Vehicle")
        print("5. Available Parking Slots")
        print("6. Parking History")
        print("7. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            park_vehicle(vehicles)

        elif choice == "2":
            view_vehicles(vehicles)

        elif choice == "3":
            search_vehicle(vehicles)

        elif choice == "4":
            remove_vehicle(vehicles)

        elif choice == "5":
            available_slots(vehicles)

        elif choice == "6":
            parking_history(vehicles)

        elif choice == "7":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice!")


# Start program
if __name__ == "__main__":
    main()