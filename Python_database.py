import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="Rosh@n2001",database="movierecord")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE Movies_List(Name VARCHAR(30),Actor VARCHAR(30),Actress VARCHAR(30),Director VARCHAR(30),Year_of_release INT NOT NULL,PRIMARY KEY(Name))")
sql = "INSERT INTO Movies_List (Name, Actor, Actress,Director,Year_of_release) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('Detachment','Adrien Brody','Marcia Gay Harden','Tony Kaye',2011),
  ('October Sky','Jake Gyllenhaal','Laura Dern','Joe Johnston',1999),
  ('INTERSTELLAR','Matthew McConaughey','Anne Hathaway','Christopher Nolan',2014),
  ('The Faults in Our Stars','Ansel Elgort','Shailene Woodley','Josh Boone',2014),
  ('Serenity','Matthew McConaughey','Anne Hathaway','Steven Knight',2019),
  ('Spider-Man','Tobey Maguire','Kirsten Dunst','Sam Raimi',2002),
  ('The Wedding Planner','Matthew McConaughey','Jennifer Lopez','Adam Shankman',2001),
  ('The Jacket','Adrien Brody','Keira Knightley','John Maybury',2005)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Contents inserted.")
mycursor.execute(" SELECT * FROM Movies_List")
for i in mycursor:
    print(i)
mycursor.execute("SELECT Name,Actor FROM Movies_List ORDER BY Actor")
for j in mycursor:
    print(j)
mydb.close()
