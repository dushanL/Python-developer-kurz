# Jednodušší úkol:
# Vytvořte tři proměnné: věk kupujícího, jeho aktuální zůstatek peněz a cenu piva. Napište podmínku, která rozhodne, zda si uživatel může koupit pivo.
# Hodnoty všech proměnných můžete zadat v programu staticky, nebo je dynamicky přijmout z uživatelského vstupu. Pokud si uživatel může pivo koupit,
# vypiš jeho zůstatek peněz po nákupu.
#
# Pokud si pivo může koupit, vypište například:
# "Můžeš si koupit pivo! Zůstatek peněz na účtu: 320Kč"
# Pokud si ho koupit nemůže, vypište odpovídající zprávu, například:
# "Nemůžeš si koupit pivo: nesplňuješ podmínky."



age = int(input("Zadaj svoj vek: "))
money = float(input("Zadaj zostatok peňazí na účte: "))
beer_price = float(input("Zadaj cenu piva: "))
balance = money - beer_price

if age<18:
    print("Nemôžeš si kúpiť pivo: nesplňuješ podmienky.")
else:
    print(f"Môžeš si kúpiť pivo! Zostatok peňazí na účte: {balance}€")
