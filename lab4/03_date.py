# Drop Microseconds from Datetime
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Drop microseconds
current_datetime_no_microseconds = current_datetime.replace(microsecond=0)

print("Current Datetime with Microseconds:", current_datetime)
print("Current Datetime without Microseconds:", current_datetime_no_microseconds)
