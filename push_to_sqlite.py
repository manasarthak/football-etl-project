# push_to_sqlite.py
import pandas as pd
from scrap_beautiful_soup import *  # Import your scraping functions
from sqlalchemy import create_engine

# List of functions to process and push to SQLite
functions = [
    league_table,
    top_scorers,
    detail_top,
    player_table,
    all_time_table,
    all_time_winner_club,
    top_scorers_seasons
]

# Create SQLite database connection
db_connection_string = 'sqlite:///football_data.db'  # Create a local SQLite database file
db = create_engine(db_connection_string)

# Loop through the functions and push data to the database
for fun in functions:
    function_name = fun.__name__  # Get the name of the current function
    result_df = fun()  # Call the function to get the DataFrame
    
    # Push the DataFrame to the SQLite database with the function name as the table name
    result_df.to_sql(function_name, con=db, if_exists='replace', index=False)
    print(f'Pushed data for {function_name} to SQLite.')

