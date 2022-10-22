import classes
import helpers
import os


class HomePage:
    def __init__(self, streamlit) -> None:
        self.streamlit = streamlit

    def home(self):
        self.streamlit.title("HOME PAGE")

        for filename in helpers.HelperFunctions().get_all_air_data():
            data_path = os.path.join(helpers.Constants().get_air_data_path(), filename)
            data = classes.PreprocessingClass().read_data(data_path)
            self.streamlit.write(data.head())
