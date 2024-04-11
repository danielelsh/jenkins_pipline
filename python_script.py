import datetime
import platform
import tempfile
import os
import boto3


current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H.%M.%S")
temp_folder = tempfile.gettempdir()
os_name = platform.system()
os_version = platform.version()
fp = os.path.join(temp_folder, f"{formatted_datetime}_artifact.txt")


def upload_file_to_s3(file_path):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, "danielshemesh", f"jenkins_artifacts/{formatted_datetime}_artifact.txt")
    except Exception as e:
        print("Error uploading file to S3:", e)


with open(fp, "w") as file:
    file.write("Current Date and Time: " + formatted_datetime + "\n")
    file.write("Operating System: " + os_name + "\n")
    file.write("OS Version: " + os_version + "\n")

upload_file_to_s3(fp)