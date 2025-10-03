# Copilot Instructions for CSF_101sonia

## Project Overview
This repository contains practical exercises for a foundational computer science course. The codebase is organized by practicals, each focusing on a core concept (e.g., data types, control structures, data structures, algorithms).

## Directory Structure & Key Files
- `practical_1/`: Basics (booleans, numbers, strings, control structures, data structures, functions, operators)
- `practical_2/`: Fibonacci algorithms (iterative, recursive)
- `practical_3/`: Stack and queue implementations
- `practical_4/`: Linked list algorithms
- `practical_5/`: Binary search tree implementation
- Each practical contains a `reflection.md` for student notes and learning reflections.

## Coding Patterns & Conventions
- Each concept is isolated in its own file (e.g., `lists.py`, `dictionaries.py`, `recursion.py`).
- Use clear, descriptive function and variable names that reflect the concept being taught.
- Avoid unnecessary abstraction; keep code readable and focused on the learning objective.
- Reflection files (`reflection.md`) are for markdown notes, not code.
- No external dependencies are used; all code is standard Python 3.

## Developer Workflows
- No build system or test framework is present; code is run directly as Python scripts.
- To run a file: `python practical_X/<subfolder>/<filename>.py` (adjust path as needed).
- Debug by adding print statements or using Python's built-in debugging tools.

## Integration & Data Flow
- Files are independent; there is no cross-file or cross-practical integration.
- Each file demonstrates a single concept or data structure in isolation.

## Examples
- For a binary search tree, see `practical_5/binary_search_tree.py`.
- For recursion, see `practical_1/functtions_and_scope/recursion.py` and `practical_2/recursive_fibonacci.py`.
- For stack/queue, see `practical_3/stack.py` and `practical_3/queue.py`.

## Special Notes
- Follow the file organization strictly; new concepts should be added in the appropriate practical folder.
- Do not introduce external libraries or frameworks.
- Keep code and markdown files separate.

---
If any section is unclear or missing, please provide feedback for further refinement.
