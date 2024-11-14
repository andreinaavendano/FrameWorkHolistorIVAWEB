import pytest
import allure
from pages.PDE.home_page_holistor_pde import HomePageHolistorPDE


@pytest.fixture
def home_page_holistor_pde(browser, base_url, datos_usuario):
    return HomePageHolistorPDE(browser, base_url, datos_usuario)

@allure.suite("Casos de prueba Home page")
@allure.epic("Home Page")
@allure.feature("Abrir la Master page de PDE")
@allure.story("US: MP PDE")
@allure.testcase("TC - 0001")
@allure.title("Carga de la APP PDE")
@allure.description("Este test verifica que se luego de hacer login en plataforma se "
                    "puede abrir PDE si esta habilitado para el usuario y tenant.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.homepde
@pytest.mark.regresion
def test_pde_home_page(home_page_holistor_pde):
    with allure.step("Navegar en la pagina de inicio de plataforma con "
                     "los datos correctos en los campos Tenant, Usuario, Contraseña"):
        home_page_holistor_pde.navegar_plataforma()

    with allure.step("Si el el boton PDE esta visible"):
        visible = home_page_holistor_pde.is_pde_tenant()
        assert visible, "El Tenant no tiene la APP SYJ"

    with allure.step("Si la APP está habilitada para el usuario/tenant"):
        hailitado = home_page_holistor_pde.is_pde_user_enabled()
        assert not hailitado, "SYJ no esta habilitado para este Tenant/usuario"

    with allure.step("Hacemos clic en el botón para cargar MP"):
        assert home_page_holistor_pde.open_pde(), "La master page SYJ no se carga correctamente."

    with allure.step("Podemos verificar que efectivamente se abre la MP de SYJ con el titulo y url esperado"):
        titulo_actual = home_page_holistor_pde.title_page()
        url_actual = home_page_holistor_pde.get_current_url()
        assert titulo_actual in 'Home', "El titulo de la pagina actual no se corresponde con el esperado"
        assert url_actual in 'https://pde-qa.holistorsaas.com.ar/agenda.home.aspx' \
            , "La URL actual no se corresponde con la esperada"

