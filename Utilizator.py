from CreateID import createID
id=createID()

class utilizator(createID):

    def __init__(self,nume,prenume,companie,idManager):
        self.utilizator={'ID':id.createID(),
                         'Nume':nume,
                         'Prenume':prenume,
                         'Companie':companie,
                         'IDManager':idManager}

    def __str__(self):
        return f'Angajatul cu id-ul {self.utilizator['ID']} se numeste {self.utilizator['Nume']} {self.utilizator['Prenume']} si lucreaza la compania {self.utilizator['Companie']} sub managerul cu id-ul {self.utilizator['IDManager']}.'
    