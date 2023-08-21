import os
import re
import warnings
import pandas as pd
from tqdm import tqdm
from validation import *
from colorama import Fore
from selenium import webdriver
from colorama import init as colorama_init
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
warnings.filterwarnings('ignore')
colorama_init()


########################################################################
WAIT_TIME = 4 # Default wait time(Seconds) before each bot action.
APP_NAME =  name # From validated input in validation.py
NUM_OF_CALL = calls # From validated input in validation.py
USER = os.getlogin() # Getting active user name.
FULL_PATH = fr"C:\Users\{USER}\Downloads\{APP_NAME.title()}_reviews.csv"
########################################################################


# url to google playstore games page
URL = 'https://play.google.com/store/games'

# Windowless mode feature (Chrome) and chrome message handling.
options = webdriver.ChromeOptions()
options.headless = True # Runs driver without opening a chrome browser.
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# Initialization of web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = options)
driver.get(URL)


reviews_list = []
ratings_list = []
app_reviews_ratings = {}


def navigate_app():
    """
    Function finds and clears the search box, enters the name of the app
    hits the enter button the navigates to the app page.
    """
    # Just some friendly user message
    print("Scraping data....")
    print("Exercise patience as this may take up to 10 minutes or more.")
    # Finds the search icon by ID and clicks on it
    search_icon = driver.find_element(by= By.CLASS_NAME, value="google-material-icons.r9optf")
    search_icon.click()
    # Enter app name into search bar and hits enter
    search_box = driver.find_element(by= By.CLASS_NAME, value="HWAcU")
    search_box.clear() # Clear search box
    # Deleted enter game name; enter_game_name = search_box.send_keys(app_name.lower())
    search_box.send_keys(APP_NAME.lower())
    time.sleep(WAIT_TIME)
    search_box.send_keys(Keys.ENTER) # Clicks enter for search box
    time.sleep(WAIT_TIME)
    # Hits tab key 3 times to shift to app link
    # Then clicks on link to get to app home page
    search_box.send_keys(Keys.TAB*3, Keys.ENTER)
    open_all_reviews()


def open_all_reviews():
    """This function navigates to the 'See all reviews' link and clicks it"""
    time.sleep(WAIT_TIME)
    # Searches for all buttons
    # Then clicks on the second to the last one
    # buttons[-2] == 'See all reviews'
    buttons = driver.find_elements(by= By.TAG_NAME, value="button")
    buttons[-2].click() # Clicks on 'See all reviews' link
    # Locates the close reviews button
    review_scroll = driver.find_element(by= By.CLASS_NAME, value="VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.a8Z62d")
    # Just some friendly user message
    print("Fetching data, hang in there....")
    # For loop to scroll down and trigger the JS Function to feed app reviews data
    time.sleep(WAIT_TIME)
    for i in tqdm(range(NUM_OF_CALL)):
        review_scroll.send_keys(Keys.TAB, Keys.END*2)
        # time.sleep(5) #### CHECK HERE INCASE.
    collect_reviews()


def collect_reviews():
    """
    This function gatheres all the data and stores them inside a dictionary
    """
    time.sleep(WAIT_TIME)
    # Just some friendly user message
    print("Currently organizing data....")
    time.sleep(1)
    print("This may take some time, based on the amount of data you're scraping.... hang in there a bit.")
    reviews = driver.find_elements(by= By.CLASS_NAME, value="h3YV2d") # Locates reviews
    star_ratings = driver.find_elements(by= By.CLASS_NAME, value="iXRFPc") # Locates ratings
    time.sleep(WAIT_TIME)
    for (review,rating) in zip(reviews, star_ratings):
        review = review.text # Extracts reviews
        star_rating = rating.get_attribute("aria-label") # Extracts the strings from "aria-label" attribute
        star_rating = re.findall("\d", star_rating) # Extracts the integer rating as list
        star_rating = star_rating[0] # Removes rating from list

        reviews_list.append(review) # adds each review to reviews list
        ratings_list.append(star_rating) # adds each rating to ratings list
        
    # Creates dictionary and adds list of reviews and ratings
    app_reviews_ratings["reviews"] = reviews_list
    app_reviews_ratings["ratings"] = ratings_list
    driver.quit() # Closes driver window and ends driver session
    save_review_dataframe()


def save_review_dataframe():
    """
    Saves dataframe in CSV file format.
    """
    # Just some friendly user message
    print("Storing data, almost done....")
    reviews_ratings_df = pd.DataFrame(app_reviews_ratings)
    reviews_ratings_df = reviews_ratings_df.iloc[1: ,]
    time.sleep(2)
    # Convert to CSV and save in Downloads.
    reviews_ratings_df.to_csv(FULL_PATH, index=False)
    data_rows = "{:,}".format(reviews_ratings_df.shape[0])
    print("\n"f"{Fore.LIGHTGREEN_EX}{data_rows} rows of data have been saved to downloadas as {APP_NAME.title()}_reviews.csv.")
    print("See you again next time ;-)")


if __name__ == "__main__":
    navigate_app()