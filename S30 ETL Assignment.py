# -*- coding: utf-8 -*-
"""
update database folder location and filename
"""

db_loc = 'C:\\Users\\droo\\Downloads\\ETL Assignment v22-01\\'
db_name = 'S30 ETL Assignment.db'

import sqlite3
import pandas as pd

conn = sqlite3.connect(db_loc + db_name)
cursor = conn.cursor()



# SQL
cursor.execute(f'''
               select s.customer_id, c.age, i.item_name, round(sum(o.quantity), 0) as quantity
               from orders as o
                   left join sales as s on o.sales_id = s.sales_id
                   left join customers as c on s.customer_id = c.customer_id
                   left join items as i on o.item_id = i.item_id
               where c.age between 18 and 35
               group by s.customer_id, c.age, i.item_id
               having round(sum(o.quantity),0) > 0
                  ''')
data = cursor.fetchall()



# Pandas
orders = pd.read_sql_query("select * from orders", conn)
sales = pd.read_sql_query("select * from sales", conn)
customers = pd.read_sql_query("select * from customers", conn)
items = pd.read_sql_query("select * from items", conn)

merged_df = sales.merge(customers, on='customer_id')
merged_df = orders.merge(merged_df, on='sales_id')
merged_df = merged_df.merge(items, on='item_id')

filtered_df = merged_df[(merged_df['age'] >= 18) & (merged_df['age'] <= 35)]
filtered_df['quantity'] = filtered_df['quantity'].fillna(0).astype(int)

data = filtered_df.groupby(['customer_id', 'age', 'item_name'], as_index=False)['quantity'].sum()
data['quantity'] = data['quantity'].round()
data = data[data['quantity'] > 0]



# Close the database connection
conn.close()



# Export
try:
    data = pd.DataFrame(data, columns = ['customer_id', 'age', 'item_name', 'total_quantity'])
except: ""
outpath = db_loc + 'query.csv'
data.to_csv(outpath, sep=';', index=False)