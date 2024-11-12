import pandas as pd
import datasets

dataset = datasets.load_dataset('/data_jobs.csv')
df = dataset['train'].to_pandas()

df['job_title_short']