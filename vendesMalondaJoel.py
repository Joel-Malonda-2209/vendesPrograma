#Joel Malonda Beltran

noms = []
preus = []
qVenudes = []

continuar = True

while continuar:

    print("MENÚ")
    print("1. Introduir article nou: ")
    print("2. Fer una venda: ")
    print("3. Mostrar informació: ")
    print("4: Esborrar tots els articles: ")
    print("5: Eixir: ")
    print("")

    opcio = int(input("Dis-me quina opció vols: "))

    if opcio == 1:
        article = input("Dis-me un article que vuigues introduïr: ")
        noms.append(article)
        preu = float(input("Dis-me el preu: "))
        preus.append(preu)
        qVenudes.append(0)
        print("")
        print("L'article s'ha guardat")
        print("")

    elif opcio == 2:
        artVendre = input("Dis-me quin article vols vendre: ")
        vendes = int(input("Quantes unitats has venut?: "))
        for n in range (len(noms)):
            if noms[n] == artVendre:
                posicio = n
                acum = 0
                acum = qVenudes[posicio] + vendes
                qVenudes[posicio] = acum
                print("")
                print("Venta realitzada")
                print("")

    elif opcio == 3:
        print("NOM", "QUANT", "PREU", "IMPORT", sep="\t")
        print("------  -----   ------  -------")
        
        total = 0
        for i in range (len(noms)):
            posicio = i
            imp = qVenudes[posicio] * preus[posicio]
            print(f"{noms[posicio].ljust(6)[:6]}    {qVenudes[posicio]}      {preus[posicio]}     {imp}")
            print("")
            total = total + imp
        print("TOTAL: ", total)
        print("")
        
            
    elif opcio == 4:
        noms = []
        preus = []
        qVenudes = []
        print("")
        print("Articles esborrats")
        print("")

    elif opcio == 5:
        
        
        seguir = input("Vols finalitzar el programa? (s/S o n/N) ")
        if seguir == "s" or seguir == "S":
            continuar = False
            print("")
            print("Programa finalitzat")
            print("")
        elif seguir == "n" or seguir == "N":
            continuar = True
        else:
            print("")
            print("Necesite una resposta vàlida")
            print("")

        

    else:
        print("")
        print("Opció no vàlida")
        print("")
        

