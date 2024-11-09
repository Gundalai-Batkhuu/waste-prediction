import joblib
import os


def predict(data):
    model_dir = os.path.join(os.path.dirname(__file__), 'models')
    model_path = os.path.join(model_dir, 'xgb_model.sav')
    clf = joblib.load(model_path)
    return clf.predict(data)
