# print(("spam " "eggs") == "spam eggs")  # True
# print("Hello\tWorld!")
# print("Hello my little\rsister")
# print("Hello\\World")
# ----------
# find


string = "There are Trumple !"
print(len(string))
start = 0
end = 17
print(f"This is find: {string.find("are",start, end)}")
print(f"This is find: {string.find("um")}")
print(f"This is index: {string.index("le")}")
print(f"This is index: {string.index("le", start, end)}")
print(f"This is rfind: {string.rfind("Tr")}")
print(f"This is rindex: {string.rindex('u')}")
# ----------
# split()

split_use = string.split()
print(f"This is use split(): {split_use}")

string = "There are Trumple!"
split_use_s = string.split('/', 3)
print(f"This is find with separator: {split_use_s}")
# --------------

# join()

string_join = ["This", "is", "world", "!"]
join_use = "/".join(string_join)
print(f"This is use join with separator: {join_use}")
# -------------

# strip()

strip_string = "     This is use method strip !    ".strip()
strip_use = strip_string.strip()
print(f"This is use strip(): {strip_string}")
# ----------------

# replace()

string_replace = "This is use method strip !"
replace_use = string_replace.replace("strip", "replace")
print(f"This is replace use: {replace_use}")
# --------------

# removeprefix

removeprefix_word = "TheHarvester"
print(removeprefix_word)
removeprefix_use = removeprefix_word.removeprefix("The")
print(f"This is removeprefix use: {removeprefix_use}")

# removesuffix()
print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))

# ----------

number = "12345"
# Виведе: True
print(f"This is use isdigit(), ALL numbers: {number.isdigit()}")

text = "Number123"
# Виведе: False
print(f"This is use isdigit(), NOT all numbers: {text.isdigit()}")
# ------------------------

# translate(), str.marketrans()


intab = "abciou"
outtab = "123456"
trantab = str.maketrans(intab, outtab)

str = "This are always cute baby"
print(f"This is use translate, marketrans: {str.translate(trantab)}")

# DELETE using translate() and str.marketrans()

intab_2 = 'thmdplks'
trantab = str.maketrans('', '', intab_2)

str = "The more and more people try to understand what`s happened last week"
print(
    f"This is use marketrans and transalte for DELETE symbols: {str.translate(trantab)}")
# ---------

# Форматування рядків

for i in range(8):
    s = f" int: {i:d}; hex: {i:#x}; oct: {i:#o}; bin: {i:#b} "
    print(f"Result formating row: \n {s}")
# ----------------

width = 5
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')
# ---------------

name = "Alice"
form = f"{name:>10}"
form_1 = f"{name:<10}"
form_2 = f"{name:^50}"
print(form)
print(form_1)
print(form_2)
# ------------------

import re
completion = 0.7456
formatted = f"{completion:.2%}"
print(f"Use :.2f: {formatted}")
# -----------------------

progress = 0.5
formatted = f"{progress:.0%}"
print(f"Use :.0% : {formatted}")
# ----------------------------

# Regular expressions(regex, regexp)


string = "Study Python will be fun!"
pattern = "Python"

result = re.search(pattern, string)

if result:
    print(f"Find word in text: {result.group()}")
else:
    print(f"Nothing find")
# ------------------------------

# Для пошуку слова в рядку
string = "Study Python will be fun!"
pattern_1 = r"s\w*y"

match = re.search(pattern_1, string, re.IGNORECASE)

if match:
    print(f"Find word start s end y:", match.group())
# ------------------------------
# find email
text_email = "This is my email sh@example.com"
pattern_2 = r"\w+@\w+\.\w+"
match_email = re.search(pattern_2, text_email)

if match_email:
    print("Find email: ", match_email.group())
# ------------------------

# витягування ім'я користувача з email та домену

email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)" # # варіант з екрануванням
pattern_3 = r"(\w+)@(\w+).(\w+)"
match_u_d = re.search(pattern_3, email)

if match_u_d:
    user_name = match_u_d.group(1)  # вилучння тексту відповідно до шаблону
    domain_name = match_u_d.group(2)  # вилучння тексту відповідно до шаблону
    # вилучння тексту відповідно до шаблону
    domain_name_com = match_u_d.group(3)
    print(f'Username: {user_name}')
    print(f'Domain : {domain_name}')
    print(f'Domain_com : {domain_name_com}')
# ------------------------------

# find number in sting

text_with_number = "In 2023 was warster then 2022."
pattern_number = r"\d+"
matches_number = re.findall(pattern_number, text_with_number)

print(f"Find all matches with number: {matches_number}")
# ------------------------------

# find all in sentence

text_sentence = "Python is easy and powerfull programing language"
pattern_sentence = r"\w+"
matches_sentence = re.findall(pattern_sentence, text_sentence)

print(f"Find all words in sentence: {matches_sentence}")
# ----------------------

# find all email in sentence

text_all_email = "Contacts: example1@example.com, example2@sample.org, example3@sample.org"
pattern_all_email = r"\w+@\w+\.\w+"
matches_all_email = re.findall(pattern_all_email, text_all_email)

print(f"Find all email: {matches_all_email}")
# ------------------------------

# re.sub(pattern, repl, string)

# rename space on underline

file_name = "This is my file.pdf"
pattern_file = r"\s"
replacement_file = "/"

formated_name_file = re.sub(pattern_file, replacement_file, file_name)

print(f"Use re.sub(ptrn,repl,text): {formated_name_file}")
# -------------------------

# remove all punctuation of string

remove_punctuation = "Python - is powrfull, universal; language!"
pat_rem_punct = r"[;,\-:!\.]"
repl_punct = ""

with_remove_punctuation_text = re.sub(
    pat_rem_punct, repl_punct, remove_punctuation)

print(f"Text with remove punctuation: {with_remove_punctuation_text}")
# ---------------

# Formating phone number

phone_tabe = """
        John Doe: 050-171-1634
        Mike Wasberg: 063-134-1729
        Rute Conahan: 068-234-5612
        """

pattern_phone_number = r"(\d{3})-(\d{3})-(\d{4})"
repl_phone_number = r"(\1) \2-\3"
repl_phone_number_result = re.sub(
    pattern_phone_number, repl_phone_number, phone_tabe)

print(f"Use re.sub() for phone number: {repl_phone_number_result}")
# -----------------------
# split text by words


text_split = "Python - is simple, but  powerfull programing language!"
pattern_split = r"\s+"
words_split = re.split(pattern_split, text_split)
print(f"Use re.split: {words_split}")
# -----------------------------------
# slit text by words use punctuations

text_split = "Python - is simple; but  powerfull,  programing: language!"
pattern_split = r"[;,\-:!\s]+"
el_split = re.split(pattern_split, text_split)

print(f"Use re.split for delete by punctuation: {el_split}")
# -------------------------------
# some different slit mark

text_split_dif = "apple#banana!mango@orange;kiwi"
patrn_text_split_dif = r"[#@;!]"
fruits_split_dif = re.split(patrn_text_split_dif, text_split_dif)

print(f"Use split with different split mark: {fruits_split_dif}")
# ------------------------

