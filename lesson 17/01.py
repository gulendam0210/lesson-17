dukan = {"alma" : {"bahasy" : 15 , "mukdary" : 30} ,
        "mandarin" : {"bahasy" : 30 ,"mukdary" : 10},
        "kivi" : {"bahasy" :  18 , "mukdary" : 1},
        "banan" : {"bahasy" : 27 , "mukdary" : 20},
        "nar" : {"bahasy" : 18 , "mukdary" : 15}
         }

sum = 0 
while True:
    print("*** DUKAN DOLANDYRYSHY ***\n1. Haryt gorkezdirijilerini gor\n2. Haryt satyn al\n3. Harytlary gosh\n4. Harytlaryn bahasyny uytget\n5. Harytlary ayyr\n6. Mukdary artdyr\n7. Kassany gor") 
    isleg = input("Name etmeli? (san giriz): ")
    if isleg == "1":
        for fruit,details in dukan.items():
            print(f"{fruit.capitalize()}: bahasy: {details['bahasy']} manat, mukdary: {details['mukdary']} kg")
    if isleg == "2":
        name_aljak = input("Name satyn aljak? ")
        if name_aljak in dukan:
            agram = float(input(f"Nace kg {name_aljak} almak isleyarsiniz? "))
            if agram > dukan[name_aljak]["mukdary"]:
                print("Onca mukdar yok!")
            else:
                a = agram * dukan[name_aljak]['bahasy']
                b = dukan[name_aljak]['mukdary'] - agram
                dukan[name_aljak]['mukdary'] = b 
                sum += a
                print(f"{name_aljak} - y satyn aldynyz! {a} manat tolediniz")
    if isleg == "3":
        haryt_gosh = input("Taze haryt ady girizin")
        haryt_baha = int(input(f"{haryt_gosh} - yn bahasy: "))
        haryt_mukdar = int(input(f"Nace kg {haryt_gosh}y goshmaly?"))
        kg = float(input("Nace almak isleyarsiniz?: "))
        print(f"{haryt_gosh}y goshuldy.")
    if isleg == "4":
        baha_uytget = input("Haysy harydyn bahasyny uytgetmeli?")
        taze_baha = int(input(f"{baha_uytget}yn taze bahasy: "))
        dukan[baha_uytget]['bahasy'] = taze_baha
    if isleg == "5":
        haryt_ayyr = input("Haysy harydy ayyrmaly?")
        dukan.pop(haryt_ayyr)
        print(f"{haryt_ayyr} dukandan ayyryldy")
    if isleg == "6":
        haryt_mukdar_artdyr = input("Haysy haryt mukdar artdyrmaly") 
        if haryt_mukdar_artdyr in dukan:
            mukdar_gosh = float(input(f"nache kg goshmaly ? (onki mukdary : {dukan[haryt_mukdar_artdyr]['mukdary']})"))
            c = dukan[haryt_mukdar_artdyr]['mukdary'] + mukdar_gosh
            dukan[haryt_mukdar_artdyr]['mukdary'] = c
            print(f"{haryt_mukdar_artdyr}-yn mukdary tazelendi")
    if isleg == "7":
        print(f"Kassadaky jemlenen pul {sum} manat")
    if isleg == "quit":
        break