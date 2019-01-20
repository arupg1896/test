from sqlalchemy import create_engine


# create engine
sql_engine = create_engine("mysql+pymysql://root:Srbc2011@@localhost:3306/testdb")

# connect engine to db
connection = sql_engine.connect()

# name ="Rani"
# owner ='Ram'
# species ='Spitch'
# sex ='male'
# birth = '2012-03-12'
# death = '2016-09-27'

# connection.execute( 'INSERT INTO pet VALUES ("Rani", "Ram", "Spitch", "m", "2012-03-12", "2016-09-27" )')

# connection.execute('DROP TABLE IF EXISTS Cars')
# connection.execute('CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name TEXT, Price INTEGER)')

# connection.execute( 'INSERT INTO Cars VALUES (1, "Audi", 5000 )')

# data = ({"Id": 2, "Name": "Skoda", "Price": 9000},
#         {"Id": 3, "Name": "Volvo", "Price": 29000},
#         {"Id": 4, "Name": "Bentley", "Price": 350000},
#         {"Id": 5, "Name": "Citroen", "Price": 21000},
#         {"Id": 6, "Name": "Hummer", "Price": 41400},
#         {"Id": 7, "Name": "Volkswagen", "Price": 21600}
#         )


# connection.execute( 'INSERT INTO Cars VALUES (1, "Audi", 5000 )')
connection.execute( 'INSERT INTO Cars VALUES (2, "Skoda", 9000 )')
connection.execute( 'INSERT INTO Cars VALUES (3, "Bentley", 29000 )')
connection.execute( 'INSERT INTO Cars VALUES (4, "Citron", 21000 )')
connection.execute( 'INSERT INTO Cars VALUES (5, "Hummer", 414000 )')
connection.execute( 'INSERT INTO Cars VALUES (6, "Volkswagen", 216000 )')



# for line in data:
#     connection.execute("INSERT INTO Cars(Id, Name, Price) VALUES(:Id, :Name, :Price)", line)

# execute query
# ret = connection.execute("SELECT name FROM pet WHERE ID = CONNECTION_ID()").fetchall()
# ret = connection.execute("SELECT name FROM pet").fetchall()

# display result
# print(ret)
