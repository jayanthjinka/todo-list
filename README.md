# To-Do List Application

A simple command-line to-do list application built with Python.

## Features

- Add tasks
- View tasks
- Mark tasks as completed
- Validate empty task descriptions
- Validate invalid menu choices
- Validate invalid and non-numeric task numbers
- Exit the application cleanly

## Requirements

- Python 3.x
- No external dependencies

## How to Run

From the project directory:

```text
python3 todo.py
```

## Usage

When the application starts, it displays a menu with four options:

1. Add a task
2. View tasks
3. Mark a task as completed
4. Exit

Select an option by entering its corresponding number.

For example, selecting `1` allows you to enter a new task. Selecting `2` displays all existing tasks and their current status.

## Data Storage

Tasks are stored in an in-memory Python list using dictionaries.
Each task contains a description and a completion status.
Tasks are not persisted after the application exits.

## Project Structure

```text
todo-list/
├── todo.py
└── README.md
```
