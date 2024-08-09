tier_na_cislo = {
    "s": 6,
    "a": 5,
    "b": 4,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 0
}

cislo_na_tier = {
    6: "s",
    5: "a",
    4: "b",
    3: "c",
    2: "d",
    1: "e",
    0: "f"
}

tier_cisla = []

print("zadej tier S-F (X=exit):")
while True:
    tier_pismeno = input()
    if tier_pismeno.lower() == "x":
        prucis = sum(tier_cisla)/len(tier_cisla)
        pismeno = cislo_na_tier[round(prucis)]
        zbytek = prucis - round(prucis)
        print("výsledný tier je:")
        if prucis > round(prucis):
            print(pismeno.upper() + " +" + str(round(zbytek, 5)))
        elif prucis < round(prucis):
            print(pismeno.upper() + " " + str(round(zbytek, 5)))
        else:
            print(pismeno.upper())
        break
    elif tier_pismeno.lower() in tier_na_cislo:
        tier_cislo = tier_na_cislo[tier_pismeno.lower()]
        tier_cisla.append(tier_cislo)
    else:
        print("""BLUDE!: "zadej tier S-F (X=exit)!:" """)
