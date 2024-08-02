tier_na_cislo = {
    "s": 6,
    "a": 5,
    "b": 4,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 0
}

tier_cisla = []

print("zadej tier S-F (X=exit):")
while True:
    tier_pismeno = input()
    if tier_pismeno.lower() == "x":
        print("*"*35)
        for num in tier_cisla:
            print(num)
        break
    elif tier_pismeno.lower() in tier_na_cislo:
        tier_cislo = tier_na_cislo[tier_pismeno.lower()]
        tier_cisla.append(tier_cislo)
    else:
        print("""BLUDE!: "zadej tier S-F (X=exit)!:" """)
