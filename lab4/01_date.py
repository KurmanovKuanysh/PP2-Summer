#Subtract Five Days from Current Date
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date after subtracting 5 days:", new_date)
