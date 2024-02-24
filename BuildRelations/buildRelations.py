import os
import random
from datetime import datetime, timedelta

BASE_TERM_COLOR = "\033[32m"
ERROR_COLOR = "\033[31m"
END_COLOR = "\033[0m"


def pColor(text, color="red"):
    """
    Print the given text in the specified color.
    Parameters:
    text (str): The text to be printed.
    color (str): The color to be used for printing. Default is "red".
    Available colors: red, green, yellow, blue, lime, gold, magenta, cyan, white, orange, purple, neon (which is like a pale green? Not neon but okay...)
    Returns:
    None
    """
    color = color.lower()
    if color == "red":
        print(f"\033[31m{text}\033[0m")
    elif color == "green":
        print(f"\033[32m{text}\033[0m")
    elif color == "yellow":
        print(f"\033[33m{text}\033[0m")
    elif color == "blue":
        print(f"\033[34m{text}\033[0m")
    elif color == "lime":
        print(f"\033[38;5;118m{text}\033[0m")
    elif color == "gold":
        print(f"\033[38;5;220m{text}\033[0m")
    elif color == "magenta":
        print(f"\033[35m{text}\033[0m")
    elif color == "cyan":
        print(f"\033[36m{text}\033[0m")
    elif color == "white":
        print(f"\033[37m{text}\033[0m")
    elif color == "orange":
        print(f"\033[38;5;208m{text}\033[0m")
    elif color == "purple":
        print(f"\033[38;5;135m{text}\033[0m")
    elif color == "neon":
        print(f"\033[38;5;156m{text}\033[0m")
    else:
        # Default to lime, but this should never actually get called lol
        print(f"\033[38;5;118m{text}\033[0m")


def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def write_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")


def exists_in_file(filename, data):
    """
    Check if the given data exists in the specified file.

    Args:
        filename (str): The path to the file.
        data (str): The data to search for in the file.

    Returns:
        bool: True if the data exists in the file, False otherwise.
    """
    existing_data = read_file(filename)
    return data in existing_data


def guest_exists(guest_details):
    """
    Check if a guest with the given details already exists in the guest list.

    Parameters:
    guest_details (list): A list containing the guest details to be checked.

    Returns:
    bool: True if a guest with the given details exists, False otherwise.
    """
    guests = read_file("Guests.txt")
    for guest in guests:
        existing_details = guest.split(",")[
            1:-1
        ]  # Ignore guestno and zipcode for comparison
        if guest_details == existing_details:
            return True
    return False


def hotel_has_rooms(hotelno):
    """
    Check if a hotel has any rooms.

    Args:
        hotelno (str): The hotel number to check.

    Returns:
        bool: True if the hotel has rooms, False otherwise.
    """
    rooms = read_file("./Raw-Relations/Rooms.txt")
    return any(hotelno == room.split(",")[1] for room in rooms)


def generate_guests():
    """
    Generates new guest records and adds them to the Guests.txt file.

    Reads the existing guest records from the Guests.txt file, prompts the user to enter
    information for new guests, and adds the new guest records to the file if they do not
    already exist.

    Args:
        None

    Returns:
        None
    """
    guests = read_file("./Raw-Relations/Guests.txt")
    if len(guests) > 0:
        max_guestno = max([int(guest.split(",")[0]) for guest in guests], default=0)
    else:
        max_guestno = 0
    num_guests = int(
        input(f"\n{BASE_TERM_COLOR}How many guests are you adding?{END_COLOR} ")
    )
    for _ in range(num_guests):
        name = input(f"{BASE_TERM_COLOR}Enter guest's name:{END_COLOR} ")
        city = input(f"{BASE_TERM_COLOR}Enter guest's city:{END_COLOR} ")
        address = input(f"{BASE_TERM_COLOR}Enter guest's address:{END_COLOR} ")
        zipcode = input(f"{BASE_TERM_COLOR}Enter guest's zipcode:{END_COLOR} ")
        guest_details = [name, city, address]
        if not guest_exists(guest_details):
            max_guestno += 1
            guest_data = f"{max_guestno},'{name}','{city}','{address}',{zipcode}"
            write_file("./Raw-Relations/Guests.txt", guest_data)
        else:
            pColor("This guest already exists. Please try again.", "red")


