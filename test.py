import pandas as pd
import numpy as np

df = pd.read_csv("historical_air_quality_2021_en.csv")
print("Mean temp in VN:", df["Temperature"].mean().round(2))
print("Standard deviation of temp in VN:", df["Temperature"].std().round(2))
print("Median of temp in VN:", df["Temperature"].median())
