flights = []
bookings = []

def add_flight():
    no = input("Flight Number: ")
    source = input("Source: ")
    dest = input("Destination: ")
    seats = int(input("Seats: "))
    flights.append([no, source, dest, seats])
    print("Flight added successfully")

def view_flights():
    for f in flights:
        print(f"Flight: {f[0]} | {f[1]} -> {f[2]} | Seats: {f[3]}")

def book_ticket():
    no = input("Flight Number: ")
    name = input("Passenger Name: ")

    for f in flights:
        if f[0] == no and f[3] > 0:
            f[3] -= 1
            bookings.append([name, no])
            print("Ticket booked successfully")
            return

    print("Flight unavailable")

def view_bookings():
    for b in bookings:
        print("Passenger:", b[0], "| Flight:", b[1])

while True:
    print("\n1.Add Flight 2.View Flights 3.Book Ticket 4.Bookings 5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_flight()
    elif choice == "2":
        view_flights()
    elif choice == "3":
        book_ticket()
    elif choice == "4":
        view_bookings()
    elif choice == "5":
        break