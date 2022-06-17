import re
import time
import warnings
import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Path should be adjusted if your drivers appropriate location.
PATH = 'C:\Program Files (x86)\chromedriver.exe'
warnings.filterwarnings('ignore')


#########################################################
# ENTER THE APP NAME BETWEEN "" BEFORE RUNNING
app_name = "roblox"
num_of_calls = 150 # Number of times the JS function to 
# return more reviews is called. Default of 150, provides
# about 3,400 to 3,800 rows of data.
# Adjust accordingly to scrape more/less data.
# Scraper will take up to 10 minutes to gather such data
# With default number of calls.
#########################################################




# url to google playstore games page
url = 'https://play.google.com/store/games'

# Windowless mode feature (Chrome) and error message handling.
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')


# Initialization of web driver
driver = webdriver.Chrome(PATH, options=options)
driver.get(url)


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
    search_icon = driver.find_element_by_class_name("google-material-icons.r9optf")
    search_icon.click()
    # Enter game name into search bar and hits enter
    search_box = driver.find_element_by_class_name("HWAcU")
    search_box.clear() # Clear search box
    enter_game_name = search_box.send_keys(app_name.lower())
    time.sleep(1)
    search_box.send_keys(Keys.ENTER) # Clicks enter for search box
    time.sleep(2)
    # Hits tab key 3 times to shift to game link
    # Then clicks on link to get to main page
    search_box.send_keys(Keys.TAB*3, Keys.ENTER)
    open_all_reviews()


def open_all_reviews():
    """This function navigates to the 'See all reviews link and clicks it'"""
    time.sleep(3)
    # Searches for all buttons
    # Then clicks on the second to the last one
    # button[-2] == See all reviews
    buttons = driver.find_elements_by_tag_name("button")
    buttons[-2].click()
    # Locates the close reviews button
    review_scroll = driver.find_element_by_class_name("VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.DiOXab.a8Z62d")
    # Just some friendly user message
    print("Fetching data, hang in there....")
    # For loop to scroll down and trigger the JS Function to feed app reviews data
    time.sleep(2)
    for i in tqdm(range(num_of_calls)):
        review_scroll.send_keys(Keys.TAB, Keys.END*2)
        time.sleep(0.01)
    collect_reviews()


def collect_reviews():
    """
    This function gatheres all the data and stores them inside a dictionary
    """
    time.sleep(1)
    # Just some friendly user message
    print("Currently organizing data....")
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
        
    # Creates dictionary and adds list of reviews and ratings
    app_reviews_ratings["reviews"] = reviews_list
    app_reviews_ratings["ratings"] = ratings_list
    save_review_dataframe()


def save_review_dataframe():
    """
    Saves dataframe in CSV format file.
    """
    # Just some friendly user message
    print("Storing data, almost done....")
    reviews_ratings_df = pd.DataFrame(app_reviews_ratings)
    reviews_ratings_df = reviews_ratings_df.iloc[1: ,]
    time.sleep(1)
    save_to = f"{app_name.title()}_reviews.csv"
    reviews_ratings_df.to_csv(save_to, index=False)
    driver.quit() # Closes driver window and ends driver session
    print(f"Data saved as {app_name.title()}_reviews.csv in current directory.")


navigate_app()