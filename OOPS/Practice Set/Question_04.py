# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.


class Train:
    def __init__(self, name, fare, total_seats):
        self.name = name
        self.fare = fare
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_ticket(self):
        if self.available_seats > 0:
            print(f"Ticket booked successfully! Seat number: {self.total_seats - self.available_seats + 1}")
            self.available_seats -= 1
        else:
            print("Sorry, no seats available.")

    def get_status(self):
        print(f"Train: {self.name}")
        print(f"Available Seats: {self.available_seats}/{self.total_seats}")

    def get_fare_info(self):
        print(f"Fare for the train '{self.name}' is ₹{self.fare}")

# Example Usage:
train1 = Train("Rajdhani Express", 1500, 5)

train1.get_status()
train1.get_fare_info()

train1.book_ticket()
train1.book_ticket()
train1.get_status()


'''
Output :- 

Train: Rajdhani Express
Available Seats: 5/5
Fare for the train 'Rajdhani Express' is ₹1500
Ticket booked successfully! Seat number: 1
Ticket booked successfully! Seat number: 2
Train: Rajdhani Express
Available Seats: 3/5
'''

