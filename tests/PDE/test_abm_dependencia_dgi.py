import pytest
import allure
from pages.PDE.home_page_holistor_pde import HomePageHolistorPDE
from pages.PDE.abm_dependencia_dgi import ABM_Dependencia_DGI

@pytest.fixture
def abm_dependencia_dgi(browser, base_url, datos_usuario):
    return ABM_Dependencia_DGI(browser, base_url, datos_usuario)


@pytest.fixture(scope="function")
def setup(abm_dependencia_dgi):
    return abm_dependencia_dgi.iniciar()

@allure.suite("Casos de Prueba Dependencia DGI")
@allure.epic("Archivos")
@allure.feature("Datos Generales")
@allure.story("US: ABM Dependencia DGI")
@allure.testcase("TC - 0001")
@allure.title("Verificar item de menu")
@allure.description("Este test verifica que se pueda ingresar al item de menu")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dependencia_dgi
@pytest.mark.regresion
def test_ingresar_menu(abm_dependencia_dgi, setup):

    resultado = abm_dependencia_dgi.selected_item_menu_dgi()
    assert resultado, "La pagina no corresponde con la esperada"
    titulo = abm_dependencia_dgi.get_titulo()
    titulo_esterado = 'Dependencias DGI'
    assert titulo == titulo_esterado, "El titulo no se corresponde con el esperado"
    assert abm_dependencia_dgi.add_item(), "No se pudo agregar el nuevo item"
    assert abm_dependencia_dgi.search_item(), "No se pudo buscar el nuevo item"
    assert abm_dependencia_dgi.visualizar_item(), "No se pudo visualizar el nuevo item"
    assert abm_dependencia_dgi.modificar_item(), "No se pudo modificar el item"
    assert abm_dependencia_dgi.search_item(), "No se pudo buscar el nuevo item"
    assert abm_dependencia_dgi.eliminar_item(), "No se pudo eliminar el item"


