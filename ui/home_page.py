import streamlit
# import classes
import os

# PPC = classes.PreprocessingClass()


class HomePage:

    def __init__(self) -> None:
        pass

    def create_title(self, title_text):
        return streamlit.title(title_text)
