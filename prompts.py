import json
from typing import List, Dict, Optional, TypedDict

PROMPT_FILE = "llm_prompts.json"

class Prompt(TypedDict):
    name: str
    text: str
    level: str  # target length
    goal: str  

# Initialize an in-memory list to store prompts
prompts_db: List[Prompt] = []

def save_prompts():
    """Saves the current list of prompts to a JSON file."""
    try:
        with open(PROMPT_FILE, "w") as f:
            json.dump(prompts_db, f, indent=4)
        print(f"💾 Prompts saved to {PROMPT_FILE}")
    except IOError as e:
        print(f"Error saving prompts: {e}")

def load_prompts():
    """Loads prompts from a JSON file into memory."""
    global prompts_db
    try:
        with open(PROMPT_FILE, "r") as f:
            prompts_db = json.load(f)
        print(f"📚 Prompts loaded from {PROMPT_FILE}")
    except FileNotFoundError:
        print(f"No existing prompt file found at {PROMPT_FILE}. Starting with an empty database.")
        prompts_db = []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {PROMPT_FILE}. Starting with an empty database.")
        prompts_db = []
    except IOError as e:
        print(f"Error loading prompts: {e}")
        prompts_db = []


def add_prompt():
    """Adds a new prompt to the database."""
    print("\n--- Add New Prompt ---")
    name = input("Enter a unique name for this prompt: ").strip()
    if any(p['name'] == name for p in prompts_db):
        print(f"⚠️ Error: A prompt with the name '{name}' already exists.")
        return

    text = input("Enter the full prompt text:\n").strip()
    level = input("Enter the summarization level").strip()
    goal = input("Enter the goal of this prompt: ").strip()

    if not all([name, text, level, goal]):
        print("⚠️ Error: All fields (name, text, level, goal) are required.")
        return

    new_prompt: Prompt = {"name": name, "text": text, "level": level, "goal": goal}
    prompts_db.append(new_prompt)
    save_prompts()
    print(f"✅ Prompt '{name}' added successfully!")

def view_prompts(filtered_prompts: Optional[List[Prompt]] = None):
    """Displays prompts. If filtered_prompts is provided, displays those, otherwise all."""
    print("\n--- Prompts ---")
    display_list = filtered_prompts if filtered_prompts is not None else prompts_db

    if not display_list:
        if filtered_prompts is not None:
            print("No prompts match your criteria.")
        else:
            print("No prompts stored yet. Try adding some!")
        return

    for i, prompt in enumerate(display_list):
        print(f"\n{i+1}. Name: {prompt['name']}")
        print(f"   Level: {prompt['level']}")
        print(f"   Goal: {prompt['goal']}")
        print(f"   Text: \"{prompt['text'][:100]}{'...' if len(prompt['text']) > 100 else ''}\"") # Preview
    print("-" * 15)

def find_prompts():
    """Finds prompts based on level and/or goal."""
    print("\n--- Find Prompts ---")
    search_level = input("Enter summarization level to filter by (or press Enter to skip): ").strip().lower()
    search_goal = input("Enter goal to filter by (or press Enter to skip): ").strip().lower()

    if not search_level and not search_goal:
        print("No search criteria entered. Displaying all prompts.")
        view_prompts()
        return

    results: List[Prompt] = []
    for prompt in prompts_db:
        match_level = True
        match_goal = True

        if search_level and search_level not in prompt['level'].lower():
            match_level = False
        if search_goal and search_goal not in prompt['goal'].lower():
            match_goal = False

        if match_level and match_goal:
            results.append(prompt)

    if results:
        print(f"\nFound {len(results)} prompt(s):")
        view_prompts(results)
    else:
        print("No prompts found matching your criteria.")

def delete_prompt():
    """Deletes a prompt by its name."""
    print("\n--- Delete Prompt ---")
    if not prompts_db:
        print("No prompts to delete.")
        return

    view_prompts()
    name_to_delete = input("Enter the exact name of the prompt to delete: ").strip()

    initial_len = len(prompts_db)
    # Use a list comprehension to create a new list excluding the item to delete
    # This is safer than modifying the list while iterating
    new_prompts_db = [p for p in prompts_db if p['name'] != name_to_delete]

    if len(new_prompts_db) < initial_len:
        prompts_db[:] = new_prompts_db # Update the global list
        save_prompts()
        print(f"🗑️ Prompt '{name_to_delete}' deleted successfully.")
    else:
        print(f"⚠️ Prompt with name '{name_to_delete}' not found.")


def get_prompt_text():
    """Allows user to select a prompt and get its full text for copying."""
    print("\n--- Get Prompt Text ---")
    if not prompts_db:
        print("No prompts available to select.")
        return

    view_prompts()
    try:
        choice = int(input("Enter the number of the prompt to get its full text: ")) -1
        if 0 <= choice < len(prompts_db):
            selected_prompt = prompts_db[choice]
            print(f"\n--- Full Text for '{selected_prompt['name']}' ---")
            print(selected_prompt['text'])
            print("--- End of Prompt Text ---")
            # In a real application, you might copy this to the clipboard.
            # For a CLI, just printing is usually sufficient.
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main_menu():
    """Displays the main menu and handles user input."""
    load_prompts() # Load prompts at startup

    while True:
        print("\n🤖 LLM Prompt Manager 🤖")
        print("1. Add New Prompt")
        print("2. View All Prompts")
        print("3. Find Prompts (by Level/Goal)")
        print("4. Get Full Prompt Text")
        print("5. Delete Prompt")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_prompt()
        elif choice == '2':
            view_prompts()
        elif choice == '3':
            find_prompts()
        elif choice == '4':
            get_prompt_text()
        elif choice == '5':
            delete_prompt()
        elif choice == '6':
            print("👋 Exiting Prompt Manager. Your prompts are saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()