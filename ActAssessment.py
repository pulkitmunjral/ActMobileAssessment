import json

# Loading the file in json format
file = open('input.json')
json_data = json.load(file)
products = {}

# Iterating over the json data to store it in pattern: prod >> country >> sales (sum of price)
for data in json_data['sales']:
    product = data['prod']

    # Checking if product is already present in Products dictionary.
    if product in products.keys():

        # Checking if country is present products.product dictionary.
        if data['country'] in products[product].keys():

            # Adding the price of product sold by the country into there total sales,
            products[product][data['country']] += int(data['price'])

        # Adding country name to products.product dictionary if country is not already present
        else:
            products[product][data['country']] = int(data['price'])

    # Adding product to products dictionary if product is not already present.
    else:
        products[product] = {data['country']: int(data['price'])}


while True:
    # Taking input product name from the user till user don't want to exit.
    user_input_product = input("Please enter the name of the product or enter 'Y' to exit: ")

    # Exit condition for the while loop.
    if user_input_product == 'Y':
        print("Thanks for visiting.")
        break

    # If the user selected product is present in our products dictionary.
    if user_input_product in products.keys():

        # Storing list of country where the user selected product was sold.
        Country_list = list(products[user_input_product].keys())

        # Storing list of sales as per the country for the user selected product.
        Sales_list = list(products[user_input_product].values())

        # Storing the maximum sales of the user selected product
        max_sales = max(Sales_list)

        # Getting the name of the country with maximum sales for the user selected product
        Country = Country_list[Sales_list.index(max_sales)]

        # Printing the country name with maximum sales for user selected product.
        print(f"\nProduct '{user_input_product}' had it's maximum sales of {max_sales}$ in ==> {Country}.\n\n")

    # If the user selected product is not present in our products dictionary we ask user to try again.
    else:
        print(f"Product '{user_input_product}' is not present in our database. Please try again.")
