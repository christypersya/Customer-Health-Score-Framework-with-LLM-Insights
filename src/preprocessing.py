import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    # Example preprocessing: fill missing values, encode categoricals
    df = df.fillna(0)
    df = pd.get_dummies(df)
    return df

def split_data(df, target_col):
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return train_test_split(X, y, test_size=0.2, random_state=42)