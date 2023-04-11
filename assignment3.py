from sqlalchemy import create_engine, text
import pandas as pd
import pymysql
import cryptography

sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1')
dbConnection = sqlEngine.connect()
vgsales = text("SELECT * FROM data1202.vgsales")
frame = pd.read_sql(vgsales, con = dbConnection)
pd.set_option('display.expand_frame_repr', False)
frame.loc[(frame['Year'] > 2005), "ERA"] = "post-2005"
frame.loc[(frame['Year'] < 2005), "ERA"] = "pre-2005"
frame.loc[(frame['Year'] == 2005), "ERA"] = "in-2005"
new_df = frame[['Global_Sales', 'ERA']]
x = new_df.loc[new_df["ERA"] != "in-2005"].groupby(["ERA"]).mean()
print(x)
