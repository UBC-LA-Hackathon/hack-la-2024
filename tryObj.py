from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import script
from script import Discussion
import time

# Set up your WebDriver (Chrome in this example)
driver_path = "chromedriver.exe"  # Ensure you have the correct path to your ChromeDriver
service = Service(driver_path)  # Create a Service object
options = Options()

def post_user1(user, driver):
    driver.get('https://objection.lol/courtroom/3792uz')
    driver.implicitly_wait(10)

    # Find and interact with the text input (example selector, modify as needed)
    # text_input = driver.find_element("id", "input-631")
    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[3]/div/div/form/div[2]/div/div/div/div/div[1]/div/input')

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.send_keys(user)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)
    submit_button = driver.find_element(By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > form > div.v-card__actions > button:nth-child(3) > span')
    submit_button.click()


def post_user2(user, driver):
    driver.get('https://objection.lol/courtroom/3792uz')
    driver.implicitly_wait(10)

    # Find and interact with the text input (example selector, modify as needed)
    # text_input = driver.find_element("id", "input-631")
    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[3]/div/div/form/div[2]/div/div/div/div/div[1]/div/input')

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.send_keys(user)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)
    submit_button = driver.find_element(By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > form > div.v-card__actions > button:nth-child(3) > span')
    submit_button.click()

    characterChoice = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[3]')
    characterChoice.click()
    driver.implicitly_wait(10)
    character = driver.find_element(By.CSS_SELECTOR, value='#app > div.v-dialog__content.v-dialog__content--active > div > div > div > div.d-flex.flex-wrap.mt-4 > div:nth-child(2)')
    character.click()


# Function to open an instance of objection.lol and post an argument
def post_argument(argument, driver):
    # driver.get('https://objection.lol/courtroom/3792uz')
    driver.implicitly_wait(30)

    # Find and interact with the text input (example selector, modify as needed)
    # text_input = driver.find_element("id", "input-631")
    text_input = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[2]/div/div[2]/textarea')
    text_input.click()

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.send_keys(argument)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)
    submit_button = driver.find_element(By.CSS_SELECTOR, '#app > div.v-application--wrap > div.container.pa-0.pa-lg-2.container--fluid > main > div > div > div.row.no-gutters > div:nth-child(1) > div > div:nth-child(4) > div:nth-child(2) > div > div > div:nth-child(2) > div > div.pl-1 > button')
    submit_button.click()


# Open two instances of Chrome with different options if needed
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()

# Post users and arguments from the course discussion
user1 = "phoenix"
user2 = "miles"

post_user1(user1, driver1)
post_user2(user2, driver2)

discussion = script.discussion_array[0]
for i in range(0, len(discussion.get_messages()) - 1):
    if i % 2 == 0:
        post_argument(discussion.get_messages()[i], driver1)    # Argument 1 posted in browser 1
    else:
        post_argument(discussion.get_messages()[i], driver2)     # Argument 2 posted in browser 2

    time.sleep(5)                                           # Adding delay for timing (adjust as needed)


# Add more interactions if necessary, or let the drivers stay open to watch the results

# To keep the browsers open:
time.sleep(300)  # Adjust the time to keep the browser open before closing

# Close the browser windows when done
driver1.quit()
driver2.quit()