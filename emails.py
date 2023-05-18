#!/usr/bin/env python3

import email.message
import mimetypes
import os
import smtplib

# Function to create an basic format email with input content
def generate_email(content):
  message = email.message.EmailMessage()
  message["From"] = content["sender"]
  message["To"] = content["recipient"]
  message["Subject"] = content["subject"]
  message.set_content(content["body"])

# Check and input if there is attachment for this email from the content
  if content["attachment"]!= None:
    # Process the attachment and add it to the email if found
    attachment_filename = os.path.basename(content["attachment"])
    mime_type, _ = mimetypes.guess_type(content["attachment"])
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(content["attachment"], 'rb') as ap:
      message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message

# Funciton to send out a email
def send_email(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()