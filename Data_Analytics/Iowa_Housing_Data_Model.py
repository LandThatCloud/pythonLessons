import pandas as pd

iowa_home_path = "/Users/simplyram/Documents/Python/Data_Analytics/train.csv"
home_data = pd.read_csv(iowa_home_path)

home_data.describe()
