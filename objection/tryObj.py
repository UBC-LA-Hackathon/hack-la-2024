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

def new_discussion_spectate(discussiontitle, driver):
    driver.get('https://objection.lol/courtroom')
    driver.implicitly_wait(10)

    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[1]/div[2]/main/div/div/form/div[1]/div[1]/div/div/div/div/input')
    text_input.send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
    text_input.send_keys(discussiontitle)

    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[1]/div[2]/main/div/div/form/div[2]/div[2]/div/div/div/div[1]/input')

    discussion_code = text_input.get_attribute('value')
    print(discussion_code)

    submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/main/div/div/form/div[4]/div/button')
    submit_button.click()

    spectate_button = driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[3]/div/div/form/div[3]/button[1]')
    spectate_button.click()

    return discussion_code
def post_user(user, disc_code, driver):
    driver.get('https://objection.lol/courtroom/' + disc_code)
    driver.implicitly_wait(10)

    # Find and interact with the text input (example selector, modify as needed)
    # text_input = driver.find_element("id", "input-631")
    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[3]/div/div/form/div[2]/div/div/div/div/div[1]/div/input')

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.send_keys(user1)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)
    submit_button = driver.find_element(By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > form > div.v-card__actions > button:nth-child(3) > span')
    submit_button.click()


# Function to open an instance of objection.lol and post an argument
def post_argument(argument, driver):
    # driver.get('https://objection.lol/courtroom/3792uz')
    # driver.implicitly_wait(10)

    # Find and interact with the text input (example selector, modify as needed)
    # text_input = driver.find_element("id", "input-631")
    text_input = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div/form/div[2]/div/div/div/div/div[1]/div/input')

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.send_keys(argument)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)
    submit_button = driver.find_element("class name", "v-btn__content")
    submit_button.click()


# Open two instances of Chrome with different options if needed
driver0 = webdriver.Chrome()

driver1 = webdriver.Chrome()
# driver2 = webdriver.Chrome(service=service, options=options)

# Post users and arguments from the course discussion
user1 = "phoenix"
user2 = "miles"
argument1 = "Your first argument here"
argument2 = "Your second argument here"
discussiontitle = "Goku vs The Sun"

disc_code = new_discussion_spectate(discussiontitle, driver0)
post_user(user1, disc_code, driver1)

post_argument(argument1, driver1)  # Argument 1 posted in browser 1
# time.sleep(20)  # Adding delay for timing (adjust as needed)
# post_argument(argument2, driver2)  # Argument 2 posted in browser 2

# Add more interactions if necessary, or let the drivers stay open to watch the results

# To keep the browsers open:
time.sleep(300)  # Adjust the time to keep the browser open before closing

# Close the browser windows when done
driver0.quit()

driver1.quit()
# driver2.quit()