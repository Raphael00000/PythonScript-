SwitchPortMaxNumber = 4

############# NETWORK Class ################
class Network:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.networkDevices = []
        
    def displayNetwork(self):
        print("\n/--- Network Devices ---/")
        for i in range (len(self.networkDevices)):
            print(self.networkDevices[i])

    def selectDevice(self, idDevice, typeDevice):
        for i in range (len(self.networkDevices)):
            if self.networkDevices[i].id == idDevice and self.networkDevices[i].type:
                return self.networkDevices[i]
            else:
                print("Error")

############# DEVICE Class ################
class Device:
    def __init__(self, id, type, name, macAdress):
        self.id = id
        self.type = type
        self.name = name
        self.macAdress = macAdress

    def __str__(self):
        return f"{self.id}_{self.type} - {self.name} ({self.macAdress})"  
    
############# COMPUTER Class ################
class Computer(Device):
    def __init__(self, id, type, name, macAdress, operatingSystem):
        super().__init__(id, type, name, macAdress)
        self.operatingSystem = operatingSystem
    
    def __str__(self):
        return f"{self.id}_{self.type} - {self.name} ({self.macAdress}) - {self.operatingSystem}" 
    
############# ROUTER Class ################
class Router(Device):
    def __init__(self, id, type, name, macAdress, ipAdress):
        super().__init__(id, type, name, macAdress)
        self.ipAdress = ipAdress

    def __str__(self):
        return f"{self.id}_{self.type} - {self.name} ({self.macAdress}) - {self.ipAdress}"

############# Switch Class ################
class Switch(Device):
    def __init__(self, id, type, name, macAdress, ipAdress):
        super().__init__(id, type, name, macAdress)
        self.ipAdress = ipAdress
        self.ipTable = []
    
    def __str__(self):
        return f"{self.id}_{self.type} - {self.name} ({self.macAdress}) - {self.ipAdress}"
    
    def displayIpTable(self):
        print("Switch Ip Table:",self)
        if len(self.ipTable) == 0 :
            print(" -- Empty -- ")
        else :
            print("Switch - IP Table - ",self.name)
            for i in range (len(self.ipTable)):
                print(self.ipTable[i])

    def addDevice (self, device):
        if len(self.ipTable)<SwitchPortMaxNumber:
            self.ipTable.append(device)
        else:
            print("\nError, you can't connect this device.\nIp table full")

############### Dictionnary ##############
class dictionnary:
    def __init__(self, nom, type_composant, annee, nombre_max_connections):
        self.nom = nom
        self.type_composant = type_composant
        self.annee = annee
        self.nombre_max_connections = nombre_max_connections

    def to_dict(self):
        return {
            "nom": self.nom,
            "type_composant": self.type_composant,
            "annee": self.annee,
            "nombre_max_connections": self.nombre_max_connections
        }