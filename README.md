# WhatsApp Contact Scraper

A Python-based tool that automates the extraction of contact details from WhatsApp Web using Selenium. 
The **WhatsApp Contact Scraper** simplifies the process of gathering profile data, such as names, profile pictures, 
and account types (Personal or Business), for a list of mobile numbers provided in an Excel file.

## Features

- Automates login to WhatsApp Web for data extraction.
- Reads a list of mobile numbers from an Excel file.
- Extracts the following details for each contact:
  - Name
  - Profile picture link
  - Account type (Personal or Business)
- Saves the extracted data incrementally to a CSV file.
- Uses Selenium for browser automation.

## Requirements

### Software and Libraries
- **Python 3.8+**
- **Selenium**: For browser automation.
- **Pandas**: For handling Excel and CSV files.

### WebDriver
- **Google Chrome** (ensure you have the latest version installed).
- **ChromeDriver**: Download the compatible version for your Chrome browser from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).

### Input File
An Excel file named `Book1.xlsx` with a column named `MobileNumber` containing the list of mobile numbers to scrape.

### Output
The output CSV file will contain the following columns:

- MobileNumber: The phone number.
- Name: The name of the contact (if available).
- Profile: The URL of the profile picture (if available).
- Whatsapp: The account type (Personal, Business, or Not Valid).


