from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
from datetime import datetime
import re

print('''
      
  ______   _______    ______   _______   ________        ______   __         ______   __    __  _______           ________  _______   ________  ________ 
 /      \ /       \  /      \ /       \ /        |      /      \ /  |       /      \ /  |  /  |/       \         /        |/       \ /        |/        |
/$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$$  |$$$$$$$$/      /$$$$$$  |$$ |      /$$$$$$  |$$ |  $$ |$$$$$$$  |        $$$$$$$$/ $$$$$$$  |$$$$$$$$/ $$$$$$$$/ 
$$ |__$$ |$$ |  $$ |$$ |  $$ |$$ |__$$ |$$ |__  ______ $$ |  $$/ $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ | ______ $$ |__    $$ |__$$ |$$ |__    $$ |__    
$$    $$ |$$ |  $$ |$$ |  $$ |$$    $$< $$    |/      |$$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |/      |$$    |   $$    $$< $$    |   $$    |   
$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$  |$$$$$/ $$$$$$/ $$ |   __ $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$$$$$/ $$$$$/    $$$$$$$  |$$$$$/    $$$$$/    
$$ |  $$ |$$ |__$$ |$$ \__$$ |$$ |__$$ |$$ |_____      $$ \__/  |$$ |_____ $$ \__$$ |$$ \__$$ |$$ |__$$ |        $$ |      $$ |  $$ |$$ |_____ $$ |_____ 
$$ |  $$ |$$    $$/ $$    $$/ $$    $$/ $$       |     $$    $$/ $$       |$$    $$/ $$    $$/ $$    $$/         $$ |      $$ |  $$ |$$       |$$       |
$$/   $$/ $$$$$$$/   $$$$$$/  $$$$$$$/  $$$$$$$$/       $$$$$$/  $$$$$$$$/  $$$$$$/   $$$$$$/  $$$$$$$/          $$/       $$/   $$/ $$$$$$$$/ $$$$$$$$/ 
                                                                                                                                                         
                                                                                                                                                         
                                                                                                                                                         ''')
print('Adobe-Cloud-Free')
print('Powered by some.js')
print('https://somejs.site')
print('https://github.com/somebodyscript/adobe-cloud-free/')
print('Available drivers: Chrome, Edge, Firefox')
selected_driver = input("Please write driver browser: ")
if selected_driver.lower() not in ["chrome", "edge", "firefox"]:
    print("Invalid driver. Exiting...")
    exit()
print('----------------------------')
print('Waiting version - a number that the user specifies, in general, the code will wait {specified number} seconds for the next action, but some actions remain unchanged even with the waiting version.')
print('If you have a weak Internet connection or device, it is recommended to set the standby version for at least 15 seconds.')
speed_version = input("Speed version: ")

def generate_random_password(length=10):
    letters = string.ascii_letters
    digits = string.digits

    has_digit = False
    while not has_digit:
        password_list = [random.choice(letters + digits) for _ in range(length)]
        has_digit = any(char.isdigit() for char in password_list)

    password = ''.join(password_list)
    return password

def generate_random_name():
    male_names = ["john", "mark", "max", "elon", "alex", "liam", "luke", "david", "jack", "noah", "michael", "william", "donald", "paul", "brian", "george", "charles"]
    female_names = ["emma", "anna", "jane", "kate", "mia", "sophia", "olivia", "grace", "lily", "ella", "mary", "linda", "lisa", "ava", "natalie", "chloe"]

    if random.choice([True, False]):
        name = random.choice(male_names)
    else:
        name = random.choice(female_names)

    additional_char = random.choice(string.ascii_lowercase)

    return additional_char.upper() + name

def write_credentials_to_file(filename, login, password, mode='a'):
    current_date = datetime.now().strftime("%Y%m%d")
    with open(filename, mode) as file:
        file.write(f"Date: {current_date}\n")
        file.write(f"Login: {login}\n")
        file.write(f"Password: {password}\n")
        file.write("\n")

if selected_driver.lower() == "chrome":
    driver = webdriver.Chrome()
elif selected_driver.lower() == "edge":
    driver = webdriver.Edge()
elif selected_driver.lower() == "firefox":
    driver = webdriver.Firefox()
else:
    print("Invalid driver selected. Exiting...")
    exit()

try:
    wait_time = int(speed_version)
except ValueError:
    print("Invalid speed version. Exiting...")
    driver.quit()
    exit()

