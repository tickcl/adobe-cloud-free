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
print('Aviable drivers: Chrome, Edge, Firefox')
selected_driver = input("Please write driver browser: ")
if selected_driver not in ["Chrome", "Edge", "Firefox", "chrome", "edge", "firefox"]:
    print("Invalid driver. Exiting...")
    exit()

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
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for _ in range(5))
    return name

def write_credentials_to_file(filename, login, password, mode='a'):
    current_date = datetime.now().strftime("%Y%m%d")
    with open(filename, mode) as file:
        file.write(f"Date: {current_date}\n")
        file.write(f"Login: {login}\n")
        file.write(f"Password: {password}\n")
        file.write("\n")

if selected_driver == "Chrome" or selected_driver == "chrome":
    driver = webdriver.Chrome()

elif selected_driver == "Edge" or selected_driver == "edge":
    driver = webdriver.Edge()

elif selected_driver == "Firefox" or selected_driver == "firefox":
    driver = webdriver.Firefox()

try:
    driver.get("https://hi2.in/")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.tooltiptextfix.text[readonly]')))
    temporary_email_input = driver.find_element(By.CSS_SELECTOR, 'input.tooltiptextfix.text[readonly]')
    temporary_email = temporary_email_input.get_attribute('value')

    driver.execute_script("window.open('https://account.adobe.com/register', 'new_window')")
    driver.switch_to.window(driver.window_handles[1])

    create_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-id="EmailPage-CreateAccountLink"]'))
    )
    create_account_button.click()

    time.sleep(1)

    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="Signup-EmailField"]'))
    )
    email_input.send_keys(temporary_email)

    time.sleep(1)

    random_password = generate_random_password()

    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="Signup-PasswordField"]'))
    )
    password_input.send_keys(random_password)

    time.sleep(1)

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]'))
    )
    next_button.click()

    time.sleep(1)

    first_name = generate_random_name()
    last_name = generate_random_name()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="Signup-FirstNameField"]')))
    first_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-id="Signup-FirstNameField"]')
    first_name_input.send_keys(first_name)

    time.sleep(1)

    last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-id="Signup-LastNameField"]')
    last_name_input.send_keys(last_name)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Signup-DateOfBirthChooser-Month')))
    month_dropdown = driver.find_element(By.ID, 'Signup-DateOfBirthChooser-Month')
    month_dropdown.click()

    months = month_dropdown.find_elements(By.TAG_NAME, 'li')

    if months:
        random_month = random.choice(months)
        random_month.click()
    else:
        print(">< No months available for selection. It's not break algorithm, i think.")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="Signup-DateOfBirthChooser-Year"]')))
    year_input = driver.find_element(By.CSS_SELECTOR, 'input[data-id="Signup-DateOfBirthChooser-Year"]')
    year_input.clear()
    year_input.send_keys("2007")

    time.sleep(2)

    if selected_driver == "Firefox" or selected_driver == "firefox":
        create_account_button = driver.find_element(By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]')
        create_account_button.click()

        time.sleep(2)
        create_account_button = driver.find_element(By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]')
        create_account_button.click()
    else:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]')))
        create_account_button = driver.find_element(By.CSS_SELECTOR, 'button[data-id="Signup-CreateAccountBtn"]')
        create_account_button.click()

    print("> Please resolve the captcha.")
    input("Press Enter when you're done...")
    print("Ok, thanks, proceeding to next step ^^")

    time.sleep(6)
    WebDriverWait(driver, 15).until(EC.url_matches("https://account.adobe.com/"))

    if driver.current_url == "https://account.adobe.com/":
        print("Account created. Proceeding to next step...")
        time.sleep(3)
        driver.get("https://account.adobe.com/profile")
        WebDriverWait(driver, 10).until(EC.url_matches("https://account.adobe.com/"))
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
        cookie_reject = driver.find_element(By.ID, "onetrust-reject-all-handler")
        cookie_reject.click()
        print("> Cookies rejected. Proceeding to next step...")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.WBgRPa_spectrum-Link')))
        send_verification_email_button = driver.find_element(By.CSS_SELECTOR, 'span.WBgRPa_spectrum-Link')
        driver.execute_script("arguments[0].click();", send_verification_email_button)
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[0]) 
        new_email_element = WebDriverWait(driver, 600).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="content"]/div'))
        )
        print("> Email received. Proceeding to next step...")

        email_text = new_email_element.text

        urls = re.findall(r'(https?://\S+)', email_text)

        adobe_url = next((url for url in urls if url.startswith("https://adobeid.services.adobe.com/ims/verify/v2/ru_ru/")), None)

        if adobe_url:
            base_url = "https://adobeid.services.adobe.com/ims/verify/v2/ru_ru/"
            path = adobe_url[len(base_url):]

            transformed_path = path.upper()

            transformed_url = base_url + transformed_path

            print(f"Received URL: {transformed_url}")

            driver.get(transformed_url)

            time.sleep(3)

            press_continue_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="PP-EmailVerificationWithLink-ContinueBtn"]'))
            )
            press_continue_button.click()

            time.sleep(5.5)

            current_date = datetime.now().strftime("%Y%m%d")
            filename = f"{current_date}.txt"
            write_credentials_to_file(filename, temporary_email, random_password)
            print(f"Login: {temporary_email}")
            print(f"Password: {random_password}")
    else:
        print("Captcha failed. Please try again.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    driver.quit()

finally:
    driver.quit()
