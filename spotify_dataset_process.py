import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.neighbors import KDTree

def fileprocessing(filename):
    print('filename', filename)
    df =pd.read_csv(filename)
    global df1
    df1 = df.drop(['id','release_date'], axis=1)
    scaler = MinMaxScaler()
    df1[['acousticness', 'danceability', 'duration_ms', 'energy','explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
        'popularity', 'speechiness', 'tempo', 'valence', 'year']] = scaler.fit_transform(df1[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode','popularity', 'speechiness', 'tempo', 'valence', 'year']])
    kmeans = KMeans(
       init="random",
       n_clusters=7,
       n_init=10,
       max_iter=300,
    random_state=42 )
    kmeans.fit(df1[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness', 'key', 'liveness', 'loudness','mode','popularity', 'speechiness', 'tempo', 'valence', 'year']])
    labels = kmeans.predict(df1[['acousticness', 'danceability', 'duration_ms', 'energy','explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode','popularity', 'speechiness', 'tempo', 'valence', 'year']])
    df1['labels'] = labels 

class User:
    def __init__(self):
        self.dbmain = pd.DataFrame([])
        self.db0 = pd.DataFrame([])
        self.db1 = pd.DataFrame([])
        self.db2 = pd.DataFrame([])
        self.db3 = pd.DataFrame([])
        self.db4 = pd.DataFrame([])
        self.db5 = pd.DataFrame([])
        self.db6 = pd.DataFrame([])

    def show_entries(self, age):
        #to return a dictionary
        if age > 30:
            age_range_min = 2020 - age + 5
            age_range_max = 2020 - age + 30
            minmax_min = (2020 - age + 5 - 1921)/(2020 -1921)
            minmax_max = (2020 - age + 30 - 1921)/(2020 - 1921)
        else:
            age_range_min = 2020 - age
            age_range_max = 2020
            minmax_min = (2020 - age - 1921)/(2020 - 1921)
            minmax_max = 1
        
        dw = df1[(minmax_min <= df1['year']) & (minmax_max >= df1['year'])]
        xa = dw[['name', 'artists']]
        x = xa.sample(10)
        m = pd.DataFrame([x.index, x['name'], x['artists']], index =['id', 'name', 'artists'])
        m = m.transpose()
        ma = m.set_index(['name']).T.to_dict('list')
        return ma


    def insert_song(self, index):
        lb = df1.iloc[index, :]['labels']
        self.dbmain = pd.concat([pd.DataFrame(df1.iloc[index, :]).transpose(), self.dbmain])
        if lb == 0:
            self.db0 = pd.concat([pd.DataFrame(df1.iloc[index, :]).transpose(), self.db0])
        elif lb == 1:
            self.db1 = pd.concat([pd.DataFrame(df1.iloc[index, :]).transpose(), self.db1])
        elif lb == 2:
            self.db2 = pd.concat([pd.DataFrame(df1.iloc[index, :]).transpose(), self.db2])
        elif lb == 3:
            self.db3 = pd.concat([pd.DataFrame(df1.iloc[index, :]).transpose(), self.db3])
        elif lb == 4:
            self.db4 = pd.concat([pd.DataFrame(df1.iloc[index, :]).transpose(), self.db4])
        elif lb == 5:
            self.db5 = pd.concat([pd.DataFrame(df1.iloc[index, :]).transpose(), self.db5])
        else:
            self.db6 = pd.concat([pd.DataFrame(df1.iloc[index, :]).transpose(), self.db6])
    
    
    
    def return_listen_history(self):
        m = self.dbmain[['name', 'artists']]
        d = m.set_index('name').T.to_dict('list')
        return d
    
    
    def return_songs(self, label):
        #returning the songs
        if label == 0 and len(self.db0) > 0:
            temp =  self.db0.head(1)
        elif label == 1 and len(self.db1) > 0:
            temp = self.db1.head(1)
        elif label == 2 and len(self.db2) > 0:
            temp =  self.db2.head(1)
        elif label == 3 and len(self.db3) > 0:
            temp =  self.db3.head(1)
        elif label == 4 and len(self.db4) > 0:
            temp =  self.db4.head(1)
        elif label == 5 and len(self.db5) > 0:
            temp =  self.db5.head(1)
        elif label == 6 and len(self.db6) > 0:
            temp = self.db6.head(1)
        else:
            return pd.DataFrame([[]])
        print(temp)

        tree = KDTree((df1[df1['labels'] == label][['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness', 'key', 'liveness', 'loudness','mode','popularity', 'speechiness', 'tempo', 'valence', 'year']]), leaf_size=2)
        dist, ind = tree.query((temp[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness', 'key', 'liveness', 'loudness','mode','popularity', 'speechiness', 'tempo', 'valence', 'year']]), k=3)
#df1[df1['labels'] == lb[0]]
        return df1[df1['labels'] == label].iloc[ind[0]][['name', 'artists']]
