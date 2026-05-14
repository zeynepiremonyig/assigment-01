## Snippet 1
**Paradigm**: Imperative
**Explanation**: The code tells the computer *what to do, step by step*. It starts `total` at 0, loops through `expenses`, and changes `total` many times with `+=`. There are no helper functions; everything happens in one place. `print` at the end also does an action (shows text), not just a return value.

## Snippet 2
**Paradigm**: Procedural
**Explanation**: The work is split into **functions** with clear names: `get_total` and `get_by_category`. Each function does one job and returns a result. The main code is short: it just **calls** those functions. Putting logic into named steps like this is the procedural style.

## Snippet 3
**Paradigm**: Imperative
**Explanation**: A `for` loop goes through each expense and **updates a dictionary** `totals` line by line. The program keeps changing `totals` while it runs. That “change memory in a loop” idea is imperative. The last line uses `max` and `lambda`, but the big part is still the loop that edits `totals`.

## Snippet 4
**Paradigm**: Functional
**Explanation**: The Food total uses `sum` with a short **generator** inside it, not a loop that changes a variable. The next lines use `map`, `filter`, and `lambda` to build new lists from old data. This style uses **functions on data** instead of writing “change this variable in a for-loop” by hand.
