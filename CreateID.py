import os
from date import *

class createID():

    def createID(self):
        if os.path.exists(path):
            with open(path,'r')as file:
                self.id=int(file.read())+1
        else:
            self.id=1
        with open(path,'w')as file:
            file.write(str(self.id))
        return self.id