import sqlite3
import csv

db = sqlite3.connect('../data-warehouse.db')
cursor = db.cursor()

cursor.execute(
    '''
    DROP TABLE  IF EXISTS matches
    '''
)

cursor.execute(
     '''
    CREATE TABLE IF NOT EXISTS matches (
            [id] INTEGER PRIMARY KEY,
            [Match_Id] INTEGER,
            [Match_Date] TEXT,
            [Toss_Decide] INTEGER,
            [Win_Margin] INTEGER,
            [Season_Year] INTEGER,
            [Team_1] TEXT,
            [Team_2] TEXT,
            [Venue_Name] TEXT,
            [City_Name] TEXT,
            [Toss_Name] TEXT,
            [Win_Type] TEXT,
            [Outcome_Type] TEXT,
            [Match_Winner] TEXT,
            [Toss_Winner] TEXT,
            [Man_of_the_Match] TEXT,
            [Country_Name] TEXT
    )
    '''
)

cursor.execute(
    '''
    DROP TABLE  IF EXISTS ball_runs
    '''
)

cursor.execute(
     '''
    CREATE TABLE IF NOT EXISTS ball_runs (
            [id] INTEGER PRIMARY KEY,
            [Match_Id] INTEGER,
            [Striker] INTEGER,
            [Non_Striker] INTEGER,
            [Bowler] INTEGER,
            [Extra_Runs] INTEGER,
            [Over_Id] INTEGER,
            [Ball_Id] INTEGER,
            [Runs_Scored] INTEGER,
            [Innings_No] INTEGER,
            [Team_Batting] TEXT,
            [Team_Bowling] TEXT,
            [Extra_Name] TEXT
    )
    '''
)

cursor.execute(
    '''
    DROP TABLE  IF EXISTS ball_outs
    '''
)

cursor.execute(
     '''
    CREATE TABLE IF NOT EXISTS ball_outs (
            [id] INTEGER PRIMARY KEY,
            [Match_Id] INTEGER,
            [Over_Id] INTEGER,
            [Ball_Id] INTEGER,
            [Innings_No] INTEGER,
            [Team_Batting] TEXT,
            [Team_Bowling] TEXT,
            [Player_Out] TEXT,
            [Out_Id] INTEGER,
            [Out_Type] TEXT
    )
    '''
)

cursor.execute(
    '''
    DROP TABLE  IF EXISTS players
    '''
)

cursor.execute(
     '''
    CREATE TABLE IF NOT EXISTS players (
            [id] INTEGER PRIMARY KEY,
            [Player_Id] INTEGER,
            [Player_Name] TEXT,
            [DOB] TEXT,
            [Batting_hand] INTEGER,
            [Bowling_skill] INTEGER,
            [Country_Name] TEXT
    )
    '''
)

cursor.execute(
    '''
    DROP TABLE  IF EXISTS venues
    '''
)

cursor.execute(
     '''
    CREATE TABLE IF NOT EXISTS venues (
            [id] INTEGER PRIMARY KEY,
            [Venue_Id] INTEGER,
            [Venue_Name] TEXT,
            [City_Id] INTEGER,
            [City_Name] TEXT,
            [Country_Id] INTEGER,
            [Country_Name] TEXT
    )
    '''
)


# file = open('./Sample - Superstore.csv')
# contents = csv.reader(file)
# next(contents, None)

# insert_records = "INSERT INTO superstore (Row_ID, Order_ID, Order_Date, Ship_Date, Ship_Mode, Customer_ID, Customer_Name, Segment, Country, City, State, Postal_Code, Region, Product_ID, Category, Sub_Category, Product_Name, Sales, Quantity, Discount, Profit) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
# cursor.executemany(insert_records, contents)