def generate_hotels():
    """
    Generates hotels based on user input and stores them in a file.

    Reads the existing hotels from the "Hotels.txt" file, prompts the user to enter details for new hotels,
    and appends the new hotel data to the file if it doesn't already exist.

    Returns:
        None
    """
    hotels = read_file("./Raw-Relations/Hotels.txt")
    hotel_linecount = 0
    for hotelc in hotels:
        pColor(hotelc, "yellow")
        hotel_linecount = hotel_linecount + 1
    if len(hotels) > 1:
        pColor(f" the len(hotels) is {len(hotels)}")
        max_hotelno = max([int(hotel.split(",")[0]) for hotel in hotels], default=0)
    else:
        max_hotelno = 0
    num_hotels = int(
        input(f"{BASE_TERM_COLOR}\nHow many hotels are you adding?{END_COLOR} ")
    )
    for _ in range(num_hotels):
        hotelno = max_hotelno + 1
        name = input(f"{BASE_TERM_COLOR}Enter hotel name:{END_COLOR} ")
        city = input(f"{BASE_TERM_COLOR}Enter hotel city:{END_COLOR} ")
        state = input(f"{BASE_TERM_COLOR}Enter hotel state:{END_COLOR} ")
        address = input(f"{BASE_TERM_COLOR}Enter hotel address:{END_COLOR} ")
        zipcode = input(f"{BASE_TERM_COLOR}Enter hotel zipcode:{END_COLOR} ")
        star = input(f"{BASE_TERM_COLOR}Enter hotel star rating:{END_COLOR} ")
        hotel_data = (
            f"{hotelno},'{name}','{city}','{state}','{address}',{zipcode},{star}\n"
        )
        if not exists_in_file("./Raw-Relations/Hotels.txt", hotel_data):
            write_file("./Raw-Relations/Hotels.txt", hotel_data)
            max_hotelno += 1
        else:
            pColor("This hotel already exists. Please try again.", "red")


def generate_rooms():
    """
    Generates rooms for a selected hotel.

    Reads the list of hotels from "Hotels.txt" file and prompts the user to select a hotel by hotel number.
    Then, it reads the list of existing rooms from "Rooms.txt" file and determines the maximum room number for the selected hotel.
    Asks the user to input the number of rooms to be added to the selected hotel.
    Generates the specified number of rooms with random room numbers, types, and prices.
    Appends the room data to the "Rooms.txt" file.
    """
    if not os.path.exists("./Raw-Relations/Hotels.txt"):
        pColor(
            "\n./Raw-Relations/Hotels.txt does not exist. Please generate hotels first."
        )
        return
    hotels = read_file("./Raw-Relations/Hotels.txt")
    for hotel in hotels:
        pColor(hotel, "yellow")
    hotelno = input(f"\n{BASE_TERM_COLOR}Select a hotel by hotel number:: {END_COLOR}")
    rooms = read_file("./Raw-Relations/Rooms.txt")
    if len(rooms) > 0:
        max_roomno = max(
            [
                int(room.split(",")[0])
                for room in rooms
                if room.split(",")[1] == hotelno
            ],
            default=0,
        )
    else:
        max_roomno = 0
    num_rooms = int(
        input(
            f"{BASE_TERM_COLOR}How many rooms are you adding to hotel {hotelno}?{END_COLOR} "
        )
    )
    for _ in range(num_rooms):
        roomno = max_roomno + 1
        type = random.choice(
            [
                "2 Queen Beds",
                "1 King Bed",
                "Junior Suite",
                "Deluxe Suite",
                "Villa 1 Bedroom",
                "Villa 2 Bedroom",
            ]
        )
        price = random.randint(50, 500)
        room_data = f"{roomno},{hotelno},'{type}',{price}"
        write_file("./Raw-Relations/Rooms.txt", room_data)
        max_roomno += 1


