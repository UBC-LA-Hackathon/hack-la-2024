from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up your WebDriver (Chrome in this example)
driver_path = "./chromedriver.exe"  # Ensure you have the correct path to your ChromeDriver
service = Service(driver_path)  # Create a Service object
options = Options()


# Function to open an instance of objection.lol and post an argument
def post_argument(argument, driver):
    driver.get('https://objection.lol/courtroom/3792uz')
    time.sleep(5)

    # Find and interact with the text input (example selector, modify as needed)
    input_field = driver.find_element(By.XPATH, '//label[text()="Username"]/following-sibling::input')
    time.sleep(5)

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.input.send_keys("Chill")

    time.sleep(5)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)
    submit_button = driver.find_element("class name", "v-btn__content")
    submit_button.click()


# Open two instances of Chrome with different options if needed
driver1 = webdriver.Chrome(service=service, options=options)
# driver2 = webdriver.Chrome(service=service, options=options)

# Post arguments from the course discussion
argument1 = "Your first argument here"
argument2 = "Your second argument here"

post_argument(argument1, driver1)  # Argument 1 posted in browser 1
time.sleep(20)  # Adding delay for timing (adjust as needed)
# post_argument(argument2, driver2)  # Argument 2 posted in browser 2

# Add more interactions if necessary, or let the drivers stay open to watch the results

# To keep the browsers open:
time.sleep(300)  # Adjust the time to keep the browser open before closing

# Close the browser windows when done
driver1.quit()
# driver2.quit()