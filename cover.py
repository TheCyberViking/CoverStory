from fng_api import *
import os

# this tool will generate a full cover idea

def clear():
    os.system('cls' if os.name=='nt' else 'clear')



def covergen():
    clear()
    print("Before Cover Made we have a few Questions")
    print("")
    print("Set Age for you want, close to real for best, 100 is the max")
    ageset = input("Set Age: ")
    print("What Country set as lower case | au | ca | gr | it | fr | sp | za | tn | uk | us | cyen | cygk | pl")
    countryset = input("Set Country: ")
    print("Set a Namestyle by country set as lower case | us | ar | cs | ch | en | gr | it | gd | ru | pl | hu")
    nameset = input("Set NameType: ")
    print("Set Gender Male or Female for now, set as lower case | male | female")
    genderset0 = input("Set Gender: ")
    if genderset0 == "male":
        genderset = "100"
    else:
        genderset = "0"
    identity = getIdentity(nameset=[nameset], country=[countryset], gender=genderset)
    textfile = (identity.name)
    f = open(f'{textfile}.txt', 'w+')
    f.write("NAME AND SSN\n")
    f.write(identity.name)
    f.write("\n")
    f.write(identity.ssn)
    f.write("\n")
    f.write("\n")
    f.write("JOB\n")
    f.write(identity.occupation)
    f.write("\n")
    f.write(identity.company)
    f.write("\n")
    f.write("\n")
    f.write("AGE AND BIRTH INFO\n")
    f.write(ageset)
    f.write("\n")
    f.write("Birth Day\n")
    f.write(identity.birthdayDay)
    f.write("\n")
    f.write("Birth Month\n")
    f.write(identity.birthdayMonth)
    f.write("\n")
    f.write("Zodiac Symbol\n")
    f.write(identity.zodiac)
    f.write("\n")
    f.write("Mother Maiden Name\n")
    f.write(identity.motherMaidenName)
    f.write("\n")
    f.write("\n")
    f.write("ADDRESS\n")
    f.write(identity.street)
    f.write("\n")
    f.write(identity.city)
    f.write("\n")
    f.write(identity.state)
    f.write("\n")
    f.write(identity.zip)
    f.write("\n")
    f.write("\n")
    f.write("VEHICLE\n")
    f.write(identity.color)
    f.write("\n")
    f.write(identity.vehicle)
    f.write("\n")
    f.write("\n")
    f.write("Phone\n")
    f.write(identity.phone)
    f.write("\n")
    f.write("Country Code\n")
    f.write(identity.countryCode)
    f.write("\n")
    f.write("\n")
    f.write("ONLINE\n")
    f.write(identity.email)
    f.write("\n")
    f.write("username\n")
    f.write(identity.username)
    f.write("\n")
    f.write("Password\n")
    f.write(identity.password)
    f.write("\n")
    f.write("\n")
    f.write("FINANCE\n")
    f.write(identity.card)
    f.write("\n")
    f.write(identity.expiration)
    f.write("\n")
    f.write(identity.cvv2)
    f.write("\n")
    f.write("\n")
    f.write("TRACKING NUMBERS\n")
    f.write("UPS\n")
    f.write(identity.ups)
    f.write("\n")
    f.write("WESTERUNION\n")
    f.write(identity.westernunion)
    f.write("\n")
    f.write("MONEYGRAM\n")
    f.write(identity.moneygram)
    f.close()

    print("you new Cover ID is called: ",textfile," This can be found in this folder")



def menu():
    clear()
    ans = True
    while ans:
        print("")
        print("#######################################################")
        print("#     CoverStory Generator By @TheCyberViking         #")
        print("#######################################################")
        print("This will Generator a Full Cover Story for you")
        print("This will generate a text file will all the details")
        print("")
        print("""
        1. Generate a Cover
        99. Exit/Quit
        """)
        print("")
        ans = input("Choose and Option from the List: ")
        if ans == "1":
            covergen()
        elif ans == "99":
            print("\n Closing Program Now")
            clear()
            sys.exit()
        else:
            print("!!! please choose a vaild menu option, now exiting !!!")
            menu()

# Working Code Bellow
menu()
