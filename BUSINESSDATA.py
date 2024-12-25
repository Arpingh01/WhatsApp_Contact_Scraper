import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_driver_path = "C:\\Users\\DELL\\PycharmProjects\\Data_Scrapper_Project\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 1: Open WhatsApp Web
print("Log in to WhatsApp Web manually...")
driver.get("https://web.whatsapp.com/")
time.sleep(22)  # Increased wait time for user to scan the QR code

# Step 2: Read the mobile numbers from Excel file
excel_file = "Book1.xlsx"
data = pd.read_excel(excel_file)
mobile_numbers = data["MobileNumber"].astype(str)

# Prepare output CSV file
output_file = "output.csv"
output_data = []

# Save an empty file initially
pd.DataFrame(output_data).to_csv(output_file, index=False)

for mobile in mobile_numbers:
    try:
        print(f"Processing mobile number: {mobile}")
        # Step 3: Open the wa.me URL
        wa_url = f"https://wa.me/{mobile}"
        driver.get(wa_url)
        time.sleep(3)  # Reduced delay for optimization

        # Step 4: Extract the name
        try:
            name_element = driver.find_element(By.XPATH, "//*[@id='main_block']/div[1]/h3")
            name = name_element.text
        except:
            name = "N/A"

        # Click on the action button to load the chat
        try:
            action_button = driver.find_element(By.XPATH, "//*[@id='action-button']/span")
            action_button.click()
            time.sleep(3)
        except:
            print("Action button not found or clickable.")

        # Go to the fallback block if needed
        try:
            fallback_block = driver.find_element(By.XPATH, "//*[@id='fallback_block']/div/div/h4[2]/a/span")
            fallback_block.click()
            time.sleep(10)
        except:
            print("Fallback block not found or clickable.")

        # Step 5: Extract the profile source link
        try:
            profile_img = driver.find_element(By.XPATH, "//*[@id='main']/header/div[1]/div/img")
            profile_src = profile_img.get_attribute("src")
        except:
            profile_src = "N/A"

        try:
            header_block = driver.find_element(By.XPATH,"//*[@id='main']/header/div[2]/div/div/div/span")
            header_block.click()
            time.sleep(3)
        except:
            print("header block not found or clickable.")

        # Step 6: Check if it's a business account
        try:
            business_indicator = driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div/div[5]/span/div/span/div/div/section/div[2]/div/div/div[1]")
            account_type = "Business" if "This is a business account." in business_indicator.text else "Personal"
        except:
            account_type = "Not Valid"

        # Append extracted data
        record = {
            "MobileNumber": mobile,
            "Name": name,
            "Profile": profile_src,
            "Whatsapp": account_type
        }
        output_data.append(record)

        # Save the output to CSV incrementally
        pd.DataFrame(output_data).to_csv(output_file, index=False)

    except Exception as e:
        print(f"Error processing {mobile}: {e}")

print("Data extraction completed. Saved to output.csv.")

# Close the WebDriver
driver.quit()
