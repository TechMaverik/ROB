import sqlite3


class Mappers:

    def __init__(self):
        self.conn = sqlite3.connect("rob.db")
        self.cursor = self.conn.cursor()
        self.create_config_table_query="""
        CREATE TABLE IF NOT EXISTS configurations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL
        )
        """
        self.create_rec_pos_table_query="""
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
            

    def configuration_setup(self, ip):        
        insert_query = "INSERT INTO configurations (ip) VALUES (?)"
        ip_data = ip
        self.cursor.execute(insert_query, ip_data)
        self.conn.commit()
        self.conn.close()

    def record_position(self, base,shoulder,elbow,wrist,end_effector,pick):        
        insert_query = "INSERT INTO records (base,shoulder,elbow,wrist,end_effector,pick) VALUES (?, ?, ?, ?, ?, ?)"        
        self.cursor.execute(insert_query,  (base, shoulder, elbow, wrist, end_effector, pick))
        self.conn.commit()
        self.conn.close()

    def delete_configuration(self):        
        delete_query = "DELETE FROM configurations"
        self.cursor.execute(delete_query)
        self.conn.commit()
        self.conn.close()
    
    def delete_record(self):        
        delete_query = "DELETE FROM records"
        self.cursor.execute(delete_query)
        self.conn.commit()
        self.conn.close()

    def select_configuration(self):       
        select_query = "SELECT * FROM configurations"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        self.conn.close()
        return rows
    
    def select_record(self):       
        select_query = "SELECT * FROM records"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        self.conn.close()
        return rows
