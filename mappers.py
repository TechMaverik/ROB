import sqlite3


class Mappers:

    def configuration_setup(self, ip):
        conn = sqlite3.connect("rob.db")
        cursor = conn.cursor()
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS configurations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,   
        )
        """
        )
        insert_query = "INSERT INTO configurations (id, ip) VALUES (?, ?)"
        ip_data = ip
        cursor.execute(insert_query, ip_data)
        conn.commit()

    def delete_configuration(self):
        conn = sqlite3.connect("rob.db")
        cursor = conn.cursor()
        delete_query = "DELETE FROM configurations"
        cursor.execute(delete_query)
        conn.commit()
        conn.close()

    def select_configuration(self):
        conn = sqlite3.connect("rob.db")
        cursor = conn.cursor()
        select_query = "SELECT * FROM configurations"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        conn.close()
        return rows
