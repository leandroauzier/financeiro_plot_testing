import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

import yfinance as yf

yf.pdr_override()

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
google = web.get_data_yahoo('GOOG')
google['Close'].plot(label='Close')
google['Dif'] = google['Close'] - google['Open']
df = google.sort_values(by=['Dif'], ascending=True)
df['Dif'].plot(label='Difference')
ax.legend()

print(df[:10])

plt.show()