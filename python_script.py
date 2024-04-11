import datetime
import platform
import tempfile
import os

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H.%M.%S")
temp_folder = tempfile.gettempdir()
os_name = platform.system()
os_version = platform.version()

fp = os.path.join(temp_folder, f"{formatted_datetime}_artifact.txt")
with open(fp, "w") as file:
    file.write("Current Date and Time: " + formatted_datetime + "\n")
    file.write("Operating System: " + os_name + "\n")
    file.write("OS Version: " + os_version + "\n")

print(f"artifact path: {fp}")