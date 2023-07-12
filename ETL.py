import mysql.connector
import pandas as pd
import json
from sqlalchemy import create_engine
from pymongo import MongoClient
 
 
# Credentials to database connection
hostname="localhost"
dbname="movies"
uname=""
pwd=""

uname_post = ""

myclient = MongoClient("mongodb+srv://<user>:<password>@cluster0.3dssseg.mongodb.net/?retryWrites=true&w=majority")

# database
db = myclient["etl_project"]
  
# collection
Collection = db["movies"]

#Extract 
df = pd.read_csv("Movies.csv")
df = df.rename(columns = {'rank':'ranking'})

df = df.replace(to_replace = "Not Available", value = "0")
df['budget'] = df['budget'].str.replace('EM', '')
df['budget'] = df['budget'].str.replace('RF', '')
df['budget'] = df['budget'].str.replace('$', '',regex = True)

df['box_office'] = df['box_office'].str.replace(r'[(estimated)]', '',regex = True)

df['box_office'] = df['box_office'].str.strip()
df['budget'] = df['budget'].str.strip()

columns = ["rating","casts","directors","writers","certificate","run_time","tagline"]
columns_b = ["budget","box_office","certificate","run_time","tagline"]

df_budget = df
df_cast = df

df_budget = df_budget.drop(columns, axis = 1) #DO NOT FORGET TO INCLUDE AXIS
df_cast = df_cast.drop(columns_b, axis = 1)

df_budget.to_csv("Movies_income.csv", encoding = 'utf-8' , index = False)
df_cast.to_json("Movies_cast.json", orient = "records")

#Uploading to MySQL --- main storage
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

df.to_sql('movie', engine, index=False, if_exists = 'replace' )

engine.dispose()

#Uploading to PostgreSQL --- budget repository 
engine2 = create_engine("postgresql+psycopg2://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname_post, pw=pwd))

df_budget.to_sql('movie_budget', engine2, index=False, if_exists = 'replace')

engine2.dispose()

#Uploading to MongoDB Atlas --- director and actors repository


with open('Movies_cast.json') as file:
    file_data = json.load(file)


Collection.insert_many(file_data) 