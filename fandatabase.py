import sqlite3
import csv
mycurs = sqlite3.connect('fandatabase.db')  # connecting to database file
curs = mycurs.cursor()
############################--------MATCH TABLE---------###########################
curs.execute('''
CREATE TABLE match (player TEXT NOT NULL,
scored INTEGER,
faced INTEGER,
fours INTEGER,
sixes INTEGER,
bowled INTEGER,
maiden INTEGER,
given INTEGER,
wkts INTEGER,
catches INTEGER,
stumping INTEGER,
ro INTEGER);
''')
try:   #try block to catch exceptions
    with open('match.csv','rt') as f:  #iterating over csv file(match.csv) and each row at a time
        data=csv.reader(f) # csv reader
        for row in data:
            curs.execute("INSERT INTO match (player,scored, faced, fours,sixes,bowled,maiden,given,wkts,catches,stumping,ro) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", #adding data to database
                          (row[0],row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
            mycurs.commit()

    print("records added successfully match table.")
except:    # except block to handle exceptions
    print("Error in operation.")
    mycurs.rollback()
############################--------STATS TABLE---------###########################
curs.execute('''
CREATE TABLE stats (player PRIMARY KEY,
matches INTEGER,
runs INTEGER,
hundreds INTEGER,
fifties INTEGER,
value INTEGER,
ctg TEXT NOT NULL);
''')
try:   #try block to catch exceptions
    with open('stats.csv','rt') as f:  #iterating over csv file(stats.csv) and each row at a time
        data=csv.reader(f) # csv reader
        for row in data:
            curs.execute("INSERT INTO stats (player,matches,runs, hundreds, fifties,value,ctg) VALUES (?,?,?,?,?,?,?)", #adding data to database
                          (row[0],row[1], row[2], row[3],row[4],row[5],row[6]))
            mycurs.commit()

        print("records added successfully for stats table.")
except:    # except block to handle exceptions
    print("Error in operation.")
    mycurs.rollback()
############################--------TEAMS TABLE---------###########################
curs.execute('''
CREATE TABLE teams (name TEXT NOT NULL,
players TEXT NOT NULL,
value INTEGER);
''')


curs.close()