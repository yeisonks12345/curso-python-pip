import pandas as pd 

import sklearn 

import matplotlib.pyplot as plt 

from sklearn.decomposition import PCA 

from sklearn.decomposition import IncrementalPCA 

from sklearn.linear_model import LogisticRegression 

from sklearn.preprocessing import StandardScaler 

from sklearn.model_selection import train_test_split
if __name__=="__main__":
    df = pd.read_csv("./data/heart.csv")
    print(df.head(5))