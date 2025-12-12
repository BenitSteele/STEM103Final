import pandas as pd # Grabbing the PANDAS library for DataFrame creation
def price_list(): # Function to create a DataFrame of purchased items and their costs
    data = [] # Empty list to store item data
    num_items_bought = int(input("Enter number of item(s) purchased: "))
    repeat_program = True
    while repeat_program: # Loop to allow multiple entries
        for _ in range(num_items_bought): # Loop for the number of items purchased
            bought_item = input("Enter item purchased: ") # User input for item name
            cost = float(input("Enter cost of item: ")) # User input for item cost
            data.append([bought_item, cost]) # Append item and cost to data list
            df_bought = pd.DataFrame(data, columns=['bought_item', 'cost'])
            print("\nFinal DataFrame:")
            print(df_bought) # Display the DataFrame
        responce = input("\nWould you like to continue? (Y/N): ")
        if responce == "Y": # If user wants to continue
            num_items_bought = int(input("Enter number of item(s) purchased: "))
        else: # If user wants to stop
            repeat_program = False
            print("Bye!")
        