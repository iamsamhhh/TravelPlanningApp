def UserInput():
    """Prompt for user input and validate it."""
    valid_inputs = {
        "1": "Create travel plan",
        "2": "Show travel plan list",
        "3": "Open travel plan",
        "4": "Close travel plan",
        "5": "Add activity",
        "6": "Quit"
    }

    print("Please select an option:")
    for key, value in valid_inputs.items():
        print(f"{key}: {value}")

    while True:
        user_input = input("Enter the option number: ").strip()
        if user_input in valid_inputs:
            return valid_inputs[user_input]
        else:
            print("Invalid input. Please enter a valid option number.")

# Example usage
if __name__ == "__main__":
    command = UserInput()
    print(f"You entered: {command}")