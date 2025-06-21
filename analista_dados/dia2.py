# prompt: https://economia.awesomeapi.com.br/json/last/BTC-BRL
# escreva um schedule que vai fazer a estração diaria dos dados e carregar em uma tabela sql no mysql
# essa e saida da API
# {"BTCBRL":{"code":"BTC","codein":"BRL","name":"Bitcoin/Real Brasileiro","high":"580838","low":"574937","varBid":"-59","pctChange":"-0.01","bid":"578115","ask":"578116","timestamp":"1750372310","create_date":"2025-06-19 19:31:50"}}

!pip install schedule requests mysql.connector

import schedule
import time
import requests
import mysql.connector
from datetime import datetime

# Replace with your MySQL database credentials
DB_CONFIG = {
    'user': 'root',
    'password': 'casaos',
    'host': '100.93.97.65',
    'database': 'cryptodb'
}

def create_connection():
    """Creates a connection to the MySQL database."""
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("MySQL database connection successful")
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
    return conn

def create_table(conn):
    """Creates the 'bitcoin_data' table if it doesn't exist."""
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bitcoin_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            code VARCHAR(10),
            codein VARCHAR(10),
            name VARCHAR(255),
            high DECIMAL(20, 2),
            low DECIMAL(20, 2),
            varBid DECIMAL(20, 2),
            pctChange DECIMAL(10, 2),
            bid DECIMAL(20, 2),
            ask DECIMAL(20, 2),
            timestamp VARCHAR(50),
            create_date DATETIME,
            ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
        print("Table 'bitcoin_data' checked/created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        cursor.close()

def insert_data(conn, data):
    """Inserts the extracted data into the 'bitcoin_data' table."""
    cursor = conn.cursor()
    sql = """
    INSERT INTO bitcoin_data (code, codein, name, high, low, varBid, pctChange, bid, ask, timestamp, create_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        # The API returns a nested JSON, we need to access the inner object
        btc_data = data.get("BTCBRL", {})
        if not btc_data:
            print("Warning: 'BTCBRL' key not found in API response")
            return

        values = (
            btc_data.get('code'),
            btc_data.get('codein'),
            btc_data.get('name'),
            btc_data.get('high'),
            btc_data.get('low'),
            btc_data.get('varBid'),
            btc_data.get('pctChange'),
            btc_data.get('bid'),
            btc_data.get('ask'),
            btc_data.get('timestamp'),
            btc_data.get('create_date')
        )
        cursor.execute(sql, values)
        conn.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    finally:
        cursor.close()

def extract_and_load():
    """Extracts data from the API and loads it into the database."""
    api_url = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"
    conn = None
    try:
        print(f"Attempting to fetch data from: {api_url}")
        response = requests.get(api_url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        print("Data fetched successfully")

        conn = create_connection()
        if conn:
            create_table(conn)
            insert_data(conn, data)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection closed")

# Schedule the job to run daily at a specific time (e.g., 10:00 AM)
schedule.every().day.at("10:00").do(extract_and_load)
print("Scheduler started. Job is scheduled to run daily at 10:00.")

# Keep the script running to execute the scheduled jobs
# In a Colab environment, this might run for a limited time depending on the runtime settings.
# For a persistent scheduler, you'd typically use a dedicated server or cloud function.
while True:
    schedule.run_pending()
    time.sleep(1)
