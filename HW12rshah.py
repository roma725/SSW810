import sqlite3

DB_FILE='/Users/Class2018/Downloads/810_startup.db'

query='''select cwid, name, major from students where cwid=?'''
args=('10103',)

db=sqlite3.connect(DB_FILE)
rows=db.execture(query,args)

#convert the query results 
# into a list of dictionaries to pass to the template

data= [{'cwid': cwid, 'name': name, 'major': major}
       for cwid, name, major in rows]

db.close() #close the connection to close the database