import ConnectingLibrary as Cl

# Przykład użycia
if __name__ == "__main__":
    conn = Cl.connect_to_mariadb()
    if conn:
        # Tutaj możesz wykonać zapytania do bazy danych
        Cl.close_connection(conn)
