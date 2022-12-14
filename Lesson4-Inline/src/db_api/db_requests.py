import sqlite3


class Database:
    def __init__(self, db_path='shop_database.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users(
        id int NOT NULL,
        phone text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, phone: str = None):
        sql = 'INSERT INTO Users(id, phone) VALUES(?, ?)'
        parameters = (id, phone)
        self.execute(sql, parameters, commit=True)

    def select_user_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM Users WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_users(self) -> list:
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def update_user_phone(self, id: int, phone: str):
        sql = "UPDATE Users SET phone=? WHERE id=?"
        return self.execute(sql, parameters=(phone, id), commit=True)

    def delete_user(self, **kwargs):
        sql = "DELETE FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def delete_all(self):
        self.execute("DELETE FROM Users WHERE True", commit=True)

    def drop_all(self):
        self.execute("DROP TABLE Users", commit=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

        ### ?????????????? ?????? ?????????????? ?? ????????????????
    
    def create_table_items(self):
        sql = """
        CREATE TABLE Items(
        id int NOT NULL,
        name text,
        quantity int,
        photo_path text,
        PRIMARY KEY(id)
        );
        """
        self.execute(sql, commit=True)

    def add_item(self, id: int, name: str = None, quantity: int = 0, photo_path: str = ''):
        sql = 'INSERT INTO Items(id, name, quantity, photo_path) VALUES(?, ?, ?, ?)'
        parameters = (id, name, quantity, photo_path)
        self.execute(sql, parameters, commit=True)

    def select_item(self, **kwargs) -> list:
        sql = 'SELECT * FROM Items WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_items(self) -> list:
        sql = 'SELECT * FROM Items'
        return self.execute(sql, fetchall=True)
    
    def update_item_quantity(self, id: int, name: str, quantity: int = None):
        sql = 'UPDATE Items SET quantity=? WHERE id=?'
        return self.execute(sql, parameters=(quantity, id), commit=True)

    # def update_items_info(self, id: int, name: str, quantity: int = None):
    #     sql = 'UPDATE Items SET name=?, quantity=? WHERE id=?'
    #     return self.execute(sql, parameters=(name, quantity, id), commit=True)
    
    def get_items_count(self) -> int:
        sql = 'SELECT * FROM Items'
        return len(self.execute(sql, fetchall=True))
    
    def delete_item(self, **kwargs):
        sql = 'DELETE FROM Items WHERE '
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)
    
    def delete_all_items(self):
        self.execute('DELETE FROM Items WHERE True', commit=True)

    def drop_all_items(self):
        self.execute('DROP TABLE Items', commit=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += " AND ".join([f"{item} = ?" for item in parameters])
        return sql, tuple(parameters.values())

