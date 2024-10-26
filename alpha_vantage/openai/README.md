# AlphaVantage OpenAI Tools

This library defines tools that an OpenAI LLM can use. The following endpoints are supported.

- [`TIME_SERIES_DAILY`](https://www.alphavantage.co/documentation/#daily) - returns raw (as-traded) daily time series (date, daily open, daily high, daily low, daily close, daily volume) of the global equity specified, covering 20+ years of historical data
- [`OVERVIEW`](https://www.alphavantage.co/documentation/#company-overview) - returns the company information, financial ratios, and other key metrics for the equity specified
- [`GLOBAL_QUOTE`](https://www.alphavantage.co/documentation/#latestprice) - returns the latest price and volume information for a ticker of your choice.

## Usage

```python
from alpha_vantage.openai import tools

# use the client
client = AlphaVantageClient()
...

# LLM code
response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )

if tool_function_name == 'get_company_overview':
    results = str(client.get_company_overview(tool_symbol_string))
elif tool_function_name == 'get_stock_quote':
    results = str(client.get_stock_quote(tool_symbol_string))
elif tool_function_name == 'get_time_series':
    results = str(client.get_time_series(tool_symbol_string))
```
