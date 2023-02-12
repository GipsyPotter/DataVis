import pandas as pd
import numpy as np

dataset = np.genfromtxt('normal_distribution.csv', delimiter=',')
data = dataset[:2]
mean = np.mean(data[3])
print(mean)
