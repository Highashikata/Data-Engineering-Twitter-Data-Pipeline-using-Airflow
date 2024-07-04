from airflow import DAG
# Importe le DummyOperator, un opérateur qui ne fait rien. Il est souvent utilisé pour créer des points de synchronisation dans le DAG.
from airflow.operators.dummy import DummyOperator
# Importe la classe datetime du module datetime pour définir les dates de démarrage et d'autres paramètres temporels.
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from airflow.operators.bash import BashOperator
import os
import glob


# Config DAGs arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'email': ['bassambenidir@yahoo.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'twitter_airflow_DAG',
    default_args=default_args,
    description='An example DAG',
    schedule_interval='@daily',
)


###### Définir les fonctions Python pour les tâches PythonOperator ######
# Liste des chemins des fichiers CSV

# csv_files = [
#     'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/2016_12_05_trumptwitterall.csv',
#     'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/2017_01_28_trump_tweets.csv',
#     'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/trumptweets1205_127.csv',
#     'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/trumpwords.csv'
# ]


# Définir le répertoire de base où se trouvent les fichiers CSV
base_dir = 'D:/Bassam Projects/Data Engineering/Data-Engineering-Twitter Data Piepline/Twitter-dataset/'

# Utiliser glob pour trouver tous les fichiers CSV dans le répertoire et ses sous-répertoires
csv_files = glob.glob(os.path.join(base_dir, '**', '*.csv'), recursive=True)

# Afficher les fichiers trouvés sous forme de liste
print(csv_files)

def extract_datat(**kwargs):
    df_list = [pd.read_csv(file) for file in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)

    combined_df.to_csv(base_dir, index=False)
    print("Extraction terminé")


start = DummyOperator(
    task_id='start',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)


# Cette ligne définit une dépendance entre les tâches start et end.
start >> end

