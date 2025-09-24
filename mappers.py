import sqlite3


class Mappers:

    def __init__(self):
        self.conn = sqlite3.connect("rob.db")
        self.cursor = self.conn.cursor()
        self.create_config_table_query = """
        CREATE TABLE IF NOT EXISTS configurations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL
        )
        """
        self.create_rec_pos_table_query = """
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            base INTEGER NOT NULL, 
            shoulder INTEGER NOT NULL,    
            elbow INTEGER NOT NULL,  
            wrist INTEGER NOT NULL,  
            end_effector INTEGER NOT NULL,  
            pick INTEGER NOT NULL
        )
        """
        self.cursor.execute(self.create_config_table_query)
        self.conn.commit()
        self.cursor.execute(self.create_rec_pos_table_query)
        self.conn.commit()

    def add_configurations(self, ip):
        """Add configuration

        Args:
            ip (_type_): string
        """
        insert_query = "INSERT INTO configurations (ip) VALUES (?)"
        ip_data = ip
        self.cursor.execute(insert_query, ip_data)
        self.conn.commit()
        self.conn.close()

    def record_position(
        self,
        base: int,
        shoulder: int,
        elbow: int,
        wrist: int,
        end_effector: int,
        pick: int,
    ):
        """Record Position

        Args:
            base (int): Base Angle
            shoulder (int): Shoulder Angle
            elbow (int): Elbow Angle
            wrist (int): Wrist Angle
            end_effector (int): Wrist Yaw Angle
            pick (int): Pick Angle
        """

        insert_query = "INSERT INTO records (base,shoulder,elbow,wrist,end_effector,pick) VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(
            insert_query, (base, shoulder, elbow, wrist, end_effector, pick)
        )
        self.conn.commit()
        self.conn.close()

    def delete_configuration(self):
        """Delete Configurations"""
        delete_query = "DELETE FROM configurations"
        self.cursor.execute(delete_query)
        self.conn.commit()
        self.conn.close()

    def delete_record(self):
        """Delete Records"""
        delete_query = "DELETE FROM records"
        self.cursor.execute(delete_query)
        self.conn.commit()
        self.conn.close()

    def select_configuration(self):
        """Select Configurations"""
        select_query = "SELECT * FROM configurations"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        self.conn.close()
        return rows

    def select_record(self):
        """Select Records"""
        select_query = "SELECT * FROM records"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        self.conn.close()
        return rows
