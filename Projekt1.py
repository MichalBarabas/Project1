"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Michal Barabáš  
email: mbarabas@csas.cz
discord: 
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


# zakladni databaze uzivatelu
uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}

line = 40 * "-"

#Prihlaseni, uzivazele, heslo
def login():
    username = input("Zadejte jméno: ")
    password = input("Zadejte heslo: ")

    if username in uzivatele and uzivatele[username] == password:
       print(f"""
{line}
Welcome to the app, {username}
We have {(len(TEXTS))} texts to be analyzed
{line}""")
    else:
        print("Neregistrovaný uzivatel, konec.")
        quit()
        
login()

#Zvoleni textu 
chosen_number = input(f"Enter a number btw. 1 and {(len(TEXTS))} to select:")
print(line)

#Vyber textu 
if chosen_number.isdigit() and int(chosen_number) <= len(TEXTS) and int(chosen_number) != 0:
    number_of_text = int(chosen_number) -1
else:
    print("Neplatný vstup, ukončuji..")
    quit()

#list slov bez speciálních znaků
list_of_words = []
 
for word in TEXTS[number_of_text].split():
    list_of_words.append(word.strip(",.:;"))
while "" in list_of_words:
        list_of_words.remove("")
   
count_of_len_words = []
list_of_lowers = []
list_of_numbers = []
list_of_capitals = []
list_of_uppers = []

for word in list_of_words:
    count_of_len_words.append(len(word))  #Počet slov
    firts_letter = word[0].isupper()      #počet slov psaných velkými písmeny
    if word.islower() and word.isalpha(): #počet slov psaných malými písmeny
        list_of_lowers.append(word)
    if word.isdigit():                    #počet čísel (ne cifer)
        list_of_numbers.append(word)    
    if firts_letter is True:              #počet slov psaných velkými písmeny
        list_of_capitals.append(word)
    if word.isupper():                    #Velkým písmem celý
        list_of_uppers.append(word)

#soucet císel v textu
total = 0

for number in list_of_numbers:
    total += int(number)

#počet slov vůči délce slova 1-11 písmen
dict_len_num = {}

#Spocítání délek z listu a zapsáno do slovníku
for number in count_of_len_words:
    number_count = count_of_len_words.count(number)
    dict_len_num.update({number: number_count})

#Počet slov
print(f"There are {len(list_of_words)} words in the selected text.")

#počet slov psaných velkými písmeny
print(f"There are {len(list_of_capitals)} titlecase words.")

#Velkým písmem celý
print(f"There are {len(list_of_uppers)} uppercase words.")

#počet slov psaných malými písmeny
print(f"There are {len(list_of_lowers)} lowercase words.")

#počet čísel (ne cifer)
print(f"There are {len(list_of_numbers)} numeric strings.")

#sumu všech čísel 
print(f"""The sum of all the numbers {total}
{line}
""")

#Vypsání výsledků
print(
    f"LEN|", "OCCURENCES".center(24), "|NR."
)
print(line)

list_len_num = list(dict_len_num.keys())
list_len_num.sort()

for i in list_len_num:
    hodnota = dict_len_num.get(i)
    print(f"{i:>3}|{'*' * hodnota:<26}|{hodnota}")

print(line)