try:
    print("< Information about setup >")
    print("> Speed version - {speed_version} seconds".format(speed_version=speed_version))
    print("> Selected driver - {selected_driver}".format(selected_driver=selected_driver))
    print("-----------------------------")
    print("> Opening hi2.in...")
    driver.get("https://hi2.in/")
    print("> Waiting for temp mail...")
    time.sleep(wait_time)
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.tooltiptextfix.text[readonly]')))
    temporary_email_input = driver.find_element(By.CSS_SELECTOR, 'input.tooltiptextfix.text[readonly]')
    temporary_email = temporary_email_input.get_attribute('value')
    print(f"Temporary email: {temporary_email}")

    driver.execute_script("window.open('https://account.adobe.com/register', 'new_window')")
    driver.switch_to.window(driver.window_handles[1])

    create_account_button = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-id="EmailPage-CreateAccountLink"]'))
    )
    create_account_button.click()

    time.sleep(1)

    email_input = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="Signup-EmailField"]'))
    )
    email_input.send_keys(temporary_email)

    time.sleep(1)

    random_password = generate_random_password()

    password_input = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="Signup-PasswordField"]'))
    )
    password_input.send_keys(random_password)

    time.sleep(1)

    next_button = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]'))
    )
    next_button.click()

    time.sleep(1)

    first_name = generate_random_name()
    last_name = generate_random_name()

    WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="Signup-FirstNameField"]')))
    first_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-id="Signup-FirstNameField"]')
    first_name_input.send_keys(first_name)

    time.sleep(1)

    last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-id="Signup-LastNameField"]')
    last_name_input.send_keys(last_name)

    time.sleep(1)

    WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="Signup-DateOfBirthChooser-Year"]')))
    year_input = driver.find_element(By.CSS_SELECTOR, 'input[data-id="Signup-DateOfBirthChooser-Year"]')
    year_input.clear()
    year_input.send_keys(random.randint(2007, 2010))

    if selected_driver.lower() == "firefox":
        create_account_button = driver.find_element(By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]')
        create_account_button.click()

        time.sleep(2)
        create_account_button = driver.find_element(By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]')
        create_account_button.click()
    else:
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]')))
        create_account_button = driver.find_element(By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]')
        create_account_button.click()

    print("> Please resolve the captcha.")
    input("Press Enter when you're done...")
    print("Ok, thanks, proceeding to the next step ^^")

    time.sleep(wait_time)
    WebDriverWait(driver, wait_time).until(EC.url_matches("https://account.adobe.com/"))

    if driver.current_url == "https://account.adobe.com/" or "https://account.adobe.com/#register" in driver.current_url:
        print("Account created. Proceeding to the next step...")
        time.sleep(3)
        driver.get("https://account.adobe.com/profile")
        WebDriverWait(driver, wait_time).until(EC.url_matches("https://account.adobe.com/"))
        time.sleep(1)
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
        cookie_reject = driver.find_element(By.ID, "onetrust-reject-all-handler")
        cookie_reject.click()
        print("> Cookies rejected. Proceeding to the next step...")
        time.sleep(4)
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.WBgRPa_spectrum-Link')))
        send_verification_email_button = driver.find_element(By.CSS_SELECTOR, 'span.WBgRPa_spectrum-Link')
        driver.execute_script("arguments[0].click();", send_verification_email_button)
        print("> Email sent. Proceeding to the next step...")
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[0]) 
        new_email_element = WebDriverWait(driver, 600).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="content"]/div'))
        )
        print("> Email received. Proceeding to the next step...")

        email_text = new_email_element.text

        urls = re.findall(r'(https?://\S+)', email_text)

        adobe_url = next((url for url in urls if url.startswith("https://adobeid.services.adobe.com/ims/verify/v2/")), None)

        if adobe_url:
            base_url = "https://adobeid.services.adobe.com/ims/verify/v2/"
            path = adobe_url[len(base_url):]

            transformed_path = path.upper()

            transformed_url = base_url + transformed_path

            print(f"Received URL: {transformed_url}")

            driver.get(transformed_url)

            time.sleep(3)

            press_continue_button = WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="PP-EmailVerificationWithLink-ContinueBtn"]'))
            )
            press_continue_button.click()

            time.sleep(wait_time)

            current_date = datetime.now().strftime("%Y%m%d")
            filename = f"{current_date}.txt"
            write_credentials_to_file(filename, temporary_email, random_password)
            print(f"Login: {temporary_email}")
            print(f"Password: {random_password}")
    else:
        print("Captcha failed or waiting time is out. Please try again.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()
