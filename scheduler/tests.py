import mysql.connector
import config.settings as settings


database = settings.DATABASES["default"]
connection = mysql.connector.connect(
    user=database["USER"],
    host=database["HOST"],
    port=database["PORT"],
    password=database["PASSWORD"],
    database=database["NAME"],
)
sql = connection.cursor()
sql.execute("select email from accounts_user")

myresult = sql.fetchall()

for x in myresult:
    print(x)
