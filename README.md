# Python Projects

A structured series of Python projects, building up core programming skills one project at a time — from basic scripts to object-oriented programs with persistent storage and external API integration.

## Table of Contents

- [About](#about)
- [Projects](#projects)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [What This Series Covers](#what-this-series-covers)
- [Author](#author)

## About

Each project in this repository focuses on a specific set of Python concepts, progressing from basic scripts to menu-driven applications with file storage, error handling, and object-oriented design. Every project is self-contained and can be run independently.

## Projects

### 1. Calculator (`calculator.py`)

A basic command-line calculator supporting core arithmetic operations. The first project in the series — focused on functions, user input, and conditional logic.

### 2. Number Guessing Game (`guessing_game.py`)

A simple interactive game where the user tries to guess a randomly generated number. Introduces loops, random number generation, and win/lose conditions.

### 3. Password Generator (`password_generator.py`)

Generates secure random passwords based on user-defined criteria (length, character types). Later updated with a save feature, so generated passwords can be stored and retrieved.

### 4. To-Do List App (`To-do-list.py`)

A menu-driven to-do list application with full CRUD functionality (add, view, complete, delete tasks). Uses JSON storage, so tasks persist between sessions.

### 5. Weather CLI App (`Weather-app/`)

A command-line weather app that fetches live weather data from [WeatherAPI.com](https://www.weatherapi.com/). Includes a search history feature, so previously searched locations are saved and can be revisited.

### 6. Student Grade Tracker (`Student-Grade-Tracker.py`)

A menu-driven grade tracker for recording and managing student grades, with JSON storage so records persist between sessions.

### 7. Bank Account System (`bank.py`)

A menu-driven bank account system built around an `Account` class — the first project in the series to use object-oriented programming. Supports creating accounts, deposits, withdrawals (with an insufficient-funds check), balance checks, and per-account transaction history. Accounts are saved to and loaded from JSON, and user input is validated so invalid entries (non-numbers, negative amounts) don't crash the program.

## Tech Stack

- **Language:** Python 3
- **Storage:** JSON file persistence
- **External API:** WeatherAPI.com (Weather CLI App)
- **Tools:** VS Code, Git & GitHub

## Getting Started

Clone the repository:

\`\`\`bash
git clone https://github.com/rolandzacx-eng/python-projects.git
cd python-projects
\`\`\`

Run any project with Python 3:

\`\`\`bash
python bank.py
\`\`\`

Some projects (like the Weather CLI App) may require an API key — check the project's own folder for setup details.

## What This Series Covers

- Core syntax: variables, conditionals, loops, functions
- Working with user input and formatted output (f-strings)
- File I/O and persistent storage using JSON
- Error handling with \`try\`/\`except\`
- Working with external APIs
- Building interactive, menu-driven command-line programs
- Object-oriented programming: classes, \`self\`, methods, and instances

More projects are added as the series continues.

## Author

**Roland Emma Watega**
[@rolandzacx-eng](https://github.com/rolandzacx-eng)
