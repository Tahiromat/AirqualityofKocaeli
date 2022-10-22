import helpers
import streamlit


def App():

    helpers.HelperFunctions().page_configuration(streamlit)
    helpers.HelperFunctions().sidebar_route(streamlit)

if __name__ == '__main__':
    App()