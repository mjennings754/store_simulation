class Store:
    def __init__(self, brand, location, opening_hours):
        self.brand = brand
        self.location = location
        self.opening_hours = opening_hours

    def display_hours(self):
        print(f"{self.brand} {self.location}'S HOURS: {store_hours}")

store_hours = {
    "Mon-Fri": "10am - 6pm",
    "Saturday": "9am - 9pm",
    "Sunday": "10am - 7pm"
}
