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

    def station_location_info(self):
        dct = {
            "Kocaeli - Alikahya-MTHM": [40.778773125653856, 30.004645890276294],
            "Kocaeli - Dilovası-İMES OSB 1-MTHM": [40.838336846997116, 29.57919698108752],
            "": [],
            "": [],
            "": [],
            "": [],
            "": [],
            "": [],
            "": [],
            "": [],
        }