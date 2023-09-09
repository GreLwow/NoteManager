import sqlite3, datetime

class DatabaseHandler:
    """
        Класс для работы с базой данных
    """
    def __init__(self, db_file: str):
        """
            Подключение базы данных.

            :param db_file: Путь до файла .db.
            :type db_file: str
        """

        self.db_file = db_file
        self.connection = None
        self.connect()

    def connect(self) -> None:
        
        """
            Функция connect создает подключение к базе данных.

            :return: None
        """

        try:
            self.connection = sqlite3.connect(self.db_file, check_same_thread=False)
        except sqlite3.Error as e:
            print(f'ERROR: {e}')

    def disconnect(self) -> None:
        """
            Функция disconnect закрывает подключение к базе данных.

            :return: None
        """

        if self.connection:
            self.connection.close()

    def is_note_exits(self, title: str, note: str) -> bool:
        """
            Функция is_note_exits проверяет есть ли идентичная заметка в базе данных.

            :param title: Название заметки.
            :type title: str
            :param note: Заметка.
            :type note: str
            :return: True - если заметка найдена / False - если заметка не найдена.
            :rtype: bool
        """

        sql: str = '''SELECT * FROM notes WHERE title = ? AND note = ?'''
        params: tuple = (title, note)

        cur: sqlite3.Cursor = self.connection.cursor()
        cur.execute(sql, params)
        self.connection.commit()

        rows: list = cur.fetchall()

        return len(rows) > 0

    def create_note(self, title: str, note: str) -> int:
        """
            Функция create_note создает в базе данных заметку.

            :param title: Название заметки.
            :type title: str
            :param note: Заметка.
            :type note: str
            :return: Возвращает ID заметки в базе данных.
            :rtype: int
        """

        current_date: datetime.datetime = datetime.datetime.now()

        sql: str = ''' INSERT INTO notes(title, note, date)
                  VALUES(?,?, ?) '''
        params: tuple = (title, note, current_date)

        cur: sqlite3.Cursor = self.connection.cursor()
        cur.execute(sql, params)
        self.connection.commit()

        return cur.lastrowid
    
    
    def notes_list(self) -> list:
        """
            Функция notes_list выводит список заметок.

            :return: Список заметок.
            :rtype: list
        """

        sql: str = '''SELECT * FROM notes'''

        cur: sqlite3.Cursor = self.connection.cursor()
        cur.execute(sql)
        self.connection.commit()

        return cur.fetchall()
    
    def get_note(self, title: str, date: datetime.datetime) -> str:
        """
            Функция get_note Выводит строку с информацией заметки.

            :param title: Название заметки.
            :type title: str
            :param date: Дата.
            :type title: datetime
            :return: Возвращает строку с информацией заметки.
            :rtype: str
        """

        sql: str = '''SELECT * FROM notes WHERE title = ? AND date = ?'''
        params: tuple = (title, date)

        cur: sqlite3.Cursor = self.connection.cursor()
        cur.execute(sql, params)
        self.connection.commit()

        return cur.fetchone()

    def get_note_from_id(self, id_note: int) -> str:
        """
            Функция get_note_from_id выводит строку с информацией заметки по ID.

            :param id_note: ID заметки.
            :type id_note: int
            :return: Выводит строку с информацией по ID.
            :rtype: str
        """

        sql: str = '''SELECT * FROM notes WHERE id = ?'''

        cur: sqlite3.Cursor = self.connection.cursor()
        cur.execute(sql, (id_note,))
        self.connection.commit()

        return cur.fetchone()
    
    def delete_note(self, id_note: int) -> None:
        """
            Функция delete_note удаляет заметку.

            :param id_note: ID заметки.
            :type id_note: int
            :rtype: None
        """
        sql = '''DELETE FROM notes WHERE id = ?'''
        cur: sqlite3.Cursor = self.connection.cursor()
        cur.execute(sql, (id_note,))

        return self.connection.commit()

    def __del__(self):
        """
        Destructor to ensure the database connection is closed when the object is deleted.

        :return: None
        """

        self.disconnect()