import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from allure_commons.types import AttachmentType


# Fixture: Test muvaffaqiyatsiz bo'lsa, screenshot oladi
@pytest.fixture()
def get_screenshot_on_failed_case(request):
    yield  # Test bajarilishini kutadi
    item = request.node  # Test nodeni oladi
    if item.rep_call.failed:  # Agar test muvaffaqiyatsiz bo'lsa
        # Screenshotni olish va Allure hisobotiga qo'shish
        allure.attach(request.instance.driver.get_screenshot_as_png(),
                      name="failed_test",
                      attachment_type=AttachmentType.PNG)

# Hook: Test natijasini saqlash uchun ishlatiladi
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield  # Hookning ishlashini davom ettiradi
    rep = outcome.get_result()  # Test natijasini oladi
    # Testning turiga qarab natijani saqlaydi (setup, call, teardown)
    setattr(item, "rep_" + rep.when, rep)
    return rep  # Natijani qaytaradi


# Fixture: Virtual devaysni sozlash
@pytest.fixture()
def setup_virtual_device(request):
    global driver  # Global driver o'zgaruvchisini e'lon qiladi
    capabilities = {
        "platformName": "Android",  # Platforma nomi
        "platformVersion": "10.0",  # Platforma versiyasi
        "deviceName": "Pixel_XL_API_10.0",  # Qurilma nomi
        "avd": "Pixel_XL_API_10.0",  # AVD nomi
        "avdReadyTimeout": "650000",  # AVD tayyor bo'lish vaqti
        "automationName": "uiautomator2",  # Avtomatlashtirish vositasi
        "app": "C:\\Users\\User\\Desktop\\ish\\Automation_testing\\apps\\Trastpay_1.1.29",  # Ilova manzili
        "appPackage": "trastpay.uz",  # Ilova paketi nomi
        "appActivity": "uz.trastpay.ui.activity.MainActivity",  # Ilova asosiy faolligi
        "noReset": "True",  # Qurilmani qayta o'rnatmaslik
        "adbExecTimeout": "650000",  # ADB bajarish vaqti
        "newCommandTimeout": "3600"  # Yangi buyruq vaqti
    }

    appium_server = AppiumService()  # Appium serverini ishga tushirish uchun ob'ekt yaratish
    appium_server.start(
        args=[
            '--address', '127.0.0.1',  # Appium server manzili
            '--port', '4723',  # Appium server porti
            '--base-path', '/wd/hub',  # Appium bazasi yo'li
        ]
    )

    request.addfinalizer(appium_server.stop)  # Test tugagach, Appium serverni to'xtatish
    url = 'http://127.0.0.1:4723/wd/hub'  # Appium server URL manzili
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)  # Parametrlarni yuklash
    request.instance.driver = webdriver.Remote(url, options=capabilities_options)  # Appium serverga ulanish

    # Teardown funksiyasi: Test tugagach, driverni to'xtatish
    def teardown():
        request.instance.driver.quit()  # Driverni to'xtatish
    request.addfinalizer(teardown)  # Teardown funksiyasini finalizerga qo'shish














