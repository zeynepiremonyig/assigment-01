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


# Helper function
def _sorted_category_names(category_totals):
    """
    Return category names sorted alphabetically (same order as Part B bubble sort).

    Parameters:
        category_totals (dict): A dictionary that matches category names to total amounts

    Returns:
        list: Category names in alphabetical order.
    """
    names = []
    for name in category_totals:
        names.append(name)
    n = 0 # number of categories
    for _ in names:
        n = n + 1
    i = 0 # index for the outer loop
    while i < n:
        j = 0 # index for the inner loop
        while j < n - 1 - i:
            # Swap if out of order (bigger name should move right).
            if names[j] > names[j + 1]:
                temp = names[j]
                names[j] = names[j + 1]
                names[j + 1] = temp
            j = j + 1
        i = i + 1
    return names


# Part B1 logic: add every expense amount into one total.
def get_total(expense_list):
    """
    Calculate the total amount of all expenses.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        float: Sum of all 'amount' values.
    """
    total = 0.0
    for expense in expense_list:
        total = total + expense["amount"]  
    return total


# Part B1 logic: count how many rows are in the list.
def get_count(expense_list):
    """
    Return the number of expense records.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        int: Number of records in expense_list.
    """
    record_count = 0
    for _ in expense_list:
        record_count = record_count + 1  # one more record
    return record_count


# Part B2 logic: one running total per category name.
def get_category_totals(expense_list):
    """
    Build a mapping from category names to their total amounts.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        dict: {category: total_amount}
    """
    category_totals = {}
    for expense in expense_list:
        cat = expense["category"]
        # If we saw this category before, add to it; else start a new total.
        if cat in category_totals:
            category_totals[cat] = category_totals[cat] + expense["amount"]
        else:
            category_totals[cat] = expense["amount"]
    return category_totals


# Part B3 logic: walk the list and remember the biggest amount (no max()).
def get_most_expensive(expense_list):
    """
    Return the expense dict with the highest amount (no max() built-in).

    Parameters:
        expense_list (list): List of expense dictionaries (non-empty).

    Returns:
        dict: The expense record with the largest 'amount'.
    """
    most = expense_list[0]
    for expense in expense_list:
        if expense["amount"] > most["amount"]:
            most = expense
    return most


# Part B3 logic: walk the list and remember the smallest amount (no min()).
def get_least_expensive(expense_list):
    """
    Return the expense dict with the lowest amount (no min() built-in).

    Parameters:
        expense_list (list): List of expense dictionaries (non-empty).

    Returns:
        dict: The expense record with the smallest 'amount'.
    """
    least = expense_list[0]
    for expense in expense_list:
        if expense["amount"] < least["amount"]:
            least = expense
    return least


# Part B4 logic: total divided by count (reuses get_total and get_count).
def get_average(expense_list):
    """
    Return the average expense amount as a float.

    Parameters:
        expense_list (list): List of expense dictionaries (non-empty).

    Returns:
        float: Mean of all 'amount' values.
    """
    return get_total(expense_list) / get_count(expense_list)


# Part B4 logic: keep only rows strictly greater than the average.
def get_above_average(expense_list):
    """
    Return a list of expense dicts whose amount is strictly above the average.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        list: Expense dicts with amount greater than the average (same order as input).
    """
    average = get_average(expense_list)
    result = []
    for expense in expense_list:
        if expense["amount"] > average:  # strictly above average, like Part B
            result.append(expense)
    return result


# Print the full report: calls the small functions instead of redoing the math.
def print_summary(expense_list):
    """
    Print a full summary report using the helper functions above.
    Produce the same output as Parts B1–B4 combined.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        None
    """
    # --- Part B1 style lines: total and count ---
    total = get_total(expense_list)
    record_count = get_count(expense_list)
    print(f"Total expenses: {total:.2f}")
    print(f"Number of records: {record_count}\n")

    # --- Part B2 style lines: per category, A–Z order ---
    category_totals = get_category_totals(expense_list)
    print("Category breakdown:")
    for cat in _sorted_category_names(category_totals):
        amt = category_totals[cat] 
        print(f"  {cat} : {amt:.2f}")

    # --- Part B3 style lines: highest and lowest single expense ---
    most = get_most_expensive(expense_list)
    least = get_least_expensive(expense_list)
    print(f"\nMost expensive : {most['description']} ({most['category']}) — {most['amount']:.2f}")
    print(f"Least expensive: {least['description']} ({least['category']}) — {least['amount']:.2f}")

    # --- Part B4 style lines: average and list above it ---
    average = get_average(expense_list)
    print(f"\nAverage expense: {average:.2f}")
    print("Expenses above average:")
    for expense in get_above_average(expense_list):
        print(f"  - {expense['description']} ({expense['amount']:.2f})")


# Run the program: show the report for the sample `expenses` list.
if __name__ == "__main__":
    print_summary(expenses)
