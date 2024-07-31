from Conn_MySQL import Con_MySQL
con=Con_MySQL('utilizatori')

class InregistrareUtilizator():

    def __init__(self,utilizator):
        self.utilizator=utilizator

    def inregistrez_utilizator(self):
        return con.insert(self.utilizator)