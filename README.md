# Expense Tracker (Programming Paradigms)

## What this project does

This is a small **Expense Tracker** project. All parts use the same sample list of expenses. Each expense has a date, a category, an amount, and a description.

The programs print useful numbers:

- Total money spent and how many records there are
- Totals for each category (category names are shown in **A–Z** order)
- The **most expensive** and **least expensive** single expense (Part B does this without using `max` / `min` on the whole list)
- The **average** amount and every expense that is **strictly above** that average

**Part A** is a short text file (`part_a_paradigms.md`). You read small code snippets and say which programming style they show.

**Parts B, C, and D** solve the same reporting task in three different styles: **imperative**, **procedural**, and **functional**. That makes it easy to compare how the code looks and how hard it is to follow.

## How to run each part

First, open a terminal and go to the project folder (the folder with the `.py` files).

1. **Part A** — Open `part_a_paradigms.md` in your editor. You do not run Python for this part.
2. **Part B** — `python3 part_b_imperative.py`
3. **Part C** — `python3 part_c_procedural.py`
4. **Part D** — `python3 part_d_functional.py` (this file uses some functions from Part C, checks results with `assert`, then prints formatted lines)

### Sample run (Part B)

```text
$ python3 part_b_imperative.py
Total expenses: 476.44
Number of records: 12

Category breakdown:
  Entertainment : 99.99
  Food : 144.45
  Transport : 67.00
  Utilities : 165.00

Most expensive : Electricity bill (Utilities) — 120.00
Least expensive: Coffee & snack (Food) — 8.75

Average expense: 39.70
Expenses above average:
  - Groceries (42.50)
  - Concert ticket (60.00)
  - Electricity bill (120.00)
  - Restaurant dinner (55.20)
  - Internet bill (45.00)
```

Part C prints the **same** summary text as Part B. Part D first prints `All assertions passed.` Then it prints one line per expense like this: `date | category | description | $amount`.

## Paradigm comparison

### Imperative (`part_b_imperative.py`)

**What was easy?** I could write the steps in order: loops, counters, and `print` statements. I did not need to plan extra files or many function names first.

**What was hard?** When everything stays in one long script, it is harder to read. The manual bubble sort for category names also adds many small lines.

**100,000 records:** The code would **still work** if the computer has enough memory to hold the list. The loops are simple. But the file would feel even longer, so **readability** would get worse.

**If I started again:** I would add clear comments between Part B tasks (B1, B2, B3, B4) so the structure is easy to see at a glance.

### Procedural (`part_c_procedural.py`)

**What was easy?** Small functions with clear names (`get_total`, `get_count`, `print_summary`, and so on). When I need the average, I reuse work I already wrote.

**What was hard?** More typing at the start: docstrings, function names, and making sure the printed output matches Part B exactly.

**100,000 records:** Same idea as Part B: it should **still work** in memory for a big list. I think this style stays **easier to read** than Part B because each function does one job.

**If I started again:** I would run Part B and Part C side by side once in a while while coding, so small output mistakes are caught early.

### Functional (`part_d_functional.py`)

**What was easy?** Some tasks become short one-line ideas, like `sum(...)` for the total, `filter` + `lambda` for “above average,” and `map` + `lambda` for formatted strings.

**What was hard?** Part D still imports `get_average` from Part C so the numbers match. That mixes styles. The dict comprehension for category totals also walks the list more than once (once per category), which can be harder to explain to a beginner.

**100,000 records:** It should **still run** for a normal number of categories. If there were **many** categories, the category-total part could become **slower** than building one dictionary in a single loop. Short pipelines are clear; **nested** comprehensions can be harder to read when they grow.

**If I started again:** If the assignment allowed it, I would try to keep Part D more “pure functional” (for example, compute the average inside Part D too) so the style feels more consistent.
