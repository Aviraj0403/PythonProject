import cx_Oracle
con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('172.16.130.104','1521'))
c=con.cursor()
insert_statement = "INSERT INTO registration (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
c.execute('select * from registration')
for column in c:
    print(column[0]," ",column[1]," ",column[2])
c.close()    
con.close()