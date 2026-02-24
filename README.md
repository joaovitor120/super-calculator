## After a long break from Python, I decided to jump back in by building a modern, well-structured calculator that goes beyond the basics. This project serves as both a practical tool and a deliberate exercise in applying clean code principles and core Python concepts in a clean, modular way.

## Built-in Python features & standard library used

This small console application explores and combines several built-in Python capabilities:

- **Dictionaries** as both data structures and function dispatch tables (menu + calculator operations)
- **Lambda functions** for clean, inline math operation definitions
- **f-strings** + `print()` for friendly console output
- **Input validation loops** using `while`, `try/except`, `.strip()`, `.upper()`
- **Exception handling** (`ValueError`, `ZeroDivisionError`)
- **JSON persistence** with the `json` module (load, dump, append logic)
- **Date & time** handling with `datetime` and `strftime`
- **Basic type conversion** (`int`, `float`, `round`)
- **HTTP requests** via `requests` library for real-time currency conversion
- **Program flow control** with `while True`, `break`, `match-case`, `time.sleep`

All of this is done without external frameworks — just Python + one small dependency (`requests`).