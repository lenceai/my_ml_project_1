import pandas as pd

#This is the new dataset

data = {
    'Product': ['Laptop', 'Desktop', 'Tablet', 'Phone', 'Smartwatch'],
    'Price': [25000, 12000, 8000, 22000, 5000]
}

df = pd.DataFrame(data)

result = df[df['Price'] >= 20000].sort_values(by='Price', ascending=False)

print(result)
