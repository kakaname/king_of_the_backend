import importlib
import requests
from colorama import Fore, Style

name = "attacker_v1.py"
details = """
        Simple attack
        """
defender = "http://127.0.0.1:8000"




def start_attack():
    utilities = importlib.import_module("attacker.flask.utilities")
    utilities.print_details(name, details)

    x = requests.post(defender+"/ping_server").json()

    print(Fore.RED + "Attacker:", Style.RESET_ALL + x["message"], "\n")
        
    return False



if __name__ == "__main__":
    start_attack()