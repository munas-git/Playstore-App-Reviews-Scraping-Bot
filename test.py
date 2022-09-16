name = input("Enter name here: ")
calls = input("Enter calls here: ")


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
        calls = int(calls) # Tries to convert number of calls into integer.
        if name.strip() != "" and 100 <= calls <=700: # Checks if name and number meet requirement.
            return(name, calls)
        else:
            print("Ensure name field isn't empty and number of calls is between 100 and 700, both inclusive.")
            name = input("Enter app name here: ")
            calls = input("Enter number of calls here: ")
            info = data_collection(name, calls)
            name, calls = info[0], info[1]
            return(name, calls)
    except ValueError:
        print("You have entered an invalid literal for int(). Enter a valid number NB: Integer between 100 and 700")
        name_n = input("Enter app name here: ")
        calls_n = input("Enter number of calls here: ")
        info = data_collection(name_n, calls_n)
        name, calls = info[0], info[1]
        return(name, calls)


info = data_collection(name, calls)
name, calls = info[0], info[1]