# Define the knowledge base (rules and facts)
knowledge_base = {
    "issue_type": {
        "1": "Software",
        "2": "Hardware",
    },
    "software_issue": {
        "1": "Operating System",
        "2": "Software Application",
    },
    "hardware_issue": {
        "1": "Computer",
        "2": "Printer",
    },
    "os_issue": {
        "1": "Windows",
        "2": "Linux",
    },
    "os_solution": {
        "1": "Reinstall Windows",
        "2": "Check for updates",
    },
    "app_solution": {
        "1": "Reinstall the application",
        "2": "Update the application",
    },
    "computer_solution": {
        "1": "Check for loose cables",
        "2": "Run hardware diagnostics",
    },
    "printer_solution": {
        "1": "Check paper and ink levels",
        "2": "Reinstall printer drivers",
    },
}

# Function to display options and get user input
def get_user_input(options):
    for key, value in options.items():
        print(f"{key}. {value}")
    choice = input("Select an option: ")
    return choice

# Main help desk management expert system
print("Welcome to the Help Desk Management Expert System!")

while True:
    print("\nSelect the type of issue:")
    issue_type_choice = get_user_input(knowledge_base["issue_type"])
    
    if issue_type_choice == '1':
        print("\nSelect the software issue:")
        software_issue_choice = get_user_input(knowledge_base["software_issue"])
        if software_issue_choice == '1':
            os_issue_choice = get_user_input(knowledge_base["os_issue"])
            print(f"\nSolution: {knowledge_base['os_solution'][os_issue_choice]}")
        elif software_issue_choice == '2':
            app_issue_choice = get_user_input(knowledge_base["app_solution"])
            print(f"\nSolution: {knowledge_base['app_solution'][app_issue_choice]}")
    elif issue_type_choice == '2':
        print("\nSelect the hardware issue:")
        hardware_issue_choice = get_user_input(knowledge_base["hardware_issue"])
        if hardware_issue_choice == '1':
            computer_issue_choice = get_user_input(knowledge_base["computer_solution"])
            print(f"\nSolution: {knowledge_base['computer_solution'][computer_issue_choice]}")
        elif hardware_issue_choice == '2':
            printer_issue_choice = get_user_input(knowledge_base["printer_solution"])
            print(f"\nSolution: {knowledge_base['printer_solution'][printer_issue_choice]}")
    else:
        print("Invalid choice. Please select a valid issue type.")
    
    another_issue = input("Do you have another issue? (yes/no): ")
    if another_issue.lower() != 'yes':
        break

print("Thank you for using the Help Desk Management Expert System!")
