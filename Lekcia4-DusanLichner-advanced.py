# Program bude pracovat se třemi údaji: věk zákazníka, cena jízdenky a zda je nakupující zaměstnancem tramvajové služby.
# Hodnoty pro údaje k určení ceny jízdenky můžeš určit libovolně přímo v kódu [+0B],
# nebo je můžeš načíst z uživatelského vstupu - pomocí funkce input [+1B],
# pokud ještě navíc ukončíš program s chybovou hláškou, když je zadaný datový typ špatný, dostaneš [+1B]
# Program určí a následně vypíše konečnou cenu na základě těchto kritérií:
# Plná cena jízdenky je 45 Kč.
# Cestující do 12 let jezdí zdarma.
# Cestující mladší 18 let má slevu 50%.
# Cestující nad 65 let mají 30% slevu.
# Zaměstnanci tramvajové služby mají slevu 80%.
# Zaměstnanci tramvajové služby nad 55 let mají jízdenku zdarma.

ticket_price = 45
discount = {"do_12_rokov":100,
            "do_18_rokov":50,
            "nad_65_rokov":30,
            "zamestnanec":80,
            "zamestnanec_nad_55":100,
            "plna_cena":0
            }
age = input("Zadaj vek: ")
employee = "N"


if not age.isdigit():
    age = input("Skusme to este raz. Zadaj vek v správnom formáte: ")
    if not age.isdigit():
        print("Chybne zadaný vek.")
        exit()
else:
    age = int(age)
    if age > 120:
        age = input("Zadaj skutočný vek: ")
        if not age.isdigit():
            print("Chybne zadaný vek.")
            exit()
age = int(age)

age_category = "plna_cena"
if age< 18:
    age_category = "do_12_rokov" if age <= 12 else "do_18_rokov"
else:
    age_category = "nad_65_rokov" if age > 65 else "plna_cena"

    employee = input("Ste zamestnanec dopravneho podniku? A-áno, N-nie : ").upper()
    if employee not in ("A", "N"):
        employee = input("Skusme to este raz. Ste zamestnanec dopravneho podniku? A-áno, N-nie : ").upper()
        if employee not in ("A", "N"):
            print("Chybné zadanie.")
            exit()
    else:
        if employee == "A":
            age_category = "zamestnanec_nad_55" if age > 55 else "zamestnanec"

discount_percent = discount[age_category]
after_discount = ticket_price * (1 - discount_percent / 100)

print(f"Cena lístku je: {after_discount}. Započítaná zľava {discount_percent} %" )