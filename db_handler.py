from mysql import connector

class DbHandler:
    def __init__(self, host, user, password, database):
        super().__init__()
        self.__assignment_db = connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.__cursor = self.__assignment_db.cursor()

    def add_assignment(self, query):
        self.__cursor.execute("INSERT INTO assignment (assignment_name, class_name, turn_in_date, author, guild) VALUES" +
            f"('{query['assignment_name']}', '{query['class_name']}', '{query['turn_in_date']}', '{query['author']}', '{query['guild']}');"
        )
        self.__assignment_db.commit()
