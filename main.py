import pandas as pd
import panel as pn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bank_dataset.csv')
data = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})

print(df.head(5))

sns.heatmap(data)

plt.title('Heatmap example')
plt.show()