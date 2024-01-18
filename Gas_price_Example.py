import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,5))

plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize': 18})

plt.plot(gas.Year, gas.USA, 'b.-', label='United States')
plt.plot(gas.Year, gas.Canada, 'r.-')
plt.plot(gas.Year, gas['South Korea'], 'g.-')
plt.plot(gas.Year, gas.Australia, 'y.-')

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.savefig('Gas_price_figure.png', dpi=300)

plt.show()