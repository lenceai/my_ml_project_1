import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21]
}

# Create DataFrame using data
df = pd.DataFrame(data)

high_ave = df[df['Temperature'] == df['Temperature'].max()]['Month'].values[0]

print(f"The highest temperature is {high_ave}")