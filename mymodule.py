import sqlite3
class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS sutdent(id INTEGER PRIMARY KEY,fname TEXT ,lname TEXT,email TEXT,password TEXT) ")
        self.con.commit()
    def insert_record(self,fname,lname,email,password):
        self.cur.execute("INSERT INTO sutdent(id,fname,lname,email,password ) VALUES (NULL,?,?,?,?)" ,(fname,lname,email,password))
        self.con.commit()
    def search_record(self,inp,inp1):
         self.cur.execute("SELECT * FROM  sutdent WHERE lower(email)=? or lower(password)=?",(inp,inp1))
         return self.cur.fetchall()
        



db=Database("h:/m/mydata1.db")  