import mariadb
import os
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    try:
        voipswitch = mariadb.connect(
            user=os.getenv('user'),
            password=os.getenv('passwd'),
            host=os.getenv('host'),
            port=3306,
            database=os.getenv('database')
        )

        print('Database connected')
        return voipswitch
    except mariadb.Error as e:
        print('An error happed: ' + str(e))
        return None


connect_db()
