from django.conf import settings
import MySQLdb
import time

host = settings.DATABASES['default']['HOST']
user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
port = int(settings.DATABASES['default']['PORT'])
db = settings.DATABASES['default']['NAME']

message = """
    ################################
    database connect:
    host = {}
    user = {}
    password = {}
    port = {}
    db = {}
    ################################
""".format(host, user, password, port, db)

print(message)

conn = None
tries = 0
while True:
    print(tries, host, user, password, port)
    tries += 1
    try:
        conn = MySQLdb.connect(
            host=host, user=user, passwd=password, port=port
        )
    except MySQLdb.Error as e:
        print("Waiting for mysql up: {}".format(e))
        time.sleep(10)
        continue

    while True:
        cursor = conn.cursor()
        cursor.execute("show databases like '{}'".format(db))
        result = cursor.fetchone()
        if result and len(result) > 0:
            print("Database '{}' is ready!").format(db)
            break
        else:
            print("Waiting for database creation to finish...")
            time.sleep(10)
        cursor.close()
    conn.close()
    break
