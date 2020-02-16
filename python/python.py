import cbpro
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

### connect to coinbase public api and download ETH and BTC data
public_client = cbpro.PublicClient()

eth = public_client.get_product_historic_rates('ETH-USD')
eth = pd.DataFrame(eth, columns=['time','open','high','low','close','volume'])
eth
eth.close.plot()
plt.show()

btc = public_client.get_product_historic_rates('BTC-USD')
btc = pd.DataFrame(btc, columns=['time','open','high','low','close','volume'])
btc
btc.close.plot()
plt.show()

combined = pd.merge(btc, eth, on='time')

rets = combined.pct_change()

sns.pairplot(rets[['close_x', 'close_y']])
plt.show()
