import pandas as pd

data = {
    'Store': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Item': ['Apple', 'Banana', 'Orange', 'Grape', 'Apple', 'Banana', 'Orange', 'Grape'],
    'Price': [50, 20, 30, 60, 55, 22, 33, 65],
    'Quantity': [10, 12, 15, 16, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

df['TotalRevenue'] = df['Price'] * df['Quantity']

result = df.groupby('Store').agg({'TotalRevenue': 'sum', 'Price':'mean'}).reset_index()

result.rename(columns={'Price':'AveragePrice'}, inplace=True)

print(result)