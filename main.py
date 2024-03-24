import pandas as pd
import panel as pn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bank_dataset.csv')

print(df.head(5))

sns.heatmap(df)