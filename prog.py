# The author of this program is not responsible for the action of his/her users
# This program is for eduaction purpose only
import colorama # Colori LGBT 
import pyfiglet # sono un gran figo
import os  #Questo qua serve per cancellare le cose scritter prima 
import requests

dadda=1
Password=(input("Enter the password:   "))   #Vabbe sono "stra privato"
if(Password == "1"):  # <----------per chi non ha capito questa e' la password
    os.system("cls" if os.name == "nt" else "clear")
else:
    print("ur wrong")
    exit()

colorama.init()
print(colorama.Fore.RED + "")
print(pyfiglet.figlet_format("Moon.hf", font = "bloody"))    #Vabbe sono un figo
print(colorama.Fore.WHITE + "")
def menu():
    print("[1] Crush a server ")
    print("[2] Russian osint telegram bot ")
    print("[3] How to access with a ds token")
    print("[4] IP locator")
    print("[5] Dadda gay")
    print("[0] Exit from here ")

menu()
option = int(input("what you gonna do?   "))

while option != 0:
    if option == 1:
        #vabbe qua ci sta il discord / here is the discord bot link
        os.system("cls" if os.name == "nt" else "clear")
        print (colorama.Fore.RED + "https://discord.gg/syncord")
        pass
    elif option == 2:
        # vero hacker / here is the telegram bot
        os.system("cls" if os.name == "nt" else "clear")
        print (colorama.Fore.RED + "Telegram ID @MoonHfOsintBot")
    elif option == 3: # Sito fatto male / real quick site 
        os.system("cls" if os.name == "nt" else "clear")
        print(colorama.Fore.RED + "https://sites.google.com/view/tutortologinbymoonhf/home")
    elif option == 4:   # gay locator / find someone with his/her IP
        os.system('clear' if os.name == 'posix' else 'cls')


        print(colorama.Fore.RED + "#" * 60)
        ip_to_check = input('Insert\'IP for reveal :  ')
        print(f"U are revealing the : {ip_to_check}")
        print('-' * 60)

        # Richiesta all'API per ottenere informazioni sull'IP / just API request
        try:
            response = requests.get(f'https://ipinfo.io/{ip_to_check}/json')
            data = response.json()

            # Visualizza le informazioni / find info
            city = data.get('city', 'Non disponibile')
            region = data.get('region', 'Non disponibile')
            country = data.get('country', 'Non disponibile')
            location = data.get('loc', 'Non disponibile')

            print(colorama.Fore.GREEN + f"City: {city}")
            print(colorama.Fore.GREEN + f"Region: {region}")
            print(colorama.Fore.GREEN + f"country: {country}")
            print(colorama.Fore.GREEN + f"Position: {location}")
        except Exception as e:
            print(colorama.Fore.RED + "Smth wrong here ! ")
        
        print('' + 60 * ' ')
        input("Just press any key ")
        os.system('clear' if os.name == 'posix' else 'cls')

    elif option == 5:
        os.system('clear' if os.name == 'posix' else 'cls')
        while True:
            print("dadda gay")

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("What are you pressing ? ")
    print(colorama.Fore.WHITE + "")
    menu()
    option = int(input("What do wanna do? "))

colorama.init()
print(colorama.Fore.RED + "")
print(pyfiglet.figlet_format("Moon.hf", font = "bloody"))  # SONO UN FIGO x2
print(colorama.Fore.WHITE + "")

print("thx for using my stuff")
