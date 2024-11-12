import pytest
import allure
from pages.SYJ.home_page_holistor_syj import HomePageHolistorSYJ
from pages.SYJ.home_page_holistor_syj import LoginPlataformaPage


@pytest.fixture
def home_page_holistor_syj(browser, base_url, datos_usuario):
    return HomePageHolistorSYJ(browser, base_url, datos_usuario)


@allure.suite("Casos de prueba Home page")
@allure.epic("Home Page")
@allure.feature("Seleccioar Empresa")
@allure.story("US: Seleccionar empresa SYJ")
@allure.testcase("TC - 0001")
@allure.title("Seleccionar la empresa de fila 1")
@allure.description("Este test verifica que se pueda seleccionar la fila 1 de la lista de empresas ")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.seleccionar_empresa
@pytest.mark.regresion

def test_syj_seleccionar_empresa(home_page_holistor_syj):
    with allure.step("Navegar en la pagina de inicio de plataforma con "
                     "los datos correctos en los campos Tenant, Usuario, Contraseña"):
        home_page_holistor_syj.navegar_plataforma()
    with allure.step("Hacemos clic en el botón para cargar MP"):
        home_page_holistor_syj.open_syj()

    with allure.step("Seleccionamos la empresa de la Fila 1 de la lista de empresas a seleccionar"):
        empresa_seleccionada = home_page_holistor_syj.open_select_empresa()
        assert empresa_seleccionada != '', ("No se pudo seleccionar la empresa o el tenant no tiene"
                                            " empresa definida aún.")
