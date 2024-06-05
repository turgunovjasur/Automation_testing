from flows.android_flow.android_base_flow import AndroidBaseFlow
from screens.android.welcome_screen import HomeScreen
from screens.android.welcome_screen import WelcomeScreen
import time


class AppLockTimeFlow(AndroidBaseFlow):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.welcome_screen = WelcomeScreen(driver)
        self.home_screen = HomeScreen(driver)

    def check_app_lock_time(self):
        self.install_application(False)
        time.sleep(5)
        self.welcome_screen.is_enter_pin_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.home_screen.click_on_profile_icon()
