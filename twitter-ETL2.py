import pandas as pd

# Liste des chemins des fichiers CSV
csv_files = [
    'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/2016_12_05_trumptwitterall.csv',
    'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/2017_01_28_trump_tweets.csv',
    'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/trumptweets1205_127.csv',
    'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/trumpwords.csv'
]

# Lire tous les fichiers CSV et les combiner en un seul DataFrame
df_list = [pd.read_csv(file) for file in csv_files]
df = pd.concat(df_list, ignore_index=True)

# Afficher les premières lignes du DataFrame combiné
print(df.head())

# Afficher les informations sur le DataFrame (colonnes, types, valeurs manquantes, etc.)
#print(df.info())

# Manipulation et analyse de base

# # Supprimer les doublons
# df.drop_duplicates(subset='id', inplace=True)

# Gestion des valeurs manquantes
df.dropna(inplace=True)


# Save to new folders
df.to_csv('D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/cleaned_tweets.csv', index=False)



