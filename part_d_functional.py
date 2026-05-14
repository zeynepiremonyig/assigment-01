"""
Part D — functional-style rewrites of selected Part C helpers.
Uses sum, comprehensions, map, filter, and lambdas instead of procedural loops.
"""

# Same average as Part C (uses get_total / get_count) so above-average matches.
from part_c_procedural import get_average


# D1 — Total with sum + generator expression
def get_total_functional(expense_list):
    """Calculate total using sum() and a generator expression."""
    # sum((expr for e in expense_list), 0.0) — 0.0 is the starting total.
    return sum((e["amount"] for e in expense_list), 0.0)


# D2 — Category totals with dict comprehension
def get_category_totals_functional(expense_list):
    """
    Build the category → total mapping using a dict comprehension
    and a generator expression (no explicit for-loop).
    """
    # {e["category"] for e in expense_list} = unique names; {cat: sum(...) for cat in that set} = each total.
    unique_categories = {e["category"] for e in expense_list} # Set comprehension 
    return { # Dictionary comprehension
        cat: sum(e["amount"] for e in expense_list if e["category"] == cat)
        for cat in unique_categories
    }


# D3 — Above-average expenses with filter + lambda
def get_above_average_functional(expense_list):
    """
    Return expenses above the average amount.
    Use filter() and a lambda — no explicit for-loop.
    """
    avg = get_average(expense_list)
    # list(filter(lambda e: <condition>, expense_list)) — keeps each dict e where the lambda is True, in original order.
    return list(filter(lambda e: e["amount"] > avg, expense_list))


# D4 — Formatted descriptions with map + lambda
def format_expenses(expense_list):
    """
    Return a list of strings in the format:
    "YYYY-MM-DD | Category | Description | $amount"
    Use map() and a lambda.
    """
    # list(map(lambda e: <one value per row>, expense_list)) — map feeds each e to the lambda; list() gathers all strings.
    return list(
        map(
            lambda e: (
                f"{e['date']} | {e['category']} | {e['description']} | "
                f"${e['amount']:.2f}"
            ),
            expense_list,
        )
    )


if __name__ == "__main__":
    from part_c_procedural import (
        get_total,  # baseline for D1 assert
        get_category_totals,  # baseline for D2 assert
        get_above_average,  # baseline for D3 assert
        expenses,  # sample data for tests and prints
    )

    # assert <condition>, <optional error message> 
    assert round(get_total_functional(expenses), 2) == round(get_total(expenses), 2), (
        "D1 total mismatch"
    )

    assert get_category_totals_functional(expenses) == get_category_totals(
        expenses
    ), "D2 category totals mismatch"

    proc_ids = {id(e) for e in get_above_average(expenses)} # Set comprehension
    func_ids = {id(e) for e in get_above_average_functional(expenses)} # Set comprehension
    assert proc_ids == func_ids, "D3 above-average mismatch"

    print("All assertions passed.")
    print("\nFormatted expenses:")
    for line in format_expenses(expenses):
        print(line)