def generate_bookings():
    """
    Generates bookings based on user input for guest, hotel, room, and date information.

    If there are no guests available, it displays an error message and returns.
    If there are no hotels or rooms available, it displays an error message and returns.
    If the selected hotel has no rooms, it displays an error message and returns.

    The function prompts the user to select a guest, hotel, and room for booking.
    If the user chooses to provide dates, it prompts for start and end dates.
    If the user chooses not to provide dates, it generates random dates within a range.

    The booking information is then written to a file named "Bookings.txt".
    """
    if not os.path.exists("./Raw-Relations/Guests.txt"):
        pColor(
            "\nUnable to locate Guests.txt in the Raw-Relations directory. Please generate guests first.",
            "red",
        )
        return
    guests = read_file("./Raw-Relations/Guests.txt")
    for guest in guests:
        pColor(guest)
    guestno = input(
        f"{BASE_TERM_COLOR}Select a guest by their guest number for booking: {END_COLOR}"
    )
    if (
        not os.path.exists("./Raw-Relations/Hotels.txt")
        or not os.path.exists("./Raw-Relations/Rooms.txt")
        or read_file("./Raw-Relations/Hotels.txt") == []
    ):
        pColor(
            "Hotels or rooms data not available. Please generate hotels and rooms first.\n",
        )
        return
    hotels = read_file("./Raw-Relations/Hotels.txt")
    for hotel in hotels:
        print(hotel)
    hotelno = input(
        f"{BASE_TERM_COLOR}\nSelect a hotel by their hotel number for booking: {END_COLOR} "
    )
    if not hotel_has_rooms(hotelno):
        print(
            f"{ERROR_COLOR}This hotel has no rooms. Please add rooms to this hotel before booking.{END_COLOR}"
        )
        return
    rooms = [
        room
        for room in read_file("./Raw-Relations/Rooms.txt")
        if room.split(",")[1] == hotelno
    ]
    for room in rooms:
        print(room)
    roomno = input(f"{BASE_TERM_COLOR}Select a room by roomno for booking: {END_COLOR}")
    date_choice = input(
        f"{BASE_TERM_COLOR}Do you want to provide dates (y/n)? {END_COLOR}"
    )
    if date_choice.lower() == "y":
        datefrom = input(f"{BASE_TERM_COLOR}Enter start date (YYYY-MM-DD): {END_COLOR}")
        dateto = input(f"{BASE_TERM_COLOR}Enter end date (YYYY-MM-DD): {END_COLOR}")
    else:
        start_date = datetime(
            random.randint(2018, 2025), random.randint(1, 12), random.randint(1, 28)
        )
        duration = random.randint(1, 30)
        datefrom = start_date.strftime("%Y-%m-%d")
        dateto = (start_date + timedelta(days=duration)).strftime("%Y-%m-%d")
    booking_data = f"{hotelno},{guestno},{datefrom},{dateto},{roomno}"
    write_file("./Raw-Relations/Bookings.txt", booking_data)


def create_relations():
    """Create relations will convert our txt files into the relational schema used in RelaX so that we can use it in our homework."""
    pColor(
        'We will attempt to create the relations for you. All files will be preceded by "rel_". Preexisting rel files will be overwritten.'
    )
    # Create the relations
    try:
        with open("./Relations/rel_Guest.txt", "w") as rel_guests:
            signature = "Guest = { guestno:number, name:string, city:string, address:string, zipcode:number\n"
            rel_guests.write(signature + "\n")
            guests = read_file("./Raw-Relations/Guests.txt")
            for guest in guests:
                rel_guests.write(guest + "\n")
            rel_guests.write("\n}")
        pColor("rel_Guests.txt created", "green")
    except Exception as e:
        pColor(f"Error creating rel_Guest.txt: {e}", "red")
    try:
        with open("./Relations/rel_Hotel.txt", "w") as rel_hotels:
            signature = "Hotel = { hotelno:number, name:string, city:string, state:string, address:string, zipcode:number, star:number\n"
            rel_hotels.write(signature + "\n")
            hotels = read_file("./Raw-Relations/Hotels.txt")
            for hotel in hotels:
                rel_hotels.write(hotel + "\n")
            rel_hotels.write("}")
        pColor("rel_Hotels.txt created", "green")
    except Exception as e:
        pColor(f"Error creating rel_Hotel.txt: {e}", "red")
    try:
        with open("./Relations/rel_Room.txt", "w") as rel_rooms:
            signature = (
                "Room = { roomno:number, hotelno:number, type:string, price:number\n"
            )
            rel_rooms.write(signature + "\n")
            rooms = read_file("./Raw-Relations/Rooms.txt")
            for room in rooms:
                rel_rooms.write(room + "\n")
            rel_rooms.write("\n}")
        pColor("rel_Rooms.txt created", "green")
    except Exception as e:
        pColor(f"Error creating rel_Rooms.txt: {e}", "red")
    try:
        with open("./Relations/rel_Booking.txt", "w") as rel_bookings:
            signature = "Booking = { hotelno:number, guestno:number, datefrom:date, dateto:date, roomno:number\n"
            rel_bookings.write(signature + "\n")
            bookings = read_file("./Raw-Relations/Bookings.txt")
            for booking in bookings:
                rel_bookings.write(booking + "\n")
            rel_bookings.write("\n}")
        pColor("rel_Booking.txt created", "green")
    except Exception as e:
        pColor(f"Error creating rel_Booking.txt: {e}", "red")

    pColor(
        "\nRelation Conversion complete! Please proofread it and check for errors!",
        "green",
    )


