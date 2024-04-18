import random
import string
import pprint

# Define dictionaries to store booking references and customer data
booking_references = {}
customer_data = {}

# creat an empty dictionary
floor_plan={}

# provide the seat data
seat_data = [
    ["1A", "2A", "3A", "4A", "5A", "6A", "7A", "8A", "9A", "10A", "11A", "12A", "13A", "14A", "15A", "16A", "17A", "18A", "19A", "20A", "21A", "22A", "23A", "24A", "25A", "26A", "27A", "28A", "29A", "30A", "31A", "32A", "33A", "34A", "35A", "36A", "37A", "38A", "39A", "40A", "41A", "42A", "43A", "44A", "45A", "46A", "47A", "48A", "49A", "50A", "51A", "52A", "53A", "54A", "55A", "56A", "57A", "58A", "59A", "60A", "61A", "62A", "63A", "64A", "65A", "66A", "67A", "68A", "69A", "70A", "71A", "72A", "73A", "74A", "75A", "76A", "77A", "78A", "79A", "80A"],
    ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B", "11B", "12B", "13B", "14B", "15B", "16B", "17B", "18B", "19B", "20B", "21B", "22B", "23B", "24B", "25B", "26B", "27B", "28B", "29B", "30B", "31B", "32B", "33B", "34B", "35B", "36B", "37B", "38B", "39B", "40B", "41B", "42B", "43B", "44B", "45B", "46B", "47B", "48B", "49B", "50B", "51B", "52B", "53B", "54B", "55B", "56B", "57B", "58B", "59B", "60B", "61B", "62B", "63B", "64B", "65B", "66B", "67B", "68B", "69B", "70B", "71B", "72B", "73B", "74B", "75B", "76B", "77B", "78B", "79B", "80B"],
    ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "11C", "12C", "13C", "14C", "15C", "16C", "17C", "18C", "19C", "20C", "21C", "22C", "23C", "24C", "25C", "26C", "27C", "28C", "29C", "30C", "31C", "32C", "33C", "34C", "35C", "36C", "37C", "38C", "39C", "40C", "41C", "42C", "43C", "44C", "45C", "46C", "47C", "48C", "49C", "50C", "51C", "52C", "53C", "54C", "55C", "56C", "57C", "58C", "59C", "60C", "61C", "62C", "63C", "64C", "65C", "66C", "67C", "68C", "69C", "70C", "71C", "72C", "73C", "74C", "75C", "76C", "77C", "78C", "79C", "80C"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "11D", "12D", "13D", "14D", "15D", "16D", "17D", "18D", "19D", "20D", "21D", "22D", "23D", "24D", "25D", "26D", "27D", "28D", "29D", "30D", "31D", "32D", "33D", "34D", "35D", "36D", "37D", "38D", "39D", "40D", "41D", "42D", "43D", "44D", "45D", "46D", "47D", "48D", "49D", "50D", "51D", "52D", "53D", "54D", "55D", "56D", "57D", "58D", "59D", "60D", "61D", "62D", "63D", "64D", "65D", "66D", "67D", "68D", "69D", "70D", "71D", "72D", "73D", "74D", "75D", "76D", "S", "S", "79D", "80D"],
    ["1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E", "10E", "11E", "12E", "13E", "14E", "15E", "16E", "17E", "18E", "19E", "20E", "21E", "22E", "23E", "24E", "25E", "26E", "27E", "28E", "29E", "30E", "31E", "32E", "33E", "34E", "35E", "36E", "37E", "38E", "39E", "40E", "41E", "42E", "43E", "44E", "45E", "46E", "47E", "48E", "49E", "50E", "51E", "52E", "53E", "54E", "55E", "56E", "57E", "58E", "59E", "60E", "61E", "62E", "63E", "64E", "65E", "66E", "67E", "68E", "69E", "70E", "71E", "72E", "73E", "74E", "75E", "76E", "S", "S", "79E", "80E"],
    ["1F", "2F", "3F", "4F", "5F", "6F", "7F", "8F", "9F", "10F", "11F", "12F", "13F", "14F", "15F", "16F", "17F", "18F", "19F", "20F", "21F", "22F", "23F", "24F", "25F", "26F", "27F", "28F", "29F", "30F", "31F", "32F", "33F", "34F", "35F", "36F", "37F", "38F", "39F", "40F", "41F", "42F", "43F", "44F", "45F", "46F", "47F", "48F", "49F", "50F", "51F", "52F", "53F", "54F", "55F", "56F", "57F", "58F", "59F", "60F", "61F", "62F", "63F", "64F", "65F", "66F", "67F", "68F", "69F", "70F", "71F", "72F", "73F", "74F", "75F", "76F", "S", "S", "79F", "80F"]
]

