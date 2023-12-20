from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver