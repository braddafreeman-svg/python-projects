# Thread Shed Sales Parser

## Overview
A beginner Python data-cleaning project that parses a messy daily sales string, cleans the data, and calculates totals.

The script:
- replaces separators and splits the raw text into transactions
- trims whitespace and extracts customer, sale amount, and thread colours
- calculates total sales for the day
- splits multi-colour purchases (e.g. "white&blue") into individual colours
- counts how many of each thread colour were sold

## Skills Practised
- String methods: `replace()`, `split()`, `strip()`
- Loops and nested loops
- Building lists from cleaned data
- Converting strings to numbers (`float`)
- Simple counting functions

## How to Run
Run the Python file:

```bash
python thread_shed_parser.py