# loop through the seat data to generate key-value pairs
for row in seat_data:
    for seat in row:
        if seat != "X" and seat != "S":  # generate key-value pair if it's not X or S
            floor_plan[seat] = "F"  # assign value "F" to each key

def generate_booking_reference(existing_references):
    """
        Generate a random booking reference with eight alphanumeric characters.
        Ensure the reference is unique.

        Parameters:
        - existing_references: List of existing booking references

        Returns:
        - Unique booking reference
    """
    # Define a function to generate a random booking reference
    while True:
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) # generate random alphanumeric characters
        if reference not in existing_references: # check if the reference is unique
            return reference

# define a function to display the menu
def display_menu():
    print("Seating Booking Application Menu")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")

# define the function to check the availability of seat
def Check_availability_of_seat(seat):
    if floor_plan.get(seat) == "F": # because floor_plan is a dictionary so we need use get() to get the value of the key
        return True
    else:
        return False

# Function to extract seat information
def extract_seat_info(seat): # to avoid such as 73A being extracted wrongly
    seat_row = seat[-1]    # I define a function to make sure whatever the seat number
    seat_column = seat[:-1]  # is 3A or 73A, both can extract their seat row and seat column properly
    return seat_row, seat_column

# define the function to book a seat
def Book_seat(seat, passport_number, first_name, last_name):
    if Check_availability_of_seat(seat):  # Check seat availability
        booking_ref = generate_booking_reference(booking_references.values())  # Generate booking reference
        booking_references[seat] = booking_ref  # Store booking reference for the seat
        seat_row, seat_column = extract_seat_info(seat)  # Extract seat row and column
        customer_data[booking_ref] = {
            'passport_number': passport_number,
            'first_name': first_name,
            'last_name': last_name,
            'seat_row': seat_row,
            'seat_column': seat_column
        }  # Store customer data
        floor_plan[seat] = booking_ref  # Mark seat as booked
        print(f"{seat} has been booked successfully! Booking reference: {booking_ref}")
    else:
        print(f"{seat} has already been booked!")


# define the function free a seat
def Free_seat(seat):
    if floor_plan.get(seat) != "F":  # Check if seat is booked
        booking_ref = floor_plan.pop(seat)  # Remove booking reference from floor plan
        del customer_data[booking_ref]  # Remove customer data
        floor_plan[seat] = "F"  # Mark seat as free
        print(f"{seat} has been freed successfully!")
    else:
        print(f"{seat} is already free!")

# define the function to show the booking state
def Show_booking_state():
    print("Current Booking State:")
    for row in seat_data:
        print(" ".join([floor_plan.get(seat, seat) for seat in row]))
        #use a list comprehension to iterate over each seat in the current row and get its booking status or original value.
        # .join() concatenates the retrieved booking statuses or original values of seats into a string with spaces between seats.
    pprint.pprint(customer_data) # use pprint module to print put the customer data

# define main function to run the program
def main():
    while True:
        display_menu() # Display the menu options to the user
        choice = input("please choose the operation you want:") # Prompt the user to enter their choice

        if choice == "1":
            seat = input("please enter the seat you want to check:") # Prompt the user to enter the seat number
            if Check_availability_of_seat(seat):  # Check if the seat is available
                print(f"{seat} is available!")
            else:
                print(f"{seat} is not available!")

        elif choice == "2":  # if the user chooses option 2
            seat = input("please enter the seat you want to book:")
            passport_number = input("please enter your passport number:")
            first_name = input("please enter your first name:")
            last_name = input("please enter your last name:")
            # prompt the user to enter the seat number
            Book_seat(seat, passport_number, first_name, last_name)  # book the seat

        elif choice == "3":  # if the user chooses option 3
            seat = input("please enter the seat you want to free:")  # prompt the user to enter the seat number
            Free_seat(seat)  # free the seat

        elif choice == "4":  # if the user chooses option 4
            Show_booking_state()  # show the current booking state

        elif choice == "5":  # if the user chooses option 5
            print("program has quit successfully!")  # print a message indicating that the program is exiting
            break  # exit the loop and end the program

        else:  # if the user enters an invalid choice
            print("invalid choice, please choose valid choice!")  # print a message indicating that the choice is invalid

if __name__ == "__main__":
    main()


