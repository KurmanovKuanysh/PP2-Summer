#Calculate Two Date Difference in Seconds
from datetime import datetime

# Define two dates
date1 = datetime(2023, 6, 1, 12, 0, 0)
date2 = datetime(2023, 6, 28, 12, 0, 0)

# Calculate the difference
difference = date2 - date1

# Convert the difference to seconds
difference_in_seconds = difference.total_seconds()

print("Difference in seconds:", difference_in_seconds)
