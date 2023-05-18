# Automate-updating-catalog-information

# This is the final course project for the Google IT Automation with Python Professional Certificate. 

# In this case, we work for an online fruits store, and need to develop a system that will update the catalog information with data provided by our suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. We also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to the Django server.

# We create a series of Python script that will process the images and descriptions and then update the company's online website to add the new products as follow:
# 1. changeImage.py : Resize the images and change the format from .TIF to .JPEG by the os module and PIL module
# 2. supplier_image_upoad.py: Upload all the .JPEG file to the web service by requests module
# 3. run.py: Read all the product description from .txt file, obtain the infromation by regular expression module and upload to the web by requests module
# 4. reports.py: Create a function to generate a report as basic format by reportlab module
# 5. emails.py: Create a function to send out a basic format email with attachment by email, minetypes and smtplib module
# 6. report_email.py: Collect all the informaiton from .txt file, create a report by reports.py and then send out the email by emails.py including input of date by datetime module

# After running the above Python script, the supplier shall be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

# Besides, in parallel to the automation running, a health_check.py Python script is created to check the health of the system and send an email if something goes wrong. The three modules : shutil, socket and psuti is used for the health check of the system for the following situation:
# 1. Report an error if CPU usage is over 80%
# 2. Report an error if available disk space is lower than 20%
# 3. Report an error if available memory is less than 500MB
# 4. Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
