target_book = input()

checked_books = 0

current_book = input()
while current_book != "No More Books":
    if current_book == target_book:
        break

    checked_books += 1    
    current_book = input()

if current_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
else:
    print(f"You checked {checked_books} books and found it.")