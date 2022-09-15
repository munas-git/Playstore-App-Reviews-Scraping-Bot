print("                              -***-")
app_name = input("Enter name of app: ")
calls_amount = input("Enter number of calls: ")


def data_collection(app_name, calls_amount) ->tuple:
    
    try:
        calls_amount = int(calls_amount)
        # Condition to check if app name is not empty and calls_amount is an integer between 100 and 700
        if app_name.strip() != "" and isinstance(calls_amount, int) == True and 100 <= calls_amount <=700:
            return(app_name, calls_amount)
        else:
            data_collection()
    except ValueError:
        print("Enter a valid number of calls NB: Integer between 100 and 700")
        data_collection()
    return(app_name, calls_amount)


info = data_collection()
name = info[0]
print(name)