import pandas as pd
def price_list():
    data = []
    num_items_bought = int(input("Enter number of item(s) purchased: "))
    repeat_program = True
    while repeat_program:
        for _ in range(num_items_bought):
            bought_item = input("Enter item purchased: ")
            cost = float(input("Enter cost of item: "))
            data.append([bought_item, cost])
            df_bought = pd.DataFrame(data, columns=['bought_item', 'cost'])
            print("\nFinal DataFrame:")
            print(df_bought)
        responce = input("\nWould you like to continue? (Y/N): ")
        if responce == "Y":
            num_items_bought = int(input("Enter number of item(s) purchased: "))
        else:
            repeat_program = False
            print("Bye!")
        