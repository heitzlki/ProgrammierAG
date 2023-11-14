import os, sys



felder = ["1","2","3","4","5","6","7","8","9"]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

blau = '\033[96m'

class play_options:
    X = f"{bcolors.OKCYAN}X{bcolors.ENDC}"
    O = f"{bcolors.FAIL}O{bcolors.ENDC}"

def pruefe_feld(nummern):
    if (felder[nummern[0]] == play_options.X) and (felder[nummern[1]] == play_options.X) and (felder[nummern[2]] == play_options.X):
        return True, play_options.X
    elif (felder[nummern[0]] == play_options.O) and (felder[nummern[1]] == play_options.O) and (felder[nummern[2]] == play_options.O):
        return True, play_options.O
    else:
        return False, ""


def pruefe_sieg():
    pruef_felder = [[0,1,2], [3, 4, 5], [6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for pruef_feld in pruef_felder:
        sieg, sieger = pruefe_feld(pruef_feld)
        if (sieg):
            print(f"{sieger} hat gewonnen!")
            neue_runde = input("Möchtest du eine neue Runde spielen? [y/n]: ")
            if neue_runde == "y":
                starte_spiel()
            else: 
                sys.exit("Spiel beendet!")

def print_feld():
    print(f"{felder[0]}|{felder[1]}|{felder[2]}\n-----\n{felder[3]}|{felder[4]}|{felder[5]}\n-----\n{felder[6]}|{felder[7]}|{felder[8]}\n")
    pruefe_sieg()

def print_optionen():
    optionen_text=""
    for feld in felder:
        # print(repr(feld))
        # print(repr(play_options.X))
        # print(feld != play_options.X)
        if (feld != play_options.X) and (feld != play_options.O):
            optionen_text = optionen_text + " " + feld

    print(f"Verfügbare Felder: {optionen_text}")

def wahl(skip_x=False):
    if skip_x == False:
        print_optionen()
        x=input("x: ")
        try:
            if felder[int(x)-1] == play_options.X or felder[int(x)-1] == play_options.O:
                print_feld()
                wahl(False)
            else:
                felder[int(x)-1]=play_options.X
                print_feld()
        except:
            print_feld()
            print("Bitte nur Zahlen!")
            wahl(False)


            
    print_optionen()
    o=input("o: ")

    try:
        if felder[int(o)-1] == play_options.X or felder[int(o)-1] == play_options.O:
            print_feld()
            wahl(True)
        else:
            felder[int(o)-1]=play_options.O
            print_feld()
    except:
        print_feld()
        print("Bitte nur Zahlen!")
        wahl(True)
    
    
    wahl(False)

def starte_spiel():
    global feldercl
    os.system('clear')
    felder = ["1","2","3","4","5","6","7","8","9"]
    print_feld()
    wahl(False)


starte_spiel()
# if __name__ == "__main__":
#     starte_spiel()