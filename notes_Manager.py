import json
import os
import time
# Save notes in a local file (notes.json)
FILENAME = "notes.json"

# Load notes from the file

FILENAME = "notes.json"


# Load notes from the file
def load_notes():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []


# Save notes to the file
def save_notes(notes):
    with open(FILENAME, "w") as file:
        json.dump(notes, file, indent=4)


# Initialize notes list
list1 = load_notes()

# Main loop
while True:
    print("\n=== Notes App ===")
    print("1) New Note")
    print("2) View All Notes")
    print("3) Delete Note")
    print("4) Exit")

    num = input("Pick A Choice (1-4): ")

    if num == "1":
        time.sleep(0.5)
        new_note = input("New Note: ")
        list1.append(new_note)
        save_notes(list1)
        print("✅ Note Added.")
        time.sleep(0.5)

    elif num == "2":
        time.sleep(0.5)
        if list1:
            print("\n📋 All Notes:")
            for i, note in enumerate(list1, 1):
                print(f"{i}) {note}")
        else:
            print("📭 No notes to show.")
        time.sleep(0.5)

    elif num == "3":
        if not list1:
            print("❌ No notes to delete.")
            continue
        print("\n🗑️ Current Notes:")
        for i, note in enumerate(list1, 1):
            print(f"{i}) {note}")
        try:
            delete = int(input("Enter the number of the note to delete: "))
            index = delete - 1
            removed = list1.pop(index)
            save_notes(list1)
            print(f"✅ Deleted: {removed}")
        except (IndexError, ValueError):
            print("⚠️ Invalid input. Try again.")
        time.sleep(0.5)

    elif num == "4":
        print("👋 Exiting... Notes saved.")
        break

    else:
        print("❗ Invalid choice. Try 1-4.")