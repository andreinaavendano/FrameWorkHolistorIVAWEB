import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.mark.navegacion
def test_prueba():
    driver.get("https://www.google.com")
    titulo = driver.title
    assert titulo == "Google"




