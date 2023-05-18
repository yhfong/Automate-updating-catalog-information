#!/usr/bin/env python3

import os
import datetime
import reports
import emails

# Function to make the format for the report
def file_to_report(file):
    with open(file) as f:
        name = "name: {}".format(f.readline())
        weight = "weight: {}".format(f.readline())
    return "{}<br /> {}<br /><br />".format(name, weight)


def main():
    # Input the information from the txt file for the report
    path = "supplier-data/descriptions/"
    txt_files = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            txt_files.append(path + file)

    attachment = "/tmp/processed.pdf"

    # Obtain the necessary information from txt file by above function to the report format
    paragraph = ""
    for file in txt_files:
        paragraph += file_to_report(file)

    # Input the time by datetime module
    today = datetime.datetime.today()
    title = "Processed Update on {} {}, {}".format(today.strftime("%b"), today.day, today.year)

    # Create the report and temporary store in above attachment position
    reports.generate_report(attachment, title, paragraph)

    # Input the content for the e-mail
    content = {
        "sender": "automation@example.com",
        "recipient": "{}@example.com".format(os.environ.get("USER")),
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": attachment,
    }

    # Create the email and send out
    message = emails.generate_email(content)
    emails.send_email(message)

if __name__ == "__main__":
    main()