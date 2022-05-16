import pandas as pd

original_df = pd.read_csv('southeast.csv')

teresopolis_df = original_df.region == 'teresopolis'

teresopolis_df.to_csv('teresopolis.csv', index = None)