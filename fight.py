import sys
import importlib
from multiprocessing import Process


def start_fight(attack_v, defend_v):
    attacker = "attacker.flask.attacker_v" + attack_v
    defender = "defender.flask.defender_v" + defend_v
    attacker = importlib.import_module(attacker)
    defender = importlib.import_module(defender)


    p = Process(target=defender.start_defence) 
    p.start()
    
    print("hello world")
    if not attacker.start_attack():
        print("Attack failed")
    else:
        print("Attack Successful")

    p.kill()

    

    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("proper usage : python fight <attacker_version> <defender_version>")

    start_fight(sys.argv[1], sys.argv[2])
