from operator import index
import os

app = 'call of dudes'
USER = os.getlogin()
FULL_PATH = fr"C:\Users\{USER}\Downloads\{app.title()}.csv"

# completeName = os.path.join(save_path, file_name)



var = "hey man, I am goodddd!!!"


# path = 
# with open(r"C:\Users\samsung\Downloads\rands.csv", 'w') as file:
#     file.write(var)


import pandas as pd


df = pd.DataFrame(
    {
    'a':[1,2,3,4,5],
    'b':[5,4,3,2,1]
   }
)


df.to_csv(FULL_PATH, index=False)
