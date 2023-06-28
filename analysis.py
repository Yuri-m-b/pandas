""" analysis """

import pandas as pd

poke = pd.read_csv('/home/yuri/Pandas_Tutorial/pandas-master/pokemon_data.csv')

# print(poke)

# # Read Header
# poke.columns

# # Read each Column
# print(poke[['Name', 'Type 1', 'HP']])

# # Reach each row
# print(poke.head(4))
# print(poke.iloc[1:4])

# # Show only the index and row Name
# for index, row in poke.iterrows():
#     print(index, row['Name'])

# poke['Total'] = poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed']
# print(poke.head(5))

# SortingDescribing Data
# print(poke.sort_values(['Type 1', 'HP']))

# Making Changes to the data
poke['Total'] = poke.iloc[:, 4:10].sum(axis=1)
print(poke.head(5))
