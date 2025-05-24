ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"O ano {ano} é BISSEXTO.")
        else:
            print(f"O ano {ano} NÃO é bissexto.")
    else:
        print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO é bissexto.")