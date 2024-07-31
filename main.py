from Inregistrare import InregistrareUtilizator
from Utilizator import utilizator
from date import *
import random

def importa_n_angajati(n):
    for i in range(n):
        numeAngajat=nume[random.randint(0,len(nume)-1)]
        prenumeAngajat=prenume[random.randint(0,len(prenume)-1)]
        idManagerAngajat=idManageri[random.randint(0,len(idManageri)-1)]
        importa_angajat(numeAngajat,prenumeAngajat,compania,idManagerAngajat)

def importa_angajat(numeAngajat,prenumeAngajat,compania,idManagerAngajat):
    angajat=utilizator(numeAngajat,prenumeAngajat,compania,idManagerAngajat)
    inregistrare=InregistrareUtilizator(angajat.utilizator)
    inregistrare.inregistrez_utilizator()