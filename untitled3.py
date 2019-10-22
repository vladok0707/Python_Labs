import requests
from collections import Counter
from datetime import datetime, date
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

friends_ALL = []
age = [];
city = []
status = []
photos = []
videos = []
notes = []
groups = []

def calculateAge(birthDate): 
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age

def deep_getfriend(user_id, deep):
    if deep == 0:
        return None
    else:
        deep -=1
        access_token = '6ce4e1e6eff341f896404821f13dd6537fb44342d11967679739f5c3148f6a534a039cd0930b4256b5cf1'
        api_version = '5.52'
        res_users = requests.get(f'https://api.vk.com/method/friends.get?user_id={user_id}&access_token={access_token}&v={api_version}')
        try:
            friends = (res_users.json())["response"].get('items')
            global friends_ALL
            friends_ALL +=friends    
            for friend in friends:
                info(friend)
                deep_getfriend(friend,deep)
        except: ()

def info(id):
        access_token = '6ce4e1e6eff341f896404821f13dd6537fb44342d11967679739f5c3148f6a534a039cd0930b4256b5cf1'
        api_version = '5.52'
        res_users = requests.get(f'https://api.vk.com/method/users.get?user_ids={id}&fields=bdate , city,status,counters&access_token={access_token}&v={api_version}')
        try:
            info = (res_users.json())["response"][0]
        except: return 0
        global age
        try:
            b_date = datetime.strptime(info.get('bdate'), '%d.%m.%Y')
            age.append(calculateAge(b_date))
        except : ()
        try:
            a = info.get('city').get('title')
            city.append(a)
        except : ()
        try:
            status.append(info.get('status'))
        except : ()
        try:
            photos.append(info.get('counters').get('photos'))
        except : ()
        try:
            videos.append(info.get('counters').get('videos'))
        except : ()
        try:
            notes.append(info.get('counters').get('notes'))
        except : ()
        try:
            groups.append(info.get('counters').get('groups'))
        except : ()
            


def main():  
    deep_getfriend(130585080,1)
    print(Counter(videos))
    X = np.array(list(Counter(videos).items()))
    km = KMeans(n_clusters=3, init='random',n_init=10, max_iter=300, tol=1e-04, random_state=0)
    y_km = km.fit_predict(X)
    plt.scatter(X[y_km == 0, 0], X[y_km == 0, 1],s=50, c='lightgreen',marker='s', edgecolor='black',label='cluster 1')

    plt.scatter(X[y_km == 1, 0], X[y_km == 1, 1],s=50, c='orange',marker='o', edgecolor='black',label='cluster 2')

    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='lightblue',marker='v', edgecolor='black',label='cluster 3')

# plot the centroids
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],s=250, marker='*',c='red', edgecolor='black',label='centroids')
    plt.legend(scatterpoints=1)
    plt.grid()
    plt.show()
    
    km = KMeans(n_clusters=5, init='random',n_init=10, max_iter=300, tol=1e-04, random_state=0)
    y_km = km.fit_predict(X)
    y_km = km.fit_predict(X)
    plt.scatter(X[y_km == 0, 0], X[y_km == 0, 1],s=50, c='lightgreen',marker='s', edgecolor='black',label='cluster 1')

    plt.scatter(X[y_km == 1, 0], X[y_km == 1, 1],s=50, c='orange',marker='o', edgecolor='black',label='cluster 2')

    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='lightblue',marker='v', edgecolor='black',label='cluster 3')
    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='green',marker='.', edgecolor='black',label='cluster 4')
    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='yellow',marker=',', edgecolor='black',label='cluster 5')

# plot the centroids
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],s=250, marker='*',c='red', edgecolor='black',label='centroids')
    plt.legend(scatterpoints=1)
    plt.grid()
    plt.show()
    
    km = KMeans(n_clusters=7, init='random',n_init=10, max_iter=300, tol=1e-04, random_state=0)
    y_km = km.fit_predict(X)
    plt.scatter(X[y_km == 0, 0], X[y_km == 0, 1],s=50, c='lightgreen',marker='s', edgecolor='black',label='cluster 1')

    plt.scatter(X[y_km == 1, 0], X[y_km == 1, 1],s=50, c='orange',marker='o', edgecolor='black',label='cluster 2')

    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='lightblue',marker='v', edgecolor='black',label='cluster 3')

    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='green',marker='.', edgecolor='black',label='cluster 4')
    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='blue',marker=',', edgecolor='black',label='cluster 5')
    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='pink',marker='>', edgecolor='black',label='cluster 6')
    plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1],s=50, c='black',marker='<', edgecolor='black',label='cluster 7')
# plot the centroids
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],s=250, marker='*',c='red', edgecolor='black',label='centroids')
    plt.legend(scatterpoints=1)
    plt.grid()
    plt.show()


if __name__ == '__main__':
	main()