#!/usr/bin/env python3

import shutil
import socket
import psutil
import emails
import os

# Define variables for the health check
max_cpu_percentage = 80
min_available_disk_space = 20
min_available_memory = 500
check_local_host_ip = "127.0.0.1"


# Function to check the CPU usage if it is over the max_cpu_percentage
def check_CPU():
    cpu_usuage_percentage = psutil.cpu_percent(5)
    return cpu_usuage_percentage > max_cpu_percentage

# Function to check the disk space if it is lower than the min_available_disk_space
def check_disk_space():
    available_disk_space = 100 - psutil.disk_usage('/').percent
    return available_disk_space < min_available_disk_space

# Function to check the available memory if it is less than the min_available_memory
def check_memory():
    available_memory = psutil.virtual_memory().available
    return available_memory < min_available_memory*(2**20)

# Function to check if the hostname equal to the check_local_host_ip
def check_network():
    localhostip = socket.gethostbyname("localhost")
    return localhostip != check_local_host_ip

# Function with the content to send out alert email by input an alert message as subject
def send_alert(alert):
    content = {
        "sender": "automation@example.com",
        "recipient": "{}@example.com".format(os.environ.get("USER")),
        "subject": alert,
        "body": "Please check your systems and resolve the issue as soon as possible",
        "attachment": None,
    }

    try:
        message = emails.generate_email(content)
        emails.send_email(message)
    except:
        print("Cannot send alert notification!!!")


def main():
    alert = ""
    # Perform health check by function above and return the alert message if result is TRUE
    if check_CPU():
        alert = f"Error - CPU usage is over {max_cpu_percentage}%"
    elif check_disk_space():
        alert = f"Error - Available disk space is less than {min_available_disk_space}%"
    elif check_memory():
        alert = f"Error - Available memory is less than {min_available_memory}MB"
    elif check_network():
        alert = f"Error - localhost cannot be resolved to {chklocalhostip}"

    # Send out alert email with the alert message as subject if the alert is activated
    if alert:
        send_alert(alert)

if __name__ == "__main__":
    main()