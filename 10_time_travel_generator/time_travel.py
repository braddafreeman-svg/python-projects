# --- Imports ---
import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# --- Get current date and time ---
now = dt.datetime.now()
current_date = now.date()
current_time = now.time()

print("Current date:", current_date)
print("Current time:", current_time)

# --- Random time travel details ---
target_year = randint(1800, 2200)

destinations = [
    "Ancient Rome",
    "Medieval England",
    "The Wild West",
    "Future Mars Colony",
    "Renaissance Italy"
]
destination = choice(destinations)

# --- Calculate cost ---
base_cost = Decimal("1000.00")
year_difference = abs(target_year - current_date.year)
cost_multiplier = Decimal(year_difference) / Decimal("10")

final_cost = base_cost + (base_cost * cost_multiplier)
final_cost = final_cost.quantize(Decimal("0.00"))  # 2dp

# --- Generate and print message ---
message = custom_module.generate_time_travel_message(
    target_year,
    destination,
    final_cost
)

print("\n" + message)



