import requests
from alpha_vantage.config import API_KEY, BASE_URL

TIME_SERIES_DAILY = "TIME_SERIES_DAILY"
OVERVIEW = "OVERVIEW"
GLOBAL_QUOTE = "GLOBAL_QUOTE"

class AlphaVantageClient:
    def __init__(self, api_key=API_KEY):
        self.api_key = api_key

    def _make_request(self, function, **kwargs):
        params = {"function": function, "apikey": self.api_key, **kwargs}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        if "Error Message" in data:
            raise ValueError(f"API Error: {data['Error Message']}")
        
        return data

    def get_time_series_daily(self, symbol):
        """
        Fetches the time series data for a given stock symbol.
        """
        return self._make_request(TIME_SERIES_DAILY, symbol=symbol)

    def get_company_overview(self, symbol):
        """
        Fetches the company overview for a given stock symbol.
        """
        return self._make_request(OVERVIEW, symbol=symbol)

    def get_stock_quote(self, symbol):
        """
        Fetches the stock quote for a given stock symbol.
        """
        return self._make_request(GLOBAL_QUOTE, symbol=symbol) 