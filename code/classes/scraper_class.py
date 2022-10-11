from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebScraper:
    """
    WebScraper class that is responsible for scraping the specified URL.
    """

    def __init__(self, driver):
        self.driver = driver

    def load_main_page(self):
        pass

    def select_city(self, city_name):
        pass

    def select_station(self, station_name):
        pass

    def select_features(self):
        pass

    def select_time_period(self):
        pass

    def select_start_date(self, start_date):
        pass

    def inquire_for_data(self):
        pass

    def export_data(self):
        pass


if __name__ == "__main__":
    scraper = WebScraper()
