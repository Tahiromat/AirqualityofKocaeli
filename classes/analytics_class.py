import helpers
import plotly.express


class AnalyticsClass:
    """
    Class that handles analytics
    """

    def __init__(self, streamlit, dataframe):
        self.streamlit = streamlit
        self.dataframe = dataframe

    def __update_layout(self, figure, title_text):
        figure.layout.update(
            title_text=title_text,
            xaxis_rangeslider_visible=False,
            height=helpers.Constants().chart_height(),
            width=helpers.Constants().chart_width(),
        )

    def __plotly_chart(self, figure):
        self.streamlit.plotly_chart(figure)

    def __update_layout_show_chart(self, figure, title_text):
        self.__update_layout(figure, title_text)
        self.__plotly_chart(figure)

    def visualize_histogram_chart(self, y_axis_param, title_text):
        figure = plotly.express.histogram(self.dataframe, x=y_axis_param)
        self.__update_layout_show_chart(figure, title_text)

    def visualize_line_chart(self, x_axis_param, y_axis_param, title_text):
        figure = plotly.express.line(self.dataframe, x=x_axis_param, y=y_axis_param)
        self.__update_layout_show_chart(figure, title_text)

    def visualize_bar_chart(self, x_axis_param, y_axis_param, title_text):
        figure = plotly.express.bar(x=x_axis_param, y=y_axis_param)
        self.__update_layout_show_chart(figure, title_text)

    def visualize_pie_chart(self, param_values, param_names):
        figure = plotly.express.pie(self.dataframe, x=param_values, y=param_names)
        self.__plotly_chart(figure)

    # Later update that chart with the mltiple columns and different colors
    def visualize_area_chart(self, x_axis_param, y_axis_param, title_text):
        figure = plotly.express.area(self.dataframe, x=x_axis_param, y=y_axis_param)
        self.__update_layout_show_chart(figure, title_text)

    # Later update that chart with the mltiple columns and different colors
    def visualize_scatter_chart(self, x_axis_param, y_axis_param, title_text):
        figure = plotly.express.scatter(x=x_axis_param, y=y_axis_param)
        self.__update_layout_show_chart(figure, title_text)

    # later add this function and dont forget the make list of latitude and longitude for cities will be visualize in the chart
    def visualize_map(latitude, longitude):
        pass
