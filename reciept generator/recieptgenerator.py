# Reciept Generator Code

# Imports
import random

############################## LISTS TO PULL FROM #############################
# Drinks
drinks = [
    "Iced Coffee",
    "Freshly Brewed Black Tea",
    "Classic Cola",
    "Lemonade",
    "Sparkling Water",
    "Mojito",
    "Strawberry Daiquiri",
    "Cappuccino",
    "Espresso",
    "Mango Lassi",
    "Green Smoothie",
    "Virgin Piña Colada",
    "Orange Juice",
    "Ginger Ale",
    "Iced Green Tea",
    "Cranberry Spritzer",
    "Chocolate Milkshake",
    "Hot Chocolate",
    "Cucumber-Mint Cooler",
    "Pomegranate Martini",
    "Long Island Iced Tea",
    "Blueberry Lemonade",
    "Raspberry Iced Tea",
    "Chai Latte",
    "Mango Iced Tea"
]

# Appetizers
appetizers = [
    "Spinach Artichoke Dip",
    "Bruschetta",
    "Mozzarella Sticks",
    "Shrimp Cocktail",
    "Stuffed Mushrooms",
    "Chicken Wings",
    "Spring Rolls",
    "Fried Calamari",
    "Sliders",
    "Nachos",
    "Garlic Bread",
    "Crispy Onion Rings",
    "Caprese Salad",
    "Dumplings",
    "Potato Skins",
    "Deviled Eggs",
    "Loaded Fries",
    "Bacon-Wrapped Scallops",
    "Mini Tacos",
    "Cheese Platter"
]

# Entrees
entrees = [
    "Grilled Steak",
    "Roast Chicken",
    "Salmon Fillet",
    "Pasta Carbonara",
    "Burger with Fries",
    "Sushi Platter",
    "Chicken Parmesan",
    "Shrimp Scampi",
    "Vegetable Stir-Fry",
    "Beef Stir-Fry",
    "Lobster Tail",
    "Rack of Ribs",
    "Eggplant Parmesan",
    "Seafood Paella",
    "Fettuccine Alfredo",
    "Tandoori Chicken",
    "Filet Mignon",
    "Shrimp and Grits",
    "Vegan Curry",
    "Mushroom Risotto",
    "Pad Thai",
    "Fish and Chips",
    "Taco Platter",
    "Vegetable Lasagna",
    "Grilled Veggie Wrap",
    "Stuffed Bell Peppers",
    "Pork Tenderloin",
    "Gourmet Pizza",
    "BBQ Pulled Pork Sandwich",
    "Steak Fajitas",
    "Chicken Tenders",
    "Sesame Crusted Tuna",
    "Lamb Chops",
    "Spaghetti Bolognese",
    "Grilled Portobello",
    "Sashimi Platter",
    "Cajun Jambalaya",
    "Butter Chicken",
    "Hawaiian Poke Bowl",
    "Pho Noodle Soup",
    "Beef Tacos",
    "Butternut Squash Ravioli",
    "Sautéed Shrimp",
    "Vegan Burger",
    "Chicken Shawarma"
]

# Desserts
deserts = [
    "Chocolate Lava Cake",
    "New York Cheesecake",
    "Tiramisu",
    "Apple Pie",
    "Crème Brûlée",
    "Brownie Sundae",
    "Fruit Parfait",
    "Churros",
    "Red Velvet Cupcake",
    "Panna Cotta",
    "Lemon Sorbet",
    "Key Lime Pie",
    "Caramel Flan",
    "Banana Split",
    "Chocolate Chip Cookies",
    "Molten Chocolate Soufflé",
    "Strawberry Shortcake",
    "Berry Crumble",
    "Ice Cream Sundae",
    "Coconut Macaroon"
]
############################ ^ LISTS TO PULL FROM ^ ###########################

#################### Drinks ####################
#Edit the range for the number of drinks that might populate the reciept (parameter max: 25)
quantity_drinks = random.randint(0, 15)
 #print("Quantity Drinks:", quantity_drinks)

# Generate a list of random integers within the specified range
drink_indexes = random.sample(range(len(drinks)), quantity_drinks)
drink_items = [drinks[i] for i in drink_indexes]
print("Drinks:", drink_items)



#################### Appetizers ####################
#Edit the range for the number of appetizers that might populate the reciept (parameter max: 20)
quantity_appetizers = random.randint(0, 15)
#print("Quantity Appetizers:", quantity_appetizers)

# Generate a list of random integers within the specified range
appetizers_indexes = random.sample(range(len(appetizers)), quantity_appetizers)
appetizer_items = [appetizers[i] for i in appetizers_indexes]
print("Appetizers:", appetizer_items)



#################### Entrees ####################
#Edit the range for the number of entrees that might populate the reciept (parameter max: 45)
quantity_entrees = random.randint(0, 15)
#print("Quantity Entrees:", quantity_entrees)

# Generate a list of random integers within the specified range
entree_indexes = random.sample(range(len(entrees)), quantity_entrees)
entree_items = [entrees[i] for i in entree_indexes]
print("Entrees:", entree_items)



#################### Deserts ####################
#Edit the range for the number of deserts that might populate the reciept (parameter max: 20)
quantity_deserts = random.randint(0, 15)
#print("Quantity Deserts:", quantity_deserts)

# Generate a list of random integers within the specified range
desert_indexes = random.sample(range(len(deserts)), quantity_deserts)
desert_itmes = [deserts[i] for i in desert_indexes]
print("Desert:", desert_itmes)

#################### Prices / Sub Total ####################
total_items = drink_items + appetizer_items + entree_items + desert_itmes
prices = [] 
subtotal = 0
for i in range(len(total_items)):
        temp_price = round(random.uniform(0,100), 2)
        subtotal += temp_price
        prices.append(temp_price)        
print("Prices:", prices )
round(subtotal,2)
print("Sub Total: ", subtotal)


#################### Tax / Tip / Total ####################
tax_percent = round(random.uniform(.05,.10), 2)
tax = round(tax_percent*subtotal , 2)
print("Tax: ", tax)

tip_percent = round(random.uniform(0,.25), 2)
tip = round(tip_percent*subtotal , 2)
print("Tip: ", tip)

total = round(subtotal + tip + tax, 2)
print("Total: ", total)

################ reciept printing --> to doc ################


