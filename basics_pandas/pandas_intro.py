import pandas as pd
import datasets

pd.read_csv('./data_jobs.csv')

dataset = datasets.load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

print(df.info())
