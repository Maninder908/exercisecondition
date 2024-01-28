def check_zander_size():
    size_limit = 42  # Size limit for a zander in centimeters

    # Get the length of the zander from the user
    try:
        zander_length = float(input("Enter the length of the zander in centimeters: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")
        return

    # Check if the zander meets the size limit
    if zander_length >= size_limit:
        print("Congratulations! The zander is of legal size.")
    else:
        size_difference = size_limit - zander_length
        print(f"Please release the zander back into the lake. It is {size_difference:.2f} centimeters below the size limit.")

# Call the function to check the zander size
check_zander_size()

