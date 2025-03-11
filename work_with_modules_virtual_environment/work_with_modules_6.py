import sys
import os
# # -------------------
# print(f"This is sys.modules['os']: {sys.modules['os']}") # ???????? не працює в мене
# print(f"This is os.__file__: \n {os.__file__}") # працює в мене
# print(f"This is dir(os): \n {dir(os)}")
# print(f"This is sys.modules.keys(): \n {sys.modules.keys()}")
# print(f"This is sys.builtin_module_names: {sys.builtin_module_names}")
# print(f"This is sys.path: \n {sys.path}")
# # -----------------------------
# скрипти включати по порядку для розуміння їх роботи
# скрипт 2

for arg in sys.argv:
    print(arg)

# команда яку треба запустити що запрацював скрипт 2:
# python work_with_modules_6.py test --user -hello some text
# ---------------------------

# скрипт 3


# def main():
#     if len(sys.argv) > 1:
#         print(sys.argv[1])


# if __name__ == "__main__":
#     main()


# # python work_with_modules_6.py 123
# # команда яку треба запустити що запрацював скрипт 3

# -----------------------
