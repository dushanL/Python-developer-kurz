books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]

# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
##pridavam 2 knihy v jednom kroku pomocou extend
books.extend([{
    "name": "Pán prsteňov: Dve veže",
    "price": 505,
    "author": "J.R.R. Tolkien",
    "publication_year": 1954, },
    {
        "name": "Pán prsteňov: Návrat kráľa",
        "price": 510,
        "author": "J.R.R. Tolkien",
        "publication_year": 1955, }
])

# pridavam 1 knihu pomocou append
books.append({
    "name": "Hobbit",
    "price": 505,
    "author": "J.R.R. Tolkien",
    "publication_year": 1937, }
)
print(books)

# 2. Změň cenu jedné libovolné knihy. Vypiš list.
books[1]["price"] = 400
print(books)

# 3. Odstraň nějakou knihu. Vypiš list.
books.pop(0)
print(books)

# 4. Vypiš celkový počet knih v listu.
print(len(books))

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)
name = input("Zadaj názov knihy: ")
price = input("Zadaj cenu: ")
author = input("Zadaj autora: ")
publication_year = input("Zadaj rok vydania: ")

books.append({
    "name": name,
    "price": price,
    "author": author,
    "publication_year": publication_year }
)
last_book = books[-1]
print("Pridaná kniha:")
print(last_book)
print(books)
