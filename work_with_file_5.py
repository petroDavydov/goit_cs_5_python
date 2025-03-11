# write
from pathlib import Path
from pathlib import PurePath
import shutil
fh = open('text.txt', 'w')
symbols_written = fh.write("Hothing Heppend")
print(f"This is symbol written: {symbols_written}")
fh.close()
# --------------

# read

fh = open('text.txt', 'w+')
fh.write("Hello World!")
fh.seek(0)
first_5_symbols = fh.read(5)  # read
print(f"This is first 5 symbols: {first_5_symbols}")
fh.close()
# --------------------

# read all file

fh = open('text.txt', 'w')
fh.write('Hello World !')
fh.close()

fh = open('text.txt', 'r')
all_file_read = fh.read()
print(f"This is read(), mean all file read: {all_file_read}")

fh.close()
# ------------------

# read file untill descriptor do not close

fh = open('text.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(f"This is count symbol length: {symbol}")

fh.close()
# ----------------------

# read line by line method: readline()

fh = open('text.txt', 'w')
fh.write('*first line\n*second line\n*third line')
fh.close()

fh = open('text.txt', 'r')
while True:
    line_read = fh.readline()
    if not line_read:
        break
    print(f"This is method readline(): {line_read}")

fh.close()
# -------------------

# readlines()

fh = open('text.txt', 'w')
fh.write('*first line\n*second line\n*third line')
fh.close()

fh = open('text.txt', 'r')
while True:
    line_read = fh.readlines()
    if not line_read:
        break
    print(f"This is method readlineS(): {line_read}")

fh.close()
# --------------------

# use strip() and readlines()


fh = open('text.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('text.txt', 'r')

lines_strip_readlines = [el.strip() for el in fh.readlines()]

print(f"This is method strip() and readline(): {lines_strip_readlines}")

fh.close()
# -------------------------

# method seek()

fh = open('txt.txt', 'w+')
fh.write('Hello World!')

fh.seek(0)
# second_0 = fh.read(0)
second_1 = fh.read(1)
second_2 = fh.read(2)
second_3 = fh.read(3)

# print(f"This is second_0: {second_0}")
print(f"This is second_1: {second_1}")
print(f"This is second_2: {second_2}")
print(f"This is second_3: {second_3}")

fh.close()
# ---------------------------

# method tell()

fh = open('text.txt', 'w+')
fh.write("Hello Now!")

position_1 = fh.tell()
print(f"Default position method tell(): {position_1}")

fh.seek(1)
position_2 = fh.tell()
print(f"This is seek() use, method tel(): {position_2}")

fh.read(2)
position_3 = fh.tell()
print(f"This is read() use method tell(): {position_3}")

fh.close()
# ---------------------

# Менеджер контексту

fh = open('text.txt', 'w')
try:
    # Виконання операцій з файлом
    res = fh.write('Some data')
finally:
    # Закриття файлу в блоку finally гарантує, що файл закриється навіть у разі помилки
    print(res)
    fh.close()

# ------------
with open('text.txt', 'w') as fh:
    # Виконання операцій з файлом
    fh.write('Some data + + + ')
# Файл автоматично закриється після виходу з блоку with
# --------------

with open("text.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("text.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(f"This is use open, 'r', 'w', and 'with': {lines}   ")
# ---------------------------------

# Робота з не текстовими файлами у Python

with open("text.bin", "wb") as fh:
    fh.write(b"Hello World!")
# -------------------------

s = b'hello world!'
print(s[0])
print(s[1])
# -----------

byte_string = b"Hello People!"
print(byte_string)

byte_str = "some text".encode()
print(byte_str)
# -----------------------

# Перетворення чисел на байт-рядки

# пердставлено у 16-річному форматі
numbers = [0, 128, 255]
bytes_numbers = bytes(numbers)
print(f"This is bytes number performance: {bytes_numbers}")

# use function hex()

numbers = [127, 255, 56]
for i in numbers:
    print(f"This is hex()function: {hex(i)}")

# ----------------------

# code in ASCII,UTF-8, CP1251

res_ord = ord('a')
print(f"This is ord() function: {res_ord}")

res_chr = chr(121)
print(f"This is chr() function: {res_chr}")
# -----------------

s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)
# -----------------------

print(b'Hello World!'.decode('utf-16'))  # 效汬⁯潗汲Ⅴ
# ----------------------
# Масив Байтів

byte_array = bytearray(b"Kill Bill")
byte_array[0] = ord("B")
byte_array[5] = ord('K')
print(f"This is bytearray: {byte_array}")

# can add and remove elemrnts

byte_array = bytearray(b"Hello")
byte_array.append(ord('!'))
print(f"This is add symbols using bytearray: {byte_array}")

# return to row using decode()

byte_array = bytearray(b"Hello World!")
string = byte_array.decode("UTF-8")
print(f"This is use decode(): {string}")
# --------------------------
# Порівняння рядків

string_1 = "Hello World!"
string_2 = "hello world!"

if string_1.lower() == string_2.lower():
    print("Equal")
else:
    print("not equal")
# -------------------------------

# methhod casefold()

text = "Python Programming"
print(f"This is method casfold(): {text.casefold()}")
# ---------------------------
# приклад для іноземних мов таких як німецька

german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")  # False
print(f"Порівняння з casefold(): {casefold_comparison}")  # True
# ------------------
# Архівування файлів

# shutil.make_archive("example_1", "zip", root_dir="LAB")
# shutil.make_archive("example_2", "tar", root_dir="LAB")
# shutil.make_archive("example_3", "gztar", root_dir="LAB")
# shutil.make_archive("example_4", "bztar", root_dir="LAB")
# shutil.make_archive("example_5", "xztar", root_dir="LAB")
# ----------------------------------------------

# unpack files, shutil

# shutil.unpack_archive("example_1.zip", "testshutil")

# some power of shutil

# shutil.copy("text.bin", "testshutil")
# shutil.copytree("LAB", "testshutil")  # папка створюється автоматичн
res_shutil = shutil.disk_usage("D:/goit_cs_5_python/testshutil")
print(f"This is result of command shutil.disk_usage('path'): {res_shutil}")
print(
    f"This is result of command shutil.disk_usage('C:/'): {shutil.disk_usage("C:/")}")
# --------------------------

# pathlib, PurePath/ from pathlib import PurePath

p = PurePath("/d/goit_cs_5_python/text.txt/")
print(f"This is p.name: {p.name}")
print(f"This is p.suffix: {p.suffix}")
print(f"This is p.parent: {p.parent}")
# -------------

# p1 = Path("example.txt")
# p1.write_text("Hello people now world!")
# print(f"This is read_text() use Path:{p1.read_text()}")
# print(f"This is exists() use Path:{p1.exists()}")
# -----------------------------

original_path = Path("/d/goit_cs_5_python/example.txt")
print(original_path)

# new_path = original_path.with_name("report.txt")
# print(f"This is use with_name(): {new_path}")
# ???--------------------------

# with_suffix

# original_path_suffix = Path("example6.txt")
# print(original_path_suffix)

# new_path_suffix = original_path_suffix.with_suffix(".md")
# print(new_path_suffix)
# # ----------------
# original_path_rename = Path( "example.txt")

# new_path_rename = original_path_rename.with_name("report7.txt")
# result_rename = original_path_rename.rename(new_path_rename)
# print(result_rename)
# -------------------

path = Path("testshutil")

# Перевірка існування
if path.exists():
    print(f"EXEXEX {path} існує")

# Перевірка, чи це директорія
if path.is_dir():
    print(f"DDD {path} є директорією")

# Перевірка, чи це файл
if path.is_file():
    print(f"FFF {path} є файлом")
# -----------------------

file_path = Path('txt1.txt')
file_path.unlink(missing_ok=False)
