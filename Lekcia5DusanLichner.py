numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.
for x in numbers:
    if x >= 0:
        print(x)

# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči
i = 0
while True:
    if len(names) == i or names[i] == "Alice":
        break
    print(names[i])
    i += 1

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0
random_codes_new = [n for n in random_codes if "0" in n]
print(random_codes_new)

# Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'
for code in random_codes:
    count = 0
    last_c = ""
    for c in code:
        count = count + 1 if c == last_c else 1
        last_c = c
    if count >= 3:
        print(code)