import pandas as pd
from sklearn.model_selection import train_test_split

DATA_FILE = "complete.dat"

data = pd.read_csv('complete-data.dat', header=None, delim_whitespace=True)
train, test = train_test_split(data, train_size = 0.8, test_size = 0.2)

train.to_csv("train.dat", index=False, header=None, sep=" ")
test.to_csv("test.dat", index=False, header=None, sep=" ")
