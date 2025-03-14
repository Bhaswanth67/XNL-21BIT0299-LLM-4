import pytest
from tools.api_tools import YahooFinanceTool, NewsAPITool, CryptoAPITool

def test_yahoo_finance_tool():
    tool = YahooFinanceTool()
    result = tool._run("AAPL")
    assert "AAPL" in result
    assert "Price" in result

def test_news_api_tool():
    tool = NewsAPITool()
    result = tool._run("Apple")
    assert "Title" in result or "No news found" in result

def test_crypto_api_tool():
    tool = CryptoAPITool()
    result = tool._run("bitcoin")
    assert "Bitcoin price" in result or "not found" in result
