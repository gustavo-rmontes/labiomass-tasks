# Compostos confirmados - script
# Como utilizar?
# 1. Colocar o .csv de entrada na mesma pasta do script;
# 2. Trocar a variável file_name para o nome do arquivo .csv de entrada;
# 3. Rodar o script.   
# O resultado será exportado para um csv de saída chamado 'output.csv'

import pandas as pd

file_name = 'Height_1_2024_12_03_14_03_55.csv' # .csv file name

df = pd.read_csv(file_name) # read .csv file
df.head(10) # show first 10 rows
df.columns # show table columns

colunas = df.iloc[3, :] # get columns labels
colunas

new_df = df.iloc[4:, :] # get the valuable table
new_df.head() # show first 5 rows

new_df.rename(columns=colunas, inplace=True) # rename columns to the correct labels  
new_df.head() # show first 5 rows

selected_columns = ['Alignment ID', 'Average Rt(min)',  'Average Mz', 'Metabolite name', 'Adduct type', 'Reference m/z']
final_df = new_df[selected_columns] # select only a few columns
final_df.head() # show first 5 rows

final_df.dtypes # show columns types

# Convert these columns to float
final_df[['Average Rt(min)', 'Average Mz', 'Reference m/z']] = final_df[['Average Rt(min)', 'Average Mz', 'Reference m/z']].apply(pd.to_numeric, errors='coerce')
final_df.dtypes # show columns types

# new column
final_df['Erro (ppm)'] = (final_df['Average Mz'] - final_df['Reference m/z']) / final_df['Reference m/z'] * 1000000
final_df.head() # show first 5 rows

# Delect repeated rows
final_df = final_df[final_df["Erro (ppm)"] != 0].drop_duplicates(subset="Metabolite name")
final_df.head() # show first 5 rows

final_df.to_csv('output.csv', sep=';', index=False, encoding='utf-8') # Export to an csv