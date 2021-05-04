# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_io.ipynb (unless otherwise specified).

__all__ = ['ADULT_PATH', 'ASSETS_PATH', 'load_adult']

# Cell
import pandas as pd
from pathlib import Path

# Cell

ADULT_PATH = Path('../data/adult.csv').absolute()

ASSETS_PATH = Path('../assets').absolute()


# Cell

def load_adult():
    """
    Download a sample of Adult dataset (if necessary), and load it
    """
    if ADULT_PATH.exists():
        df = pd.read_csv(ADULT_PATH)
    else:
        CSV_HEADER = [
        'age',
        'workclass',
        'fnlwgt',
        'education',
        'education-num',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'capital-gain',
        'capital-loss',
        'hours-per-week',
        'native-country',
        'salary']

        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

        df = pd.read_csv(url, header=None, names=CSV_HEADER)
        df.to_csv(ADULT_PATH, index=False)
    return df
