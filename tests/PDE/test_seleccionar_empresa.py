import pytest
import allure
from pages.PDE.home_page_holistor_pde import HomePageHolistorPDE


@pytest.fixture
def home_page_holistor_pde(browser, base_url, datos_usuario):
    return HomePageHolistorPDE(browser, base_url, datos_usuario)


@allure.suite("Casos de prueba Home page")
@allure.epic("Home Page")
@allure.feature("Seleccioar Empresa")
@allure.story("US: Seleccionar empresa")
@allure.testcase("TC - 0001")
@allure.title("Seleccionar la empresa de fila 1")
@allure.description("Este test verifica que se pueda seleccionar la fila 1 de la lista de empresas ")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.seleccionar_empresa
@pytest.mark.regresion
def test_pde_seleccionar_empresa(home_page_holistor_pde):
    with allure.step("Navegar en la pagina de inicio de plataforma con "
                     "los datos correctos en los campos Tenant, Usuario, Contraseña"):
        home_page_holistor_pde.navegar_plataforma()
    with allure.step("Hacemos clic en el botón para cargar MP"):
        home_page_holistor_pde.open_pde()

    with allure.step("Seleccionamos la empresa de la Fila 1 de la lista de empresas a seleccionar"):
        empresa_seleccionada = home_page_holistor_pde.open_select_empresa()
        assert empresa_seleccionada != '', ("No se pudo seleccionar la empresa o el tenant no tiene"
                                            " empresa definida aún.")
