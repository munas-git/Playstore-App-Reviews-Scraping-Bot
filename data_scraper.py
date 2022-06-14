import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd
PATH = 'C:\Program Files (x86)\chromedriver.exe'
import warnings
warnings.filterwarnings('ignore')


##############################################
# ENTER THE APP NAME BETWEEN "" BEFORE RUNNING 
app_name = "stick war legacy"
##############################################




# url to google playstore games page
url = 'https://play.google.com/store/games'

# Initialization of web driver
driver = webdriver.Chrome(PATH)
driver.get(url)


reviews_list = []
ratings_list = []
app_reviews_ratings = {}


def navigate_app():
    """
    Function finds and clears the search box, enters the name of the app
    hits the enter button the navigates to the app page.
    """
    # Finds the search icon by ID and clicks on it
    search_icon = driver.find_element_by_class_name("google-material-icons.r9optf")
    search_icon.click()
    # Enter game name into search bar and hits enter
    search_box = driver.find_element_by_class_name("HWAcU")
    search_box.clear() # Clear search box
    enter_game_name = search_box.send_keys(app_name)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER) # Clicks enter for search box
    time.sleep(2)
    # Hits tab key 3 times to shift to game link
    # Then clicks on link to get to main page
    search_box.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)
    open_all_reviews()


def open_all_reviews():
    """This function navigates to the 'See all reviews link and clicks it'"""
    time.sleep(3)
    # Searches for all buttons
    # Then clicks on the second to the last one
    # button[-2] == See all reviews
    buttons = driver.find_elements_by_tag_name("button")
    buttons[-2].click()
    collect_reviews()


def collect_reviews():
    """
    This function gatheres all the data and stores them inside a dictionary
    """
    time.sleep(1)

    reviews = driver.find_elements_by_class_name("h3YV2d") # Locates reviews
    star_ratings = driver.find_elements_by_class_name("iXRFPc") # Locates ratings
    time.sleep(1)
    for (review,rating) in zip(reviews, star_ratings):
        review = review.text # Extracts test from the reviews
        star_rating = rating.get_attribute("aria-label") # Extracts the strings from "aria-label" attribute
        star_rating = re.findall("\d", star_rating) # Extracts the integer rating as list
        star_rating = star_rating[0] # Removes rating from list

        reviews_list.append(review) # adds each review to reviews list
        ratings_list.append(star_rating) # adds each rating to ratings list
        
    time.sleep(1)
    # Creates dictionary and add list values of reviews and ratings
    app_reviews_ratings["reviews"] = reviews_list
    app_reviews_ratings["ratings"] = ratings_list
    save_review_dataframe()


def save_review_dataframe():
    """
    Saves dataframe in CSV format file.
    """
    reviews_ratings_df = pd.DataFrame(app_reviews_ratings)
    reviews_ratings_df = reviews_ratings_df.iloc[1: ,]
    time.sleep(1)
    save_to = f"{app_name}.csv"
    reviews_ratings_df.to_csv(save_to, index=False)
    print(f"Data saved as {app_name}'.csv' in current directory")


navigate_app()