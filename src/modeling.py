from lightgbm import LGBMClassifier
import joblib

def train_model(X_train, y_train):
    model = LGBMClassifier()
    model.fit(X_train, y_train)
    return model

def save_model(model, path="model.pkl"):
    joblib.dump(model, path)

def load_model(path="model.pkl"):
    return joblib.load(path)