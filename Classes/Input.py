import numpy as np
import pandas as pd

class InputClass():

    def __init__(self, file):
        df = pd.read_csv(file)
        self.data = df.replace(np.nan, '', regex=True)

input = InputClass('./Input/r.csv')