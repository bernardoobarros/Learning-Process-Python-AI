# PySpend CLI 

A lightweight, local expense tracker built with Python. This project focuses on clean CLI logic, data persistence using JSON, and robust error handling.

## Overview
PySpend allows users to manage their daily finances directly from the terminal. It was designed to practice foundational programming concepts required for Data Science and AI Orchestration.

## Key Learnings
* **Data Persistence:** Implemented `json` serialization to ensure data survives application restarts.
* **Error Handling:** Used `try-except` blocks to manage `FileNotFoundError` and invalid user inputs.
* **State Management:** Managed application state using Python dictionaries and lists.
* **Modular Design:** Separated business logic (CRUD operations) from the execution layer (Launcher script).

## Features
- [x] Add expenses with category and date.
- [x] View full expense history.
- [x] Persistent storage in `expenses.json`.
- [x] Automatic file creation on first run.

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/pyspend.git](https://github.com/your-username/pyspend.git)

2. Navigate to the Folder
   ```bash  
   cd Pyspend

3. Run the aplication
   ```bash
   python run.py
