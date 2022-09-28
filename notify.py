import fetch
import psycopg2
from psycopg2 import Error


def CreateNotification(notification):

    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="yiutwxdz",
                                    password="2LuL55EjQeO_mzqIEGooGZ10GHvWQeL5",
                                    host="jelani.db.elephantsql.com",
                                    database="yiutwxdz")

        # Create a cursor to perform database operations
        cursor = connection.cursor()


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    user = fetch.get_UserById(id=notification["user_id"])
    print(user)

    notif = None
    sql = ('''INSERT INTO notifications (title, body, user_id, entity, entity_id)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
            ''')

    if user:
        try:
            notif = cursor.execute(sql,
            (notification["title"],  
            notification["body"], notification["user_id"], 
            notification["entity"], notification["entity_id"],))

            notification_id = cursor.fetchone()[0]
            print("notification Id::",notification_id)

            connection.commit()
            cursor.close()
            connection.close()
            return notif
            
        except Exception as err:
            print("encountered error writing to db::",err)
            return {"error": err}

    return notif
