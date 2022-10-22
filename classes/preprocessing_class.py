import os
import pandas


class PreprocessingClass:
    """
    Class that handles preprocessing
    """

    def __init__(self) -> None:
        pass

    def read_data(self, data_path):
        """
            Reads the data from the given data_path
        """
        return pandas.read_csv(data_path)

    def object_to_datetime(self, dataframe, param):
        """
            Converts the given object type dates to a datetime in dataframe
        """
        dataframe[param] = pandas.to_datetime(dataframe[param])
        return dataframe
    
    def __find_first_and_last_datetime(self, dataframe, param):
        """
            Finds the first and last datetime in dataframe
        """
        first_datetime = min(dataframe[param])
        last_datetime = max(dataframe[param])
        return first_datetime, last_datetime

    def __check_missing_dates(self, dataframe, param):
        """
            Checks if the given dates are missing in dataframe
        """
        dataframe = self.object_to_datetime(dataframe, param)
        first_datetime, last_datetime = self.__find_first_and_last_datetime(dataframe, param)
        date_range = pandas.date_range(start=first_datetime, end=last_datetime, freq='h')
        return date_range.difference(dataframe[param])
    
    def fill_missing_dates(self, dataframe, param):
        """
            Fills the missing dates in dataframe 
        """
        missing_dates_list = self.__check_missing_dates(dataframe, param)
        if len(missing_dates_list) == 0:
            pass
        else:
            pass
            # Add missing dates to existing dates column in dataframe
    
