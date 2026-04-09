#buoi1
import time

# Get the current time in seconds since the epoch
current_seconds = time.time()

# Define constants for time conversion
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_DAY = 24 * 60 * 60

# Calculate total days since the epoch
days_since_epoch = int(current_seconds // SECONDS_IN_DAY)

# Calculate the remaining seconds in the current day
remaining_seconds = current_seconds % SECONDS_IN_DAY

# Calculate hours, minutes, and seconds from the remaining seconds
hours = int(remaining_seconds // SECONDS_IN_HOUR)
remaining_seconds %= SECONDS_IN_HOUR

minutes = int(remaining_seconds // SECONDS_IN_MINUTE)
seconds = int(remaining_seconds % SECONDS_IN_MINUTE)

# Display the results
print(f"Days since epoch: {days_since_epoch}")
print(f"Current time (GMT): {hours:02}:{minutes:02}:{seconds:02}")
