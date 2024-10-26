from alpha_vantage import AlphaVantageClient

client = AlphaVantageClient()
data = client.get_time_series_daily(symbol="AAPL")