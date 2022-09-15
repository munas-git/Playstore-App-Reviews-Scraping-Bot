import time


print("###################################################################################")
print("Welcome to Playstore App Reviews Data Scraper \n")
print("Things To Note")
print("- App name can not be empty and must appear as it does in playstore")
print("- Number of calls must be integer between 100 to 700, both inclusive.")
print("   **And finally, ensure you have steady network connection.**")
time.sleep(2)


def data_collection() ->tuple:
    try:
        print("                              -***-")
        app_name = input("Enter name of app: ")
        calls_amount = int(input("Enter number of calls: "))
        # Condition to check if app name is not empty and calls_amount is an integer between 100 and 700
        if app_name.strip() != "" and isinstance(calls_amount, int) == True and 100 <= calls_amount <=700:
            return(app_name, calls_amount)
        else:
            data_collection()
    except ValueError:
        print("Enter a valid number of calls NB: Integer between 100 and 700")
        data_collection()
        # return(app_name, calls_amount)
        # print("Except block")
        # print(app_name)
    return(app_name, calls_amount)
print("###################################################################################")


info = data_collection()
print(info[0])
print(info[1])