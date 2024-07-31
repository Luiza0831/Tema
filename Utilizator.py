from CreateID import createID
from Conn_MySQL import Con_MySQL
con=Con_MySQL('utilizatori')

class utilizator(createID):

    def __init__(self,nume,prenume,companie,idManager):
        self.utilizator={'ID':createID().createID(),
                         'Nume':nume,
                         'Prenume':prenume,
                         'Companie':companie,
                         'IDManager':idManager}

    def __str__(self):
        return f'Angajatul cu id-ul {self.utilizator['ID']} se numeste {self.utilizator['Nume']} {self.utilizator['Prenume']} si lucreaza la compania {self.utilizator['Companie']} sub managerul cu id-ul {self.utilizator['IDManager']}.'
    
    def inregistrez_utilizator(self):
        return con.insert(self.utilizator)
    