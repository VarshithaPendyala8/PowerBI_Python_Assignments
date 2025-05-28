inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]


# calculate the TotalRevenue
totalRevenue = 0
for i in range(len(inventory)):
    totalRevenue += (inventory[i][2] * inventory[i][3])
print("TotalRevenue:", totalRevenue)

# List Low stock item if stock is less than 5
for i in range(len(inventory)):
    if inventory[i][4] < 5:
        print('Low stock Item:', inventory[i][0])

# calculte the categorywaise Revenue
for name, category, unitprice, unitsSold, unitsLeft in inventory:
    revenue = unitprice * unitsSold
    print('Categorywise Revenue:',revenue)



