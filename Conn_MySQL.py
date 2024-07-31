import mysql.connector

class Con_MySQL():

    def __init__(self,db):
        self.db=db
        self.mydb=mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='root',
                                          database=db)
        self.cursor=self.mydb.cursor()

    def select(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self,dict):
        query=f'INSERT INTO `{self.db}` VALUES('
        for key in dict:
            if type(dict[key])==int:
                query+=f"{dict[key]},"
            else:
                query+=f"'{dict[key]}',"
        query=query[:-1]
        query+=');'
        self.cursor.execute(query)
        self.mydb.commit()
        return 'Dictionarul atasat a fost inserat in baza de date!'
        
    def update(self):
        pass

    def delete(self):
        pass    