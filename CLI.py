import datetime
import json
import sys

import keyboard
import pandas as pd


# Load existing data from the local JSON file to keep the session persistent
def loadExpenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Initialize the global expenses list
expenses = loadExpenses()

while True:
    print("1 - Add Expense")
    print("2 - View Expenses")
    print("3 - Show category totals")
    print("4 - Exit")
    print("")

    userSelection = str(input())

    # --- FUNCTION: Create/Add New Data ---
    def optionOne():
        date = input("Insert the date of the expense (YYYY/MM/DD): ")
        description = input(
            "Insert the description of the expense (Coffee, Bag, Smoothie, etc...): "
        )
        amount = input("Insert the amount spent ($): ")
        category = input(
            "Insert the category of the expense (Food, Transport, Rent, Clothes): "
        )

        category = category.capitalize()
        description = description.capitalize()

        # Creating the dictionary (The fundamental unit of our JSON storage)
        expense = {
            "date": date,
            "description": description,
            "amount": amount,
            "category": category,
        }

        expenses.append(expense)

        # Writing the updated list back to the hard drive
        try:
            with open("expenses.json", "w") as file:
                json.dump(expenses, file, indent=4)

            print("Expense added!")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Failed to add")
            input("Press any key")

        print("")
        print("Press Enter to go back")
        input()
        if keyboard.is_pressed("Enter"):
            return

    # --- FUNCTION: Data Visualization with Pandas ---
    def optionTwo():
        if expenses == "":
            print(
                "You don't have any expenses registered, please come back and add expenses to view them!"
            )
            print("Press Enter to go back")
            input()
            if keyboard.is_pressed("Enter"):
                return
        else:
            table = pd.DataFrame(expenses)
            print(table)
            print("")

            sum = 0

            for expense in expenses:
                sum += float(expense["amount"])

            print("Total spent: US$", sum)

            print("")
            print("Press Enter to go back")
            input()
            if keyboard.is_pressed("Enter"):
                return

    # --- FUNCTION: Data Analysis and Filtering ---
    def optionThree():
        totalFood, totalTransport, totalRent, totalClothes = 0, 0, 0, 0
        recentFood, recentTransp, recentRent, recentClothes = 0, 0, 0, 0

        # Setting up time-based filtering (Last 7 days logic)
        dateToday = datetime.datetime.now()
        filterDate = int((dateToday.strftime("%d"))) - 7

        for expense in expenses:
            match expense["category"]:
                case "Food":
                    totalFood += float(expense["amount"])
                case "Transport":
                    totalTransport += float(expense["amount"])
                case "Rent":
                    totalRent += float(expense["amount"])
                case "Clothes":
                    totalClothes += float(expense["amount"])

        totalExpense = pd.DataFrame(
            {
                "Food": [totalFood],
                "Transport": [totalTransport],
                "Rent": [totalRent],
                "Clothes": [totalClothes],
            }
        )

        print(totalExpense)

        for expense in expenses:
            dateExpense = datetime.datetime.strptime(expense["date"], "%Y/%m/%d")
            dateExpense = int(dateExpense.strftime("%d"))
            if dateExpense >= filterDate:
                match expense["category"]:
                    case "Food":
                        recentFood += float(expense["amount"])
                    case "Transport":
                        recentTransp += float(expense["amount"])
                    case "Rent":
                        recentRent += float(expense["amount"])
                    case "Clothes":
                        recentClothes += float(expense["amount"])

        print("")
        print("Food on the last 7 Days: ", recentFood)
        print("Transport on the last 7 Days: ", recentTransp)
        print("Rent on the last 7 Days: ", recentRent)
        print("Clothes on the last 7 Days: ", recentClothes)

        print("")
        print("Press Enter to go back")
        input()
        if keyboard.is_pressed("Enter"):
            return

    def optionFour():
        sys.exit("Closing...")

    # Main Menu Routing
    match userSelection:
        case "1":
            print("")
            optionOne()
        case "2":
            print("")
            optionTwo()
        case "3":
            print("")
            optionThree()
        case "4":
            print("")
            optionFour()
        case _:
            print("")
            print("Unknown command, please type one of the listed above")
