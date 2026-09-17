import time
import random

# Traffic light
RED = "🔴"
YELLOW = "🟡"
GREEN = "🟢"


roads = ["North", "East", "South", "West"]


def generate_traffic():
    """Generate random traffic density for each road."""
    traffic = {}

    for road in roads:
        traffic[road] = random.randint(5, 50)

    return traffic


def display_traffic(traffic):
    """Display traffic density."""

    print("\n========== TRAFFIC STATUS ==========")

    for road, vehicles in traffic.items():

        if vehicles < 15:
            status = "Low"
        elif vehicles < 35:
            status = "Medium"
        else:
            status = "High"

        print(f"{road:8} : {vehicles:2} vehicles - {status}")

    print("====================================")


def calculate_green_time(vehicle_count):
    """Calculate green-light duration based on traffic."""

    if vehicle_count < 15:
        return 10

    elif vehicle_count < 35:
        return 20

    else:
        return 30


def traffic_light(road, green_time):

    print(f"\n🚦 {road} Road Signal")

    
    print(f"{GREEN} GREEN - Vehicles can go")

    for remaining in range(green_time, 0, -1):
        print(f"\rGreen time remaining: {remaining} sec", end="")
        time.sleep(1)

    print()

    
    print(f"{YELLOW} YELLOW - Slow down")
    time.sleep(3)

    
    print(f"{RED} RED - Stop")
    time.sleep(2)


def emergency_mode(road):

    print("\n🚨 EMERGENCY MODE ACTIVATED 🚨")
    print(f"Giving priority to {road} Road")

    print(f"{GREEN} {road} Road → GREEN")

    time.sleep(10)

    print(f"{RED} {road} Road → RED")


def main():

    print("==========================================")
    print("     🚦 TRAFFIC LIGHT MANAGEMENT SYSTEM")
    print("==========================================")

    while True:

        # Generate traffic
        traffic = generate_traffic()

        # Display current traffic
        display_traffic(traffic)

        # Find road with maximum traffic
        busiest_road = max(traffic, key=traffic.get)

        print(f"\n🚗 Busiest Road: {busiest_road}")

        # Ask user for emergency mode
        choice = input(
            "\nEnter 'E' for emergency mode or press ENTER to continue: "
        )

        if choice.upper() == "E":

            emergency_mode(busiest_road)

        else:

            # Sort roads according to traffic
            sorted_roads = sorted(
                traffic,
                key=traffic.get,
                reverse=True
            )

            # Manage signals
            for road in sorted_roads:

                green_time = calculate_green_time(
                    traffic[road]
                )

                print(
                    f"\nTraffic on {road}: "
                    f"{traffic[road]} vehicles"
                )

                print(
                    f"Green light duration: "
                    f"{green_time} seconds"
                )

                traffic_light(road, green_time)

        
        again = input(
            "\nDo you want to continue? (Y/N): "
        )

        if again.upper() != "Y":
            print("\n🚦 Traffic Management System Stopped.")
            break


if __name__ == "__main__":
    main()