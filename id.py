import sqlite3
con=sqlite3.connect('h:id.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS employs (id  INTEGER PRIMARY KEY  ,fname TEXT,lname TEXT, salary INTEGER)')
con.commit()


def insert_record(fname,lname,salary):
 cur.execute('INSERT INTO employs (id,fname,lname,salary) VALUES (NULL,?,?,?)',(fname,lname,salary))
 print(' record insert')
 con.commit()


def read_record():
  cur.execute('SELECT  fname,salary FROM  employs WHERE  salary<=5000 and fname="ali" ')
  cur.execute('SELECT  fname,salary FROM  employs WHERE  salary>=3000 and lname="maradi" ')
  record=cur.fetchall()
  return record
  
records=(read_record()) 
print('**************')

for record in records:
 # print(f'{record[0]}-\nfname={record[1]}-lname={record[2]}\t salary is {record[3]}')
  print(record)

#for i in range(5):
  #fname=input(" enter youer number ")
 # lname=input(" enter youer number ")
 # salary=int(input(" enter youer number "))
  #insert_record(fname,lname,salary)
 