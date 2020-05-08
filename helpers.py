from colorama import init, Fore

def display(message, is_warning=False):
    if is_warning == True:
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message)