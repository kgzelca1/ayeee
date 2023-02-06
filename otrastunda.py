import random 
from colorama import Fore, Back, Style
print(f"{Fore.CYAN}Teksts{Style.RESET_ALL}")
while True:
    vardi = ["viens", "divi", "trīs", "četri"]
    vards = random.choice(vardi)
    minetaisvards = list("_"for _ in vards)
    dzivibas = 5 

    print(vards)
    print("".join(minetaisvards))

    while dzivibas > 0 or not "".join(minetaisvards) == vards:
        inp = input(f"Ievade{len(vards)}:")
        if len(inp) != len(vards): continue
        #garuma pārbaude 

        minetaisvards = list("_" for _ in vards)
        for iii in range(0, len(vards)):
            if vards[iii] == inp[iii]:
                print(f"{Back.GREEN}{vards[iii]}{Style.RESET_ALL}," end="")
                minetaisvards[iii] = inp[iii]
            elif inp[iii] in vards:
                print(f"{Back.YELLOW}{vards[iii]}{Style.RESET_ALL}," end="")
            else:
                print(f"{inp{iii}}", end="")

        if uzminets == False:
            dzivibas -= 1


        print(f"Dzīvības: {dzivibas}:")
        print("".join(minetaisvards))
        


    if dzivibas == 0:
        print("tu zaudeji")
    else:
        print("tu uzvareji")

    if not input("Vai turpināt? Y/N") [0].lower() == "y":
        break   

