# Notes-Manager
A command-line notes application in Python that allows you to add, view, and delete notes saved locally in a JSON file (notes.json).

## Features
- Add new notes

- View all saved notes

- Delete notes by selecting their number

- Persistent storage using a local JSON file

How to Use:
1. Run the script:
2. Menu Options:
1) New Note: Enter a new note to save.

2) View All Notes: Display all saved notes.

3) Delete Note: Delete a specific note by entering its number.

4) Exit: Save and exit the app.

## Files
- notes.json: Automatically created file where notes are stored in JSON format.

- notes_app.py: The Python script for the notes application.

Requirements
- Python 3

- No external dependencies are needed.

How It Works:
- Notes are loaded from notes.json at startup.

- New notes are appended to the list and saved immediately.

- Deletion removes the selected note and updates the file.

- The app runs in a loop until the user chooses to exit.

Example Usage:
~~~
=== Notes App ===
1) New Note
2) View All Notes
3) Delete Note
4) Exit
Pick A Choice (1-4): 1
New Note: Buy groceries
✅ Note Added.

=== Notes App ===
1) New Note
2) View All Notes
3) Delete Note
4) Exit
Pick A Choice (1-4): 2

📋 All Notes:
1) Buy groceries
~~~
