import random
import re
from ClassFile import *


def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )

def is_valid_ip_address(ip_address):
    chunks = ip_address.split(".")
    if len(chunks) != 4:
        return False
    for chunk in chunks:
        if not chunk.isdigit() or not 0 <= int(chunk) <= 255:
            return False
    return True



##########################      MAIN      #################################

def main():  
    composants_dict = {
    "composant1": dictionnary("Device", "Hardware", 2010, 1).to_dict(),
    "composant2": dictionnary("Router", "Hardware", 2015, 3).to_dict(),
    "composant3": dictionnary("Switch", "Hardware", 2012, SwitchPortMaxNumber).to_dict(),
    "composant4": dictionnary("Printer", "Hardware", 2018, 1).to_dict()
}
    network1 = Network(0, "Local Network")
    network1.networkDevices.append(Device(0, "Device", "Printer", rand_mac()))
    network1.networkDevices.append(Computer(1, "Computer", "RaphaComputer", rand_mac(), "Kali"))
    network1.networkDevices.append(Router(2, "Router", "Router1", rand_mac(), "10.10.10.10"))
    network1.networkDevices.append(Switch(3, "Switch", "Switch1", rand_mac(), "10.10.10.20"))
    network1.networkDevices[3].addDevice(network1.networkDevices[0].macAdress) #Adding macAdress to Ip table of the existing switch
    network1.networkDevices[3].addDevice(network1.networkDevices[1].macAdress)
    network1.networkDevices[3].addDevice(network1.networkDevices[2].macAdress)


    condition = True
    id = 4
    while (condition == True):
        print("\n\n0./Stop\n1./ Create a new device\n2./ Display network\n3./ Link a Device to a Switch\n4./ Display Ip table\n5./ Display component information")
        choice = input('-Enter your choice:')
        match choice:

            case '0': #Stop the loop
                condition = False
                print("\nThe program has stopped...")

            case '1': #Create a new Device
                print(" 1-Device / 2-Computer / 3-Switch / 4-Router")
                while True:
                    try:
                        choice = input('-Enter your choice:')
                        break
                    except ValueError:
                        print("Enter a valid number")

                match choice:
                    case '1': #Device
                        type = input(' -Type of device:')
                        name = input(' -Device name:')
                        network1.networkDevices.append(Device(id, type, name, rand_mac()))
                        id = id+1
                    case '2': #Computer 
                        name = input(' -Device name:')
                        operatingSystem = input(' -Operating System:')
                        network1.networkDevices.append(Computer(id, "Computer", name, rand_mac(), operatingSystem))
                        id = id+1                    
                    case '3':#Switch
                        name = input(' -Device name:')
                        ipAdress = input(' -Ip Address:')
                        if is_valid_ip_address(ipAdress) == True:
                            network1.networkDevices.append(Switch(id, "Switch", name, rand_mac(), ipAdress))
                            id = id+1
                        else :
                            print("Invalid IP Address")
                    case '4': #Router
                        name = input(' -Device name:')
                        ipAdress = input(' -Ip Address:')
                        if is_valid_ip_address(ipAdress) == True:
                            network1.networkDevices.append(Router(id, "Router", name, rand_mac(), ipAdress))
                            id = id+1
                        else :
                            print("Invalid IP Address")

            case '2': #Display the array Network
                network1.displayNetwork()

            case '3': #Link a device to a switch
                while True:
                    try:
                        switchId = int(input('Choose a switch (id)'))
                        deviceNb = int(input('Choose a device to connect (id)'))
                        break
                    except ValueError:
                        print("Enter a valid number")

                if switchId < id and deviceNb < id and network1.networkDevices[switchId].type == "Switch":
                    if network1.networkDevices[deviceNb].macAdress in network1.networkDevices[switchId].ipTable or network1.networkDevices[deviceNb].id == network1.networkDevices[switchId].id:
                        print("\nThe device already exist in the IP table")
                    else:
                        #network1.networkDevices[switchId].ipTable.append(network1.networkDevices[deviceNb].macAdress)
                        network1.networkDevices[switchId].addDevice(network1.networkDevices[deviceNb].macAdress)
                else :
                    print('\nError - Please select a Switch')

            case '4': #Display Ip table
                while True:
                    try:
                        switchId = int(input('Choose a switch (id)'))
                        break
                    except ValueError:
                        print("Enter a valid number")

                if switchId < id and network1.networkDevices[switchId].id == switchId and network1.networkDevices[switchId].type == "Switch":
                    if len(network1.networkDevices[switchId].ipTable) == 0:
                        print("\nEmpty Ip Table")
                    else:
                        for i in range (len(network1.networkDevices[switchId].ipTable)):
                            print("\nPort ", i ," - macAdress: ", network1.networkDevices[switchId].ipTable[i])
                else :
                    print('\nError - Please select a Switch')

            case '5':
                for nom, infos in composants_dict.items():
                    print("-" * 10)
                    print(f"Name: {infos['nom']}")
                    print(f"Type: {infos['type_composant']}")
                    print(f"Year: {infos['annee']}")
                    print(f"Max number of connection: {infos['nombre_max_connections']}")
                print("-" * 10)




if __name__ == "__main__":
    main()