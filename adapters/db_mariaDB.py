import mysql.connector
import os
import logging
from mysql.connector import Error
from dotenv import load_dotenv

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Załaduj zmienne z pliku .env
load_dotenv()

# Pobierz dane konfiguracyjne
DB_HOST = os.getenv("MARIA_DB_HOST")
DB_USER = os.getenv("MARIA_DB_USER")
DB_PASSWORD = os.getenv("MARIA_DB_PASSWORD")
DB_NAME = os.getenv("MARIA_DB_NAME")

# Walidacja zmiennych środowiskowych
if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
    logging.error("Brakuje jednej lub więcej zmiennych środowiskowych: MARIA_DB_HOST, MARIA_DB_USER, MARIA_DB_PASSWORD, MARIA_DB_NAME")
    raise EnvironmentError("Nie można załadować konfiguracji bazy danych.")

def connect_to_mariadb():
    """Nawiązuje połączenie z bazą danych MariaDB."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            logging.info("Połączono z bazą danych MariaDB")
            return connection
        return None
    except Error as e:
        logging.error(f"Błąd podczas łączenia z MariaDB: {e}")
        return None

def close_connection(connection):
    """Zamyka połączenie z bazą danych."""
    if connection and connection.is_connected():
        connection.close()
        logging.info("Połączenie z bazą danych zostało zamknięte")