import pytest
from src.logic import analyze_price
from src.api_client import get_bitcoin_price
from unittest.mock import patch

# --- Unit Tests for Logic ---

def test_analyze_price_buy_signal():
    """Test that logic triggers a buy alert when price is low"""
    result = analyze_price(45000, 50000)
    assert "BUY ALERT" in result

def test_analyze_price_hold_signal():
    """Test that logic stays quiet when price is high"""
    result = analyze_price(55000, 50000)
    assert "Hold" in result

# --- Integration Tests with Mocking ---

# @patch('requests.get')
# def test_get_bitcoin_price_success(mock_get):
#     """Test successful API data extraction"""
#     # We 'fake' the API response
#     mock_get.return_value.status_code = 200
#     mock_get.return_value.json.return_value = {"bitcoin": {"usd": 62000}}
    
#     price = get_bitcoin_price()
#     assert price == 62000

# @patch('requests.get')
# def test_get_bitcoin_price_rate_limit(mock_get):
#     """Test how code handles the 429 error"""
#     mock_get.return_value.status_code = 429
    
#     price = get_bitcoin_price() # Minimal retries for fast test
#     assert price is None

def test_actual_api_call():
    """A REAL integration test that hits the live internet"""
    price = get_bitcoin_price()
    
    # Assertions: What must be true for the integration to be 'successful'?
    assert price is not None        # The connection worked
    assert isinstance(price, int) # The data format is correct
    assert price > 0                # The data makes sense
