import pandas as pd

 
# Fazendo o merge das listas csv
lista1 = pd.read_csv("lst11.csv", sep=",")
lista2 = pd.read_csv("lst22.csv", sep=",")

#Authors,Author(s) ID,Title,Year,Source title,Volume,Issue,Art. No.,Page start,Page end, Page count,Link,PubMed ID,Document Type,Source,EID
df1 = pd.DataFrame(lista1,columns=['Authors', 'Author(s) ID', 'Title', 'Year', 'Source title', 'Volume', 'Issue', 'Art. No.', 
                                'Page start', 'Page end', 'Page count', 'Link', 'PubMed ID', 'Document Type', 'Source', 'EID'])
df2 = pd.DataFrame(lista2,columns=['Authors', 'Author(s) ID', 'Title', 'Year', 'Source title', 'Volume', 'Issue', 'Art. No.', 
                                'Page start', 'Page end', 'Page count', 'Link', 'PubMed ID', 'Document Type', 'Source', 'EID'])

# print(df1)
# print(df2)

set_diff_df_1_to_2 = pd.concat([df2, df1, df1]).drop_duplicates(keep=False)
# print('Diferença Lista1 para Lista2:')
# print(set_diff_df_1_to_2)
set_diff_df_1_to_2.to_csv('diferenca_lista1_to_lista2.csv', index=False)

set_diff_df_2_to_1 = pd.concat([df1, df2, df2]).drop_duplicates(keep=False)
# print()
# print('Diferença csv2 para csv1:')
# print(set_diff_df_2_to_1)
set_diff_df_2_to_1.to_csv('diferenca_lista2_to_lista1.csv', index=False)

