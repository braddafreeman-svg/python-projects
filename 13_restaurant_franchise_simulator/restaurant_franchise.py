# --- Making the Menus ---

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total


brunch = Menu(
    "brunch",
    {
        'pancakes': 7.50,
        'waffles': 9.00,
        'burger': 11.00,
        'home fries': 4.50,
        'coffee': 1.50,
        'espresso': 3.00,
        'tea': 1.00,
        'mimosa': 10.50,
        'orange juice': 3.50
    },
    "11am",
    "4pm"
)

early_bird = Menu(
    "early-bird",
    {
        'salumeria plate': 8.00,
        'salad and breadsticks (serves 2, no refills)': 14.00,
        'pizza with quattro formaggi': 9.00,
        'duck ragu': 17.50,
        'mushroom ravioli (vegan)': 13.50,
        'coffee': 1.50,
        'espresso': 3.00
    },
    "3pm",
    "6pm"
)

dinner = Menu(
    "dinner",
    {
        'crostini with eggplant caponata': 13.00,
        'caesar salad': 16.00,
        'pizza with quattro formaggi': 11.00,
        'duck ragu': 19.50,
        'mushroom ravioli (vegan)': 13.50,
        'coffee': 2.00,
        'espresso': 3.00
    },
    "5pm",
    "11pm"
)

kids = Menu(
    "kids",
    {
        'chicken nuggets': 6.50,
        'fusilli with wild mushrooms': 12.00,
        'apple juice': 3.00
    },
    "11am",
    "9pm"
)

# 8) Test string representation
print(brunch)

# 10) Test calculate_bill for brunch order
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

# 11) Test calculate_bill for early-bird order
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))


# --- Creating the Franchises ---

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Franchise location: {}".format(self.address)

    def available_menus(self, time):
        available = []
        for menu in self.menus:
            # time is assumed to be an int like 12, 17 etc
            if menu.start_time <= time <= menu.end_time:
                available.append(menu)
        return available


# NOTE:
# The original Codecademy project usually uses integers for time (ex: 11, 16, 17, 23)
# So we will create another set of menus using int times for available_menus() to work correctly.

brunch_int = Menu(brunch.name, brunch.items, 11, 16)
early_bird_int = Menu(early_bird.name, early_bird.items, 15, 18)
dinner_int = Menu(dinner.name, dinner.items, 17, 23)
kids_int = Menu(kids.name, kids.items, 11, 21)

flagship_store = Franchise("1232 West End Road", [brunch_int, early_bird_int, dinner_int, kids_int])
new_installment = Franchise("12 East Mulberry Street", [brunch_int, early_bird_int, dinner_int, kids_int])

# 15) Test franchise representation
print(flagship_store)

# 17) Test available_menus at 12 noon
print(flagship_store.available_menus(12))

# 18) Test available_menus at 5pm (17)
print(flagship_store.available_menus(17))


# --- Creating Businesses ---

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# 22) Arepas menu (10am to 8pm)
arepas_menu = Menu(
    "Take a' Arepa",
    {
        'arepa pabellon': 7.00,
        'pernil arepa': 8.50,
        'guayanes arepa': 8.00,
        'jamon arepa': 7.50
    },
    10,
    20
)

# 23) Arepas franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# 24) Arepas business
take_a_arepa = Business("Take a' Arepa", [arepas_place])

