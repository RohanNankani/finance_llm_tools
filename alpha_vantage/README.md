# AlphaVantage Client

This library defines a client for [AlphaVantage API](https://www.alphavantage.co/documentation/). The following endpoints are supported.

- [`TIME_SERIES_DAILY`](https://www.alphavantage.co/documentation/#daily) - returns raw (as-traded) daily time series (date, daily open, daily high, daily low, daily close, daily volume) of the global equity specified, covering 20+ years of historical data
- [`OVERVIEW`](https://www.alphavantage.co/documentation/#company-overview) - returns the company information, financial ratios, and other key metrics for the equity specified
- [`GLOBAL_QUOTE`](https://www.alphavantage.co/documentation/#latestprice) - returns the latest price and volume information for a ticker of your choice.

## Usage

```python
from alpha_vantage import AlphaVantageClient

# use the client
client = AlphaVantageClient()
```

## Tools

The tools for the following LLMs is supported in this library. 

- [OpenAI](./openai/README.md) 