import pandas as pd
import sqlite3


csv = "buddymove_holidayiq.csv"
df = pd.read_csv(csv)
con = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('review', con)


###This is what i would write in sql, thanks for coming to my ted talk
Count_rows = """
    SELECT COUNT (*) 
    """

user_review = 
