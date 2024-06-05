from flows.android_flow.android_base_flow import AndroidBaseFlow
from screens.android.welcome_screen import WelcomeScreen
import time


class LoginFlow(AndroidBaseFlow):

    def __init__(self, driver):
        super().__init__(driver)  # AndroidBaseFlow ning konstruktorini chaqiradi
        self.driver = driver  # Driver obyektini saqlaydi
        self.welcome_screen = WelcomeScreen(driver)  # WelcomeScreen obyektini yaratadi

    def check_login(self, phone_number, password):
        self.install_application(True)  # Ilovani o'rnatadi va avvalgi versiyasini olib tashlaydi
        time.sleep(5)  # Ilova o'rnatilishi uchun 5 soniya kutadi
        self.welcome_screen.change_lang_to_uzb()  # Ilovaning tilini o'zbek tiliga o'zgartiradi
        assert self.welcome_screen.is_welcome_screen_open()  # WelcomeScreen ochiq ekanligini tasdiqlaydi
        self.welcome_screen.enter_phone_numb(phone_number)  # Telefon raqamini kiritadi
        assert self.welcome_screen.is_kirish_screen_open()  # Kirish ekranining ochiq ekanligini tasdiqlaydi
        self.welcome_screen.enter_password(password)  # Parolni kiritadi
        self.welcome_screen.click_on_davom_etish_button()  # "Davom etish" tugmasini bosadi
        assert self.welcome_screen.is_otp_tasdiqlash_screen_open()  # OTP tasdiqlash ekranining ochiq ekanligini tasdiqlaydi
        # assert self.welcome_screen.is_entered_phone_number_exist(phone_number)  # Kiritilgan telefon raqami mavjudligini tasdiqlash uchun (izohlangan)
        time.sleep(6)  # Ilova yuklanishi uchun 6 soniya kutadi
        assert self.welcome_screen.is_welcome_screen_open()  # WelcomeScreen ochiq ekanligini yana tasdiqlaydi
        self.welcome_screen.create_pin_code()  # PIN kod yaratadi
        assert self.welcome_screen.is_confirm_pin_screen_open()  # PIN kodni tasdiqlash ekranining ochiq ekanligini tasdiqlaydi
        self.welcome_screen.create_pin_code()  # PIN kodni yana bir bor kiritadi
        assert self.welcome_screen.is_dear_user_message_appear()  # "Hurmatli foydalanuvchi" xabari chiqsa
        return True
        time.sleep(2)  # 2 soniya kutadi (lekin bu kod hech qachon ishlamaydi, chunki u `return` dan keyin keladi)
