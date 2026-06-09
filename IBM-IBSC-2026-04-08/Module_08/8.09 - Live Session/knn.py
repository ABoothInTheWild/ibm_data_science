import numpy as np

class KNN:
    def __init__(self, k):
        self.__k = k
        self.__X = None

    def __euclidian(self, a, b):
        '''
        Calculate euclidian distance between two data points
        '''
        dist = np.sqrt(np.sum((a - b) ** 2))
        return dist

    def __distances(self, x):
        '''
        Get distances between x and all the training examples
        '''
        dists = []
        for i in range(self.__X.shape[0]):
            dist = self.__euclidian(self.__X[i,:], x)
            dists.append((dist, i))
        return dists

    def fit(self, X, y):
        '''
        All we do here is to memorize the training data and labels!
        '''
        self.__X = np.copy(X)
        self.__y = np.copy(y)
        self.__classes = np.unique(y)
        return self
        
    def predict(self, X):
        '''
        Now we'll get the distances between each input example and the 
        training examples we have memorized, sort them, and take the best k. 
        Then we'll find the majority class of the best k neighbors, and 
        that is our prediction for the example. We'll also get and return
        probabilites as well.
        '''
        assert self.__X is not None, 'Model has not been fit'
        labels = []
        probs = []
        for x in X:
            dists = self.__distances(x)
            dists.sort(key=lambda d: d[0])
            neighbors = dists[:self.__k]

            class_dist = [0] * len(self.__classes)
            for neighbor in neighbors:
                class_dist[self.__y[neighbor[1]]] += 1

            label = np.argmax(class_dist)
            prob = class_dist[label] / np.sum(class_dist)
            labels.append(label)
            probs.append(prob)
        return labels, probs