# import pandas as pd

CATEGORIES = {
    1: "groceries",
    2: "healthcare",
    3: "entertainment",
    4: "utilities",
}


# maybe use a dataframe instead of a list
def process_data() -> list:
    data = []

    # TODO: Make the month input smart
    # - accept text and numbers
    # - maybe datetime module
    month = input("Month: ")

    while True:
        amount = input("Amount: ")
        if amount == "":
            break

        for num, category in CATEGORIES.items():
            print(f"{num}: {category}")

        category = input("\nCategory: ")

        data.append([month, amount, category])

    return data


if __name__ == "__main__":
    data: list = process_data()
    print(data)
