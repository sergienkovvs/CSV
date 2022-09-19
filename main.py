import json
import csv

with open("sample.json") as f:
    phone_book = json.load(f)

with open("sample.csv", "w") as f:
    field_names = ["телефон", "имя","возраст"]
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    for key, value in phone_book.items():
        phone_book_entry = {
            field_names[0]: key,
            field_names[1]: value[0],
            field_names[2]: value[1]
            }
        writer.writerow(phone_book_entry)
