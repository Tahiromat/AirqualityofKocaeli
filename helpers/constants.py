import os


class Constants:
    def __init__(self):
        pass

    def get_raw_data_path(self):
        return os.path.join("raw-data")

    def get_air_data_path(self):
        return os.path.join("air-data")

    def chart_height(self):
        return 600

    def chart_width(self):
        return 800