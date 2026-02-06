import json

# Load data at the start of the program
try:
    with open("school_data.json", "r") as file:
        data = json.load(file)
        # Using .get() to avoid errors if the keys don't exist
        lessons = data.get("lessons", {})
        absenteeism = data.get("absenteeism", 0)
except (FileNotFoundError, json.JSONDecodeError):
    lessons = {}
    absenteeism = 0

def save_data():
    """Saves all current data to a JSON file."""
    all_data = {
        "lessons": lessons,
        "absenteeism": absenteeism
    }
    with open("school_data.json", "w") as file:
        json.dump(all_data, file, indent=4)
    print("\n--- Data successfully saved! ---")

def add_lesson():
    """Adds new lessons to the dictionary."""
    while True:
        new_lesson = input("Enter the name of the lesson to add: ").strip()
        if new_lesson:
            if new_lesson not in lessons:
                lessons[new_lesson] = []
                print(f"New lesson added: {new_lesson}")
            else:
                print("This lesson already exists!")
        
        choice = input("Do you want to add another lesson? (y/n): ").lower()
        if choice == "n":
            break

def add_score():
    """Adds scores to an existing lesson."""
    while True:
        lesson_choice = input("Which lesson do you want to add a score to? (q to quit): ").strip()
        
        if lesson_choice.lower() == "q":
            break
            
        if lesson_choice in lessons:
            while True:
                try:
                    score = int(input(f"Enter the score for {lesson_choice}: "))
                    lessons[lesson_choice].append(score)
                    print(f"Score added: {score}")
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
                    continue
                
                choice = input("Add another score for this lesson? (y/n): ").lower()
                if choice == "n":
                    break
            break
        else:
            print(f"Error: '{lesson_choice}' does not exist.")

def remove_lesson():
    """Removes a lesson from the system."""
    lesson_to_remove = input("Which lesson do you want to remove?: ").strip()
    if lessons.pop(lesson_to_remove, None) is not None:
        print(f"Lesson removed: {lesson_to_remove}")
    else:
        print(f"Error: Lesson '{lesson_to_remove}' not found.")

def calculate_stats():
    """Calculates and displays averages for all lessons."""
    if not lessons:
        print("No data available to display statistics.")
        return

    total_averages = 0
    lesson_count = 0
    
    print("\n--- ACADEMIC PERFORMANCE ---")
    for lesson, scores in lessons.items():
        if scores:
            avg = sum(scores) / len(scores)
            print(f"{lesson}: {avg:.2f}")
            total_averages += avg
            lesson_count += 1
        else:
            print(f"{lesson}: No scores recorded yet.")

    if lesson_count > 0:
        overall_avg = total_averages / lesson_count
        print(f"\nOVERALL GPA: {overall_avg:.2f}")
    else:
        print("\nCould not calculate GPA (no scores found).")

# Main Application Loop
while True:
    print("\n" + "="*25)
    print(" SCHOOL PLANNING SYSTEM ")
    print("="*25)
    print("0: Exit & Save\n"
          "1: Add New Lesson\n"
          "2: Remove a Lesson\n"
          "3: Add a New Score\n"
          "4: Record Absenteeism (+1)\n"
          "5: Show Statistics")
    
    try:
        choice = int(input("\nSelect an option: "))
    except ValueError:
        print("Please enter a valid number (0-5).")
        continue

    if choice == 1:
        add_lesson()
    elif choice == 2:
        if not lessons:
            print("Your list is empty.")
        else:
            remove_lesson()
    elif choice == 3:
        add_score()
    elif choice == 4:
        absenteeism += 1
        print(f"Absenteeism recorded. Current count: {absenteeism}")
    elif choice == 5:
        print("\n" + "\\" + "-"*10 + " STATS " + "-"*10 + "/")
        calculate_stats()
        print(f"Total Absenteeism: {absenteeism}")
        print("-" * 27)
    elif choice == 0:
        save_data()
        print("Goodbye!")
        break
