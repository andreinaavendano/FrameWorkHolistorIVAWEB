import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService



def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Type of browser: chrome, firefox, edge, safari",
    )
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Entorno: dev, staging, prod")

    parser.addoption("--app",
    action = "store",
    default = "PDE",
    help = "Aplicacion: SYJ, PDE, CTB, IVA")

@pytest.fixture
def base_url(request):

    environment = request.config.getoption("--env")
    if environment == "qa":
        return "https://plataforma-saas-qa.azurewebsites.net"
    elif environment == "uat":
        return "https://plataforma-saas-uat.azurewebsites.net"
    elif environment == "stg":
        return "https://plataforma-saas-stg.azurewebsites.net"
    elif environment == "prod":
        return "https://plataforma-saas.azurewebsites.net"
    else:
        raise ValueError(f"Entorno no soportado: {environment}")

@pytest.fixture(scope="session")
def datos_usuario(request):

    app = request.config.getoption("--app")
    environment = request.config.getoption("--env")
    # Validar el entorno y la aplicación para retornar datos de usuario específicos
    if environment == "qa":
        if app == 'SYJ':
            return {"usuario": "Andreina", "clave": "123qwe", "tenan": "SYJ_PM"}
        if app == 'PDE':
            return {"usuario": "Andreina", "clave": "123qwe", "tenan": "Agenda22022022"}

    if environment == "UAT":
        if app == 'SYJ':
            return {"usuario": "Andreina", "clave": "123qwe", "tenan": "SYJ_Especialistas"}
        if app == 'PDE':
            return {"usuario": "Andreina", "clave": "123qwe", "tenan": "Agenda22022022"}


@pytest.fixture(scope="session")
def browser(request):

    browser_type = request.config.getoption("--browser").lower()
    if browser_type == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_type == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser_type == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser_type == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {browser_type} no soportado")
    yield driver
    driver.quit()




