import pyautogui
import time
from datetime import datetime

# Set the start and end times for when the script should run (24-hour format)
start_time = datetime.now().replace(hour=7, minute=0, second=0)
end_time = datetime.now().replace(hour=23, minute=0, second=0)

# Set the duration for the back-and-forth movement
movement_duration = 5  # Adjust this as needed (in seconds)

# Set the distance for the back-and-forth movement (in pixels)
movement_distance = 100  # Adjust this as needed

# Loop to perform back-and-forth mouse movements during the specified time range
while True:
   current_time = datetime.now()

   # Check if the current time is within the desired range
   if start_time <= current_time <= end_time:
       # Calculate the start and end coordinates for the movement
       start_x, start_y = pyautogui.position()
       end_x = start_x + movement_distance
       end_y = start_y

       # Perform the back-and-forth movement
       pyautogui.moveTo(end_x, end_y, duration=movement_duration/2)
       pyautogui.moveTo(start_x, start_y, duration=movement_duration/2)
   else:
       # If the current time is outside the desired range, wait for a while before checking again
       time.sleep(3600)  # Sleep for 1 hour (3600 seconds) before checking again