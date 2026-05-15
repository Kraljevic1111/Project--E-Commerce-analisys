import pandas as pd 

orders = [
    {"order_id": 1, "customer": "Ana", "category": "Shoes", "price": 120, "quantity": 1, "date": "2024-01-05"},
    {"order_id": 2, "customer": "Marko", "category": "T-Shirts", "price": 30, "quantity": 2, "date": "2024-01-10"},
    {"order_id": 3, "customer": "Ana", "category": "Shoes", "price": 150, "quantity": 1, "date": "2024-02-01"},
    {"order_id": 4, "customer": "Jelena", "category": "Jackets", "price": 200, "quantity": 1, "date": "2024-02-15"},
    {"order_id": 5, "customer": "Petar", "category": "T-Shirts", "price": 25, "quantity": 3, "date": "2024-03-01"},
    {"order_id": 6, "customer": "Marko", "category": "Shoes", "price": 100, "quantity": 1, "date": "2024-03-10"},
    {"order_id": 7, "customer": "Ana", "category": "Jackets", "price": 220, "quantity": 1, "date": "2024-03-20"},
]

df = pd.DataFrame(orders)

df['revenue'] = df['price'] * df['quantity']
print(df)

#kovertovanje kolone date u datetime

df['date'] = pd.to_datetime(df['date'])

total_revenue = df['revenue'].sum()
print("Total revenue:",total_revenue)

#top 3 lupca po potrosnji 

top_3_customers_by_revenue = df.groupby('customer')['revenue'].sum().sort_values(ascending = False).head(3)
print('Top three customers:',top_3_customers_by_revenue)

# ukupan prihod po kategoriji 

total_revenue_by_category = df.groupby('category')['revenue'].sum()
print('Total revenue per category:',total_revenue_by_category)

#mesec sa najvecim prihodom

df['date'] = pd.to_datetime(df['date'])
df['month']= df['date'].dt.month

best_month = df.groupby('date')['revenue'].sum().idxmax()
print(best_month)

#kategorija koja donosi najvise novca 

best_category = total_revenue_by_category.idxmax()
print('Best category:',best_category)

#najbolji kupac 

best_customer = top_3_customers_by_revenue.sort_values(ascending = False).head(1)
print('Best customer:',best_customer)

#da li prodaja raste kroz vreme 

monthly_revenue = df.groupby('month')['revenue'].sum()
print('Revenue by month:',monthly_revenue)

