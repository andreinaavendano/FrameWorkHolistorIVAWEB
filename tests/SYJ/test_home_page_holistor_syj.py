import pytest
import allure
from pages.SYJ.home_page_holistor_syj import HomePageHolistorSYJ


@pytest.fixture
def home_page_holistor_syj(browser, base_url, datos_usuario):
    return HomePageHolistorSYJ(browser, base_url, datos_usuario)

@allure.suite("Casos de prueba Home page")
@allure.epic("Home Page")
@allure.feature("Abrir la Master page de SYJ")
@allure.story("US: MP SYJ")
@allure.testcase("TC - 0001")
@allure.title("Carga de la APP SYJ")
@allure.description("Este test verifica que se luego de hacer login en plataforma se "
                    "puede abrir SYJ si esta habilitado para el usuario y tenant.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.homesyj
@pytest.mark.regresion
def test_syj_home_page(home_page_holistor_syj):
    with allure.step("Navegar en la pagina de inicio de plataforma con "
                     "los datos correctos en los campos Tenant, Usuario, Contraseña"):
        home_page_holistor_syj.navegar_plataforma()

    with allure.step("Si el el boton SYJ esta visible"):
        visible = home_page_holistor_syj.is_SYJ_tenant()
        assert visible, "El Tenant no tiene la APP SYJ"

    with allure.step("Si la APP está habilitada para el usuario/tenant"):
        hailitado = home_page_holistor_syj.is_SYJ_user_enabled()
        assert not hailitado, "SYJ no esta habilitado para este Tenant/usuario"

    with allure.step("Hacemos clic en el botón para cargar MP"):
        assert home_page_holistor_syj.open_syj(), "La master page SYJ no se carga correctamente."

    with allure.step("Podemos verificar que efectivamente se abre la MP de SYJ con el titulo y url esperado"):
        titulo_actual = home_page_holistor_syj.title_page()
        url_actual = home_page_holistor_syj.get_current_url()
        assert titulo_actual in 'Home', "El titulo de la pagina actual no se corresponde con el esperado"
        assert url_actual in 'https://syj-qa.holistorsaas.com.ar/home.aspx' \
            , "La URL actual no se corresponde con la esperada"

