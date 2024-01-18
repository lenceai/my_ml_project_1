import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'City_A_Temp': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21],
    'City_B_Temp': [10, 12, 15, 17, 20, 22, 25, 24, 20, 18, 14, 11]
}

# Create DataFrame using data
df = pd.DataFrame(data)

df['Temp_Diff'] = abs(df['City_A_Temp'] - df['City_B_Temp'])

print(df)