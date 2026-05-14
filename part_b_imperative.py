expenses = [
    {"date": "2024-01-05", "category": "Food",          "amount": 42.50, "description": "Groceries"},
    {"date": "2024-01-07", "category": "Transport",     "amount": 15.00, "description": "Bus pass"},
    {"date": "2024-01-09", "category": "Entertainment", "amount": 60.00, "description": "Concert ticket"},
    {"date": "2024-01-10", "category": "Food",          "amount": 8.75,  "description": "Coffee & snack"},
    {"date": "2024-01-12", "category": "Utilities",     "amount": 120.00,"description": "Electricity bill"},
    {"date": "2024-01-14", "category": "Food",          "amount": 55.20, "description": "Restaurant dinner"},
    {"date": "2024-01-15", "category": "Transport",     "amount": 30.00, "description": "Taxi"},
    {"date": "2024-01-17", "category": "Entertainment", "amount": 14.99, "description": "Streaming subscription"},
    {"date": "2024-01-20", "category": "Food",          "amount": 38.00, "description": "Groceries"},
    {"date": "2024-01-22", "category": "Utilities",     "amount": 45.00, "description": "Internet bill"},
    {"date": "2024-01-25", "category": "Transport",     "amount": 22.00, "description": "Train ticket"},
    {"date": "2024-01-28", "category": "Entertainment", "amount": 25.00, "description": "Book"},
]

# B1 — Total and count 
total = 0.0
record_count = 0
for expense in expenses:
    total = total + expense["amount"]
    record_count = record_count + 1

print(f"Total expenses: {total:.2f}")
print(f"Number of records: {record_count}\n")

# B2 — Category breakdown 
category_totals = {}
for expense in expenses:
    cat = expense["category"]
    if cat in category_totals:
        category_totals[cat] = category_totals[cat] + expense["amount"]
    else:
        category_totals[cat] = expense["amount"]

print("Category breakdown:")
category_names = []
for name in category_totals:
    category_names.append(name)

n_categories = 0
for x in category_names:
    n_categories = n_categories + 1

# Alphabetical order: bubble sort (length = number of categories, not number of expenses)
i = 0
while i < n_categories:
    j = 0
    while j < n_categories - 1 - i:
        if category_names[j] > category_names[j + 1]:
            temp = category_names[j]
            category_names[j] = category_names[j + 1]
            category_names[j + 1] = temp
        j = j + 1
    i = i + 1

k = 0
while k < n_categories:
    cat = category_names[k]
    amt = category_totals[cat]
    print(f"  {cat} : {amt:.2f}")
    k = k + 1

# B3 — Most and least expensive (no max/min builtins)
most = expenses[0]
least = expenses[0]
for expense in expenses:
    if expense["amount"] > most["amount"]:
        most = expense
    if expense["amount"] < least["amount"]:
        least = expense

print(f"\nMost expensive : {most['description']} ({most['category']}) — {most['amount']:.2f}")
print(f"Least expensive: {least['description']} ({least['category']}) — {least['amount']:.2f}")

# B4 — Average with a loop, then second loop for strictly above average
sum_for_avg = 0.0
count_for_avg = 0
for expense in expenses:
    sum_for_avg = sum_for_avg + expense["amount"]
    count_for_avg = count_for_avg + 1

average = sum_for_avg / count_for_avg
print(f"\nAverage expense: {average:.2f}")
print("Expenses above average:")
for expense in expenses:
    if expense["amount"] > average:
        print(f"  - {expense['description']} ({expense['amount']:.2f})")
