#Quest 1
# urdu_to_english = {
    # "kursi": "chair",
    # "pani": "water",
    # "kitab": "book",
    # "ghar": "house",
    # "dost": "friend",
    # "khana": "food",
    # "raat": "night",
    # "din": "day",
    # "suraj": "sun",
    # "chand": "moon",
    # "shehar": "city",
    # "mulk": "country",
    # "khandan": "family",
    # "waqt": "time",
    # "ustad": "teacher",
    # "talib_ilm": "student",
    # "school": "school",
    # "gari": "car",
    # "sadak": "road",
    # "darwaza": "door",
    # "khidki": "window",
    # "mez": "table",
    # "bistar": "bed",
    # "kamra": "room",
    # "aasman": "sky",
    # "zameen": "ground",
    # "darakht": "tree",
    # "phool": "flower",
    # "bacha": "child",
    # "aurat": "woman",
    # "aadmi": "man",
    # "bhai": "brother",
    # "behan": "sister",
    # "maa": "mother",
    # "baap": "father",
    # "kaam": "work",
    # "paisa": "money",
    # "dukan": "shop",
    # "bazar": "market",
    # "safar": "journey",
    # "hawai_jahaz": "airplane",
    # "train": "train",
    # "kapray": "clothes",
    # "joota": "shoe",
    # "topi": "cap",
    # "chai": "tea",
    # "doodh": "milk",
    # "cheeni": "sugar",
    # "namak": "salt",
    # "roti": "bread"
# }
# value = input("Enter a word that u want the meaning of :")
# if value in urdu_to_english:
    #  print(urdu_to_english[value])
# else:
    # print("word not found in the dictionary!")
#another method 
#print (urdu_to_english[value])
#Quest 2:
# s = set()
# no = input("Enter a number : ")
# s.add(int(no))
# no = input("Enter a number : ")
# s.add(int(no))
# no = input("Enter a number : ")
# s.add(int(no))
# no = input("Enter a number : ")
# s.add(int(no))
# no = input("Enter a number : ")
# s.add(int(no))
# no = input("Enter a number : ")
# s.add(int(no))
# no = input("Enter a number : ")
# s.add(int(no))
# no = input("Enter a number : ")
# s.add(int(no))
# print(s)
#Quet 3
# s = set(18,'18')
# print(s)---> set() takes only one argument → design/signature restriction 
# (unrelated to iteration) That one argument must be iterable → 
# because set()'s job is to iterate it and pull out elements
# s = set()
# s.add(18)
# s.add('18')
# print(s)
# Quest 4
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
# print(len(s))
# Explanation --> Because Python compares values, not types, when using ==. 
# Even though 20 is an int and 20.0 is a float, they represent the same numeric value — 
# so Python converts them to a common type internally for comparison and finds them equal.
#Quest 5
# s = {}
# print(type(s))
#Quest 6
d = {}
name = input("Enter your name : ")
lang = input("Enter language : ")
d[name] = lang # d.update({name:lang})

name = input("Enter your name : ")
lang = input("Enter language : ")
d[name] = lang

name = input("Enter your name : ")
lang = input("Enter language : ")
d[name] = lang

name = input("Enter your name : ")
lang = input("Enter language : ")
d[name] = lang
print(d)
#Quest 7 -> if  keys  same and value diff then the value will be updated for that key but 
# if values same then ? nothing will happen
#  keys cannt be same keys are identifer so they should be different
