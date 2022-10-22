import pandas
import os


class PreprocessingClass:
    """
    Class that handles preprocessing
    """

    def __init__(self) -> None:
        pass

    def read_data(self, data_path):
        return pandas.read_csv(data_path)
