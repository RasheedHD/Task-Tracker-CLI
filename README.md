# Task Tracker CLI

A simple command‑line task management application written in Python. It allows you to create, update, delete, and track tasks with persistent storage using a JSON file.

This project focuses on clarity, minimal dependencies, and learning‑friendly code rather than complex frameworks.

---

## Features

* Add tasks with automatic ID assignment
* Mark tasks as **todo**, **in‑progress**, or **done**
* Update task descriptions
* Delete tasks
* Filter tasks by status
* Persistent storage (tasks are saved between runs)
* Clean table output for readability

---

## Project Structure

```
.
├── main.py       # Main application logic and CLI loop
└── tasks.json    # Persistent storage (must exist, can be empty)
```

> `tasks.json` should exist before running the program. It can be an empty file.

---

## Requirements

* Python 3.9+
* No external libraries required (uses only standard library)

---

## Running the App

From the project directory:

```bash
python main.py
```

You will enter an interactive CLI prompt:

```
>
```

The program continues running until `exit` is entered.

---

## Commands

### 1. Add a Task

```
add "<description>"
```

Example:

```
add "Finish software engineering assignment"
add "Prepare presentation slides"
```

Output:

```
Task added successfully (ID: 1)
```

---

### 2. List Tasks

```
list
list all
list todo
list in-progress
list done
```

Examples:

```
list
list done
list in-progress
```

---

### 3. Delete a Task

```
delete <task_id>
```

Example:

```
delete 3
```

---

### 4. Update Task Description

```
update <task_id> <new_description>
```

Example:

```
update 2 Revise database schema
update 2 "Revise database schema properly"
```

---

### 5. Change Task Status

Mark as in progress:

```
mark-in-progress <task_id>
```

Mark as done:

```
mark-done <task_id>
```

Examples:

```
mark-in-progress 1
mark-done 1
```

---

### 6. Exit Program

```
exit
```

All tasks are saved automatically before exiting.

---

## Task Status Flow

```
todo -> in-progress -> done
```

You can directly mark a todo task as done if desired.

---

## Data Storage Format

Tasks are stored in `tasks.json` as a list of JSON strings.

Example structure:

```json
[
  "{\"id\": 1, \"description\": \"Study algorithms\", \"status\": \"todo\", \"createdAt\": \"2026-02-19 15:42\", \"updatedAt\": \"N/A\"}"
]
```

Each task contains:

| Field       | Description               |
| ----------- | ------------------------- |
| id          | Unique task identifier    |
| description | Task text                 |
| status      | todo / in-progress / done |
| createdAt   | Creation timestamp        |
| updatedAt   | Last update timestamp     |

---

## Error Handling

The program handles common user mistakes:

| Error               | Message                                                           |
| ------------------- | ----------------------------------------------------------------- |
| Missing arguments   | `Error: Command takes more inputs!`                               |
| Invalid ID          | `Error: ID should be a number!`                                   |
| Task not found      | `Error: Task with given ID does not exist!`                       |
| Invalid list filter | `Error: list accepts optional arguments: (done/todo/in-progress)` |
| Unknown command     | `Invalid input!`                                                  |

---

## Limitations

* No multi‑user support
* No task priority or due dates
* JSON storage not optimized for very large datasets
* No undo functionality

---

## Possible Improvements

Ideas for future development:

* Add due dates and reminders
* Add priorities (low / medium / high)
* Colored terminal output
* Search command
* Export to CSV
* Packaging as a pip module
* Argument‑based mode (non‑interactive CLI usage)

---

## Educational Purpose

This project is intentionally simple and readable. It is suitable for beginners learning:

* Classes and objects
* File persistence
* JSON serialization
* Command parsing
* Error handling

The original project idea can be found at https://roadmap.sh/projects/task-tracker

---

## License

You may freely use, modify, and distribute this project for educational purposes.



