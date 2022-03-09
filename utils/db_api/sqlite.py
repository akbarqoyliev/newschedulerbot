from datetime import date, time, timezone
import sqlite3

from data.weekdays import days

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            name varchar(255) NOT NULL,
            timezone varchar(50),
            email varchar(255),
            language varchar(5),
            PRIMARY KEY (id)
            );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, timezone: str = 'GMT+5', email: str = None, language: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"
        sql = """
        INSERT INTO Users(id, name, timezone, email, language) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, timezone, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_timezone(self, timezone, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE Users SET timezone=? WHERE id=?
        """
        return self.execute(sql, parameters=(timezone, id), commit=True)

    def update_language(self, language, id):
        sql = f"""
        UPDATE Users SET language=? WHERE id=?
        """
        return self.execute(sql, parameters=(language, id), commit=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


    ## Hafta kunlari uchun jadvallxar yaratish
    def create_tables_weekdays(self):
        for day in days:
            sql = f"""
            CREATE TABLE {day} (
                user_id int NOT NULL,
                table_id varchar(255) NOT NULL,
                table_name varchar(255) NOT NULL,
                situation varchar(20) NOT NULL,
                warning_time varchar(255),
                text varchar(4000)
                );
            """
            self.execute(sql, commit=True)

    def add_schedule(self, user_id: int, table_id: str, table_name: str, situation: bool = False, warning_time: time = None, text: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"
        for day in days:
            sql = f"""
            INSERT INTO {day} (user_id, table_id, table_name, situation, warning_time, text) VALUES(?, ?, ?, ?, ?, ?)
            """
            self.execute(sql, parameters=(user_id, table_id, table_name, situation, warning_time, text), commit=True)

    def select_schedule(self, day, **kwargs):
        sql = f"SELECT * FROM {day.title()} WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_schedule(self):
        return self.execute("SELECT COUNT(*) FROM Monday;", fetchone=True)

    def update_table_name(self, table_name: str, table_id: str):
        for day in days:
            sql = f"""
            UPDATE {day.title()} SET table_name=? WHERE table_id=?
            """
            return self.execute(sql, parameters=(table_name, table_id), commit=True)

    def update_situation(self, day, situation: bool, table_id: str):
        sql = f"""
        UPDATE {day.title()} SET situation=? WHERE table_id=?
        """
        return self.execute(sql, parameters=(situation, table_id), commit=True)

    def update_warning_time(self, day, warning_time: list, table_id: str):
        sql = f"""
        UPDATE {day.title()} SET warning_time=? WHERE table_id=?
        """
        return self.execute(sql, parameters=(warning_time, table_id), commit=True)

    def update_text(self, day, text: str, table_id: str):
        sql = f"""
        UPDATE {day.title()} SET text=? WHERE table_id=?
        """
        return self.execute(sql, parameters=(text, table_id), commit=True)

    def delete_schedule(self, table_id: str):
        for day in days:
            sql = f"""
            DELETE FROM {day.title()} WHERE table_id=?
            """
            return self.execute(sql, parameters=(table_id,), commit=True)

    def delete_tables_weekdays(self):
        for day in days:
            self.execute(f"DELETE FROM {day.title()} WHERE TRUE", commit=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
