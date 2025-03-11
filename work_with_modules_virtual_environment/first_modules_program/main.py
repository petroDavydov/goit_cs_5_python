from jokes_handler import get_random_joke


def main():
    name = input("Enter Your Name?")
    print(f"Hi {name}")

    while True:
        user_response = input(f"{name} , wona hear story?(yes/no)").lower()
        if user_response == "yes":
            print(get_random_joke())
        elif user_response == "no":
            print(f"Good Buy {name} !")
            break


if __name__ == "__main__":
    main()
