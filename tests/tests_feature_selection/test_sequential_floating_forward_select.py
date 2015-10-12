import numpy as np
from mlxtend.feature_selection import SFFS

def test_Iris():
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.datasets import load_iris

    iris = load_iris()
    X = iris.data
    y = iris.target

    knn = KNeighborsClassifier(n_neighbors=4)

    sffs = SFFS(knn, k_features=2, scoring='accuracy', cv=5, print_progress=False)
    sffs.fit(X, y)

    assert(sffs.indices_ == (2, 3))
    assert(round(sffs.k_score_, 2) == 0.97)


def test_selects_all():
    from sklearn.neighbors import KNeighborsClassifier
    from mlxtend.data import wine_data

    X, y = wine_data()
    knn = KNeighborsClassifier(n_neighbors=4)
    sffs = SFFS(knn, k_features=13, scoring='accuracy', cv=3, print_progress=False)
    sffs.fit(X, y)
    assert(len(sffs.indices_) == 13)