def create_dataset():
    """This willattempt to create a dataset for the purpose of the project."""
    try:
        nameofgroup = input("Please give a name to the dataset:\t")
    except Exception as e:
        pColor(f"Error creating dataset: {e}", "red")
        return
    header = f"group: {nameofgroup}"

    try:
        desc = input("Please give a description to the dataset:\t")
        header += f"\n\t\tdescription:\t{desc}\n\n"
    except Exception as e:
        pColor(f"Error creating dataset: {e}", "red")
        return

    # Import all relations
    try:
        # Get the files found in ./Relations
        rel_files = os.listdir("./Relations/")
        rel_files = [rel_file for rel_file in rel_files if rel_file.startswith("rel_")]
        pColor(f"Found the following rel files: {rel_files}")
        if len(rel_files) == 0:
            pColor("No rel files found. Please run CreateRelations first.", "red")
            return
        pColor(
            f"Attempting to create the dataset using {rel_files} Creating the dataset..."
        )
        with open(f"./BuiltDatasets/{nameofgroup}.txt", "w") as dataset:
            dataset.write(header + "\n")
            dataset.close()

        for rel_file in rel_files:
            with open(f"./Relations/{rel_file}", "r") as file:

                rel_data = file.read()
                with open(f"./BuiltDatasets/{nameofgroup}.txt", "a") as dataset:
                    dataset.write(rel_data + "\n")
                    # CLOSE THE FILE
                    dataset.close()
                file.close()
        pColor("Dataset created!", "green")
        # Cleanup the Relations directory by creating a subfolder with the name of the group and moving all rel_ files into it
        try:
            os.mkdir(f"./Relations/{nameofgroup}")
            for rel_file in rel_files:
                os.rename(
                    f"./Relations/{rel_file}", f"./Relations/{nameofgroup}/{rel_file}"
                )
            pColor("Rel files moved to the dataset folder", "green")

        except Exception as e:
            pColor(f"Error moving rel files: {e}", "red")

    except Exception as e:
        pColor(f"Error finding rel files: {e}", "red")


def main():
    actions = {
        "1": generate_guests,
        "2": generate_hotels,
        "3": generate_rooms,
        "4": generate_bookings,
        "5": create_relations,
        "6": create_dataset,
        "-1": exit,
    }
    while True:
        action = input(
            f"\nChoose an action using its corresponding number\n{BASE_TERM_COLOR}1{END_COLOR}:\tgenerate guests\n{BASE_TERM_COLOR}2{END_COLOR}:\tgenerate hotels\n{BASE_TERM_COLOR}3{END_COLOR}:\tgenerate rooms\n{BASE_TERM_COLOR}4{END_COLOR}:\tgenerate bookings\n{BASE_TERM_COLOR}5{END_COLOR}:\tCreateRelations\n{BASE_TERM_COLOR}6{END_COLOR}:\tCreate Dataset\n{ERROR_COLOR}-1{END_COLOR}:\tExit\nYour choice:\t"
        )
        if action in actions:
            actions[action]()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
