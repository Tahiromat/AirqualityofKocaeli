import os
import ui
from streamlit_option_menu import option_menu
from helpers.constants import Constants


class HelperFunctions:
    def __init__(self) -> None:
        pass

    def page_configuration(self, streamlit):
        streamlit.set_page_config(
            page_title="Air Quality", page_icon="❗", layout="wide"
        )
        streamlit.markdown(
            """ <style> [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {width: 280px;} </style> """,
            unsafe_allow_html=True,
        )
        hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
        streamlit.markdown(hide_streamlit_style, unsafe_allow_html=True)

    def __select_current_page(self, streamlit):
        with streamlit.sidebar:
            selected_page = option_menu(
                "Main Menu",
                ["Home", "Analytics", "Algorithms"],
                icons=["house", "list-task", "gear"],
                menu_icon="cast",
                default_index=0,
                orientation="vertical",
            )

        return selected_page

    def sidebar_route(self, streamlit):
        selected_page = self.__select_current_page(streamlit)

        if selected_page == "Home":
            ui.HomePage(streamlit).home()
        elif selected_page == "Analytics":
            ui.AnalyticsPage(streamlit).analytics()
        else:
            ui.AlgorithmsPage(streamlit).algorithms()

    def get_all_air_data(self):
        air_data_files = []
        for file in os.listdir(Constants().get_air_data_path()):
            if file.endswith(".csv"):
                air_data_files.append(file)
        return air_data_files
