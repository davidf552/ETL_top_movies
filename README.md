# ETL_top_movies
A client needs a movie dataset saved inside a database. Also, another client requires the budget information and box office earnings of the previous data. Finally, a third client wishes to see the information about the directors and actors involved in those movies.


## Introduction


The source code of this project is located [here.](ETL.py)

This project involves three databases:
 - [MySQL](#mysql-and-postgresql) for general storage.
 - [Postgresql](#mysql-and-postgresql) for movie financial data.
 - [MongoDB](#mongodb) for the movie cast.


There are also [Queries](#queries) made using the previous data.


## MySQL and PostgreSQL

First, the dataset is loaded inside a Panda dataframe for inspection. There are a couple of errors inside the data, so a transformation is needed before uploading the information to the databases.


![image](https://github.com/davidf552/ETL_top_movies/assets/103103116/c48bcf9f-b45b-4105-b7aa-fba1c64ea13f)


Once the data from before is adequate, it will be saved inside the designated databases.

PostgreSQL was chosen because it makes querying financial information a lot easier than a NoSQL database.


To make the connection, a username and password are required:


![image](https://github.com/davidf552/ETL_top_movies/assets/103103116/64b3189c-b3d8-492c-bbc2-a9f716f4e479)


In this project, the sql engine is used with these databases. It is a great tool that will make the process go more smoothly.


![image](https://github.com/davidf552/ETL_top_movies/assets/103103116/009bc188-1571-4c42-8412-7c52ed46f1fa)

[Return](#introduction)


## MongoDB


This database was chosen as the movie cast storage because MongoDB is great when there is a lot of text data. The sql engine is no longer needed with this database, just the Pymongo library. 


![image](https://github.com/davidf552/ETL_top_movies/assets/103103116/44aefb6b-5619-44ad-a3ad-13672bfd8bca)


A json file is needed to upload the data instead of using dataframes. For this reason, a conversion is necessary:


![image](https://github.com/davidf552/ETL_top_movies/assets/103103116/38ad9c9a-a87f-4429-ba8c-1db1f67045a6)


To upload the previous json file, the Pymongo library is used as shown here:


![image](https://github.com/davidf552/ETL_top_movies/assets/103103116/9498bda4-9706-4640-991c-4f79a888e6ef)

[Return](#introduction)


## Queries

A couple of queries were made to show how the data gets stored in the different databases:

**Top budget movie** 


![top_budget_movie](https://github.com/davidf552/ETL_top_movies/assets/103103116/7b934a35-cbe0-47e4-90cb-c6a091b45c40)


**Movie with most profits**


![top_gain_movie](https://github.com/davidf552/ETL_top_movies/assets/103103116/e93be8ac-fcd0-46a9-8b58-8538a55b80aa)


**Top 5 action movies**


![top_5_action](https://github.com/davidf552/ETL_top_movies/assets/103103116/9a828a4a-eaa2-459c-9921-5980a3b44634)


**Top 5 movies with good profit**


![top_5_profit](https://github.com/davidf552/ETL_top_movies/assets/103103116/4d9bb388-6dd9-42f8-abc3-d44780539a14)


**Film with ranking number 120**


![mongodb_rank120](https://github.com/davidf552/ETL_top_movies/assets/103103116/7624aa27-dfac-4775-babd-a0698602b807)


[Return](#introduction)
