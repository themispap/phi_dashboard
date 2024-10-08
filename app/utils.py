import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def execute_query(query_file, start_date, end_date, acad_year, values=()):
    # Read the SQL query from the file
    with open(query_file, 'r') as file:
        query = file.read()
    
    # Replace placeholders in the query
    query = query.format(acad_year="'"+acad_year+"'",start_date=start_date,end_date=end_date)
    # Remove newline characters (\n) and unnecessary whitespaces
    query = ' '.join(query.split())

    # Create a local database connection using credentials from .env
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    
    DATABASE_URL = f'postgresql://{username}:{password}@localhost:5432/{database}'
    engine = create_engine(DATABASE_URL)

    # Execute the query and return a DataFrame
    with engine.connect() as connection:
        result = connection.execute(text(query), values)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    return df
