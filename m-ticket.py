class Star_Cinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

    def view_all_shows(self):
        if not self.hall_list:
            print("No halls available.")
            return
        for hall in self.hall_list:
            hall.view_show_list()

    def view_available_seats(self):
        try:
            show_id = int(input("Enter show ID: "))
            for hall in self.hall_list:
                hall.view_available_seats(show_id)
        except ValueError:
            print("Invalid input. Please enter a valid show ID.")

    def book_ticket(self):
        try:
            show_id = int(input("Enter show ID: "))
            row = int(input("Enter seat row: "))
            col = int(input("Enter seat column: "))
            for hall in self.hall_list:
                hall.book_seats(show_id, [(row, col)])
        except ValueError:
            print("Invalid input. Please enter valid show ID, row, and column.")

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        seats = [[0 for j in range(self.__cols)] for i in range(self.__rows)]
        self.__seats[id] = seats

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            raise ValueError("Invalid show ID")
        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                raise ValueError("Invalid seat")
            if self.__seats[id][row][col] == 1:
                raise ValueError("Seat already booked")
            self.__seats[id][row][col] = 1
            print(f"Seat ({row}, {col}) booked for show {id}")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows running")
            return
        for show in self.__show_list:
            print(f"Movie: {show[1]} ({show[0]}) - Show ID: {show[0]} - Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            raise ValueError("Invalid show ID")
        print(f"Available seats for show {id}:")
        for row in self.__seats[id]:
            print(row)

def main():
    cinema = Star_Cinema()

    hall1 = Hall(7, 7, 1)
    hall1.entry_show(111, "Jawan", "11:00 AM")
    hall1.entry_show(333, "Pathan", "2:00 PM")
    cinema.entry_hall(hall1)

    
    while True:
        print("1. View all shows today")
        print("2. View available seats")
        print("3. Book ticket")
        print("4. Exit")
        try:
            choice = int(input("Enter option: "))
            if choice == 1:
                cinema.view_all_shows()
            elif choice == 2:
                cinema.view_available_seats()
            elif choice == 3:
                cinema.book_ticket()
            elif choice == 4:
                break
            else:
                print("Invalid option. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
