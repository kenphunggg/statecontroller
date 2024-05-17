import mysql.connector
from dotenv import load_dotenv
import os
import sys

load_dotenv()


print("Hello World I'm Ken 1")
#Connect to mysql


def printAll():
  cnx = mysql.connector.connect(
    user = 'kenphung', 
    password = 'PQThai29112003', 
    # host = f'{os.getenv("USER_IP")}',
    host = 'localhost',
    database = 'randomNumberDB', 
    port = '3306'
    )
  cursor = cnx.cursor()
  cursor.execute(f"SELECT randomNumber FROM randomNumberTable;")
  found = cursor.fetchall()
  for x in found:
    print (x)
  cursor.close()
  cnx.close()
  print(found)

def insert(x):
  cnx = mysql.connector.connect(
      user = 'kenphung', 
      password = 'PQThai29112003', 
      host = f'{os.getenv("USER_IP")}',
    #   host = 'localhost',
      database = 'randomNumberDB',
      port = '3306'
      )
  cursor = cnx.cursor()
  action = "INSERT INTO randomNumberTable (randomNumber) VALUES (%s);"
  cursor.execute(action, (x,))
  cnx.commit()
  cursor.close()
  cnx.close()

if __name__ == "__main__":
  function_name = sys.argv[1]

  if function_name == "printAll":
    printAll()
  elif function_name == "insert":
    x = sys.argv[2]
    insert(x)