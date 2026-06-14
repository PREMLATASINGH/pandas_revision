import sys

try:
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	from sklearn.linear_model import LinearRegression
except ModuleNotFoundError as e:
	missing = getattr(e, 'name', str(e))
	print(f"Missing dependency: {missing}")
	print("Install required packages with: pip install -r requirements.txt")
	sys.exit(1)

df = pd.read_csv('netflix_titles.csv')
print(df.head())