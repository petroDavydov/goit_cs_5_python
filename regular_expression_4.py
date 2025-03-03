# print(("spam " "eggs") == "spam eggs")  # True
# print("Hello\tWorld!")
# print("Hello my little\rsister")
# print("Hello\\World")
# ----------
# find

string = "There are Trumple !"
# start = 0
# end = 17
# print(f"This is find: {string.find("are",start, end)}")
# print(f"This is find: {string.find("um")}")
# print(f"This is index: {string.index("le")}")
# print(f"This is index: {string.index("le", start, end)}")
# print(f"This is rfind: {string.rfind("Tr")}")
# print(f"This is rindex: {string.rindex('u')}")
# ----------
# split()

# split_use = string.split()
# print(f"This is use split(): {split_use}")

string = "There are Trumple!"
split_use_s = string.split('/', 3)
print(f"This is find with separator: {split_use_s}")
# --------------

# join()

string_join = ["This", "is", "world", "!"]
join_use = "/".join(string_join)
print(join_use)
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
