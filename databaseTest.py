
import mysql.connector

#open connection
db = mysql.connector.connect(host ="localhost", user="root", password="Not that easy m8", database="sense_data")
print(db)

mycursor = db.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)

commander = "INSERT INTO `data` (`TEMPERATURE`, `PRESSURE`, `HUMIDITY`, `TIMESTAMP`, `id`) VALUES ('111', '111', '111', '111', 3);"
mycursor.execute(commander)
db.commit()

