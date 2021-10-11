
import mysql.connector
from faker import Faker
import random

conn = mysql.connector.connect(host="localhost", user="root", password="", database="naa_sales")

crs = conn.cursor(dictionary=True)

def populateProductsTable():

    crs.execute("set foreign_key_checks=0")
    crs.execute("truncate table products")

    words = [
        "Lavaş", "Təndir", "Zavod Çörəyi",  
        "Apple", "Banana", "Orange", "Grapes", "Pineapple", "Watermelon", "Lettuce", "Tomato", "Carrot", "Broccoli",
        "Milk", "Cheese", "Yogurt", "Butter", "Eggs", "Chicken", "Beef", "Pork", "Fish", "Shrimp",
        "Bread", "Bagel", "Croissant", "Muffin", "Donut", "Pasta", "Rice", "Quinoa", "Oats", "Cereal",
        "Soup", "Beans", "Tuna", "Vegetables", "Fruits", "Tomato Sauce", "Salsa", "Peanut Butter", "Jam", "Honey",
        "Chips", "Cookies", "Crackers", "Chocolate", "Popcorn", "Nuts", "Juice", "Soda", "Tea", "Coffee",
        "Ice Cream", "Frozen Vegetables", "Frozen Pizza", "Frozen Dinners", "Frozen Fruit", "Frozen Desserts",
        "Ketchup", "Mustard", "Mayonnaise", "Soy Sauce", "Vinegar", "Salad Dressing", "BBQ Sauce", "Hot Sauce", "Maple Syrup", "Worcestershire Sauce",
        "Shampoo", "Soap", "Toothpaste", "Deodorant", "Toilet Paper", "Paper Towels", "Laundry Detergent", "Dish Soap", "Cleaning Supplies",
        "Diapers", "Baby Food", "Baby Wipes", "Baby Lotion", "Baby Shampoo", "Baby Powder", "Baby Oil", "Baby Diaper Rash Cream",
        "Dog Food", "Cat Food", "Pet Treats", "Pet Toys", "Pet Shampoo", "Pet Litter", "Bird Seed", "Fish Food", "Pet Bed"
    ]

    for w in words:
        sql = 'insert into products (name, quantity, price) values  (%s, %s, %s)'
        crs.execute(sql, (w, random.randint(1, 50), round(random.uniform(0.1, 100),2)))

    conn.commit()

    crs.execute("select count(*) from products")
    rows = crs.fetchall()
    for row in rows:
        print(row)
        

def generateReceipt():
    crs.execute("insert into receipts (created_at) values (now())")
    receiptId = crs.lastrowid
    
    numberOfProductsToBuy = random.randint(2, 10)
    
    sql = f"select * from products where quantity > 0 order by rand() limit {numberOfProductsToBuy}"
    crs.execute(sql)
    
    for row in crs.fetchall():
        quantityToBuy = round(random.uniform(0.1, row['quantity']), 2)
        productId = row['id']
        sql = f'''insert into receipt_details(receipt_id, product_id, quantity) 
                  values (%s, %s, %s)'''
        crs.execute(sql, (receiptId, productId, quantityToBuy))
        
    conn.commit()

generateReceipt()

