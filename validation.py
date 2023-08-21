import time


print("###################################################################################")
print("Welcome to Playstore App Reviews Data Scraper \n")
print("Things To Note:")
print("- App name can not be empty and must appear as it does in playstore")
print("- Number of calls must be integer between 100 to 700, both inclusive.")
print("- Minimum number of calls (100) provides an average of 2,000 rows of data, adjust accordingly.")
print("   **And finally, ensure you have steady network connection.**")
time.sleep(2)


print("                              -***-")
name = input("Enter app name here: ")
calls = input("How many calls should be made?: ")


def data_collection(name:str, calls:int) ->tuple:
    """
    Function collects and validates user inputs.

    Input:
        name:str: Name of app whose data is to be scraped. App must be available on the app store and spelt correctly.

        calls:int: Integer value between 100 and 700 that determines amount of data that will be scraped.


    Output:
        (name, calls): Tuple containig validated app name and amount of calls.
    """

    try:
        print("                              -***-")
        calls = int(calls) # Tries to convert number of calls into integer.
        if name.strip() != "" and 100 <= calls <=700: # Checks if name and number meet requirement.
            return(name, calls)
        else:
            print("Ensure name field isn't empty and number of calls is between 100 and 700, both inclusive.")
            name = input("Enter app name here: ")
            calls = input("How many calls should be made calls?: ")
            info = data_collection(name, calls)
            name, calls = info[0], info[1]
            return(name, calls)
    except ValueError:
        print("You have entered an invalid literal for int(). Enter a valid number NB: Integer between 100 and 700")
        name_n = input("Enter app name here: ")
        calls_n = input("How many calls should be made calls?: ")
        info = data_collection(name_n, calls_n)
        name, calls = info[0], info[1]
        return(name, calls)


info = data_collection(name, calls)
name, calls = info[0], info[1]
print("###################################################################################")