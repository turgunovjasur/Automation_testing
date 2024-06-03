import time
from time import sleep
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.appiumby import AppiumBy


class Screen:
    def __init__(self, driver):
        """
        Screen klassining konstruktori. WebDriver obyektini oladi.
        :param driver: WebDriver obyektini oladi.
        """
        self.driver = driver

    # def check_platform_version(self):
    #     if self.driver.capabilities["platformVersion"] == "10.0":
    #         print("*************PLATFORM VERSION - ", self.driver.capabilities["platformVersion"])
    #         return 10.0
    #     else:
    #         return 11.0

    # get elements
    def get_element(self, locator):
        """
        Berilgan lokator bo'yicha bitta elementi oladi.
        :param locator: Lokator (method, value) tuple.
        :return: WebElement.
        """
        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_element_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_element_by_type(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_element_by_pasted_data(self, locator, data):
        """
        Berilgan lokator va ma'lumot bo'yicha bitta elementi oladi.
        :param locator: Lokator (method, value) tuple.
        :param data: Formatlanadigan ma'lumot.
        :return: WebElement.
        """
        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_element_by_type(method, values.format(data))
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_element_by_type(method, value.format(data))
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_element_by_type(self, method, value):
        """
        Lokator turi va qiymati bo'yicha elementi oladi.
        :param method: Lokator turi.
        :param value: Lokator qiymati.
        :return: WebElement.
        """
        if method == 'accessibility_id':
            return WebDriverWait(self.driver, timeout=70).until(ec.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, value)))
        elif method == 'android':
            return WebDriverWait(self.driver, timeout=70).until(ec.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, value)))
        elif method == 'ios':
            return WebDriverWait(self.driver, timeout=70).until(ec.element_to_be_clickable((AppiumBy.IOS_UIAUTOMATION, value)))
        elif method == 'class_name':
            return WebDriverWait(self.driver, timeout=78).until(ec.element_to_be_clickable((AppiumBy.CLASS_NAME, value)))
        elif method == 'id':
            return WebDriverWait(self.driver, timeout=70).until(ec.visibility_of_element_located((AppiumBy.ID, value)))
        elif method == 'xpath':
            return WebDriverWait(self.driver, timeout=70).until(ec.visibility_of_element_located((AppiumBy.XPATH, value)))
        elif method == 'name':
            return WebDriverWait(self.driver, timeout=70).until(ec.element_to_be_clickable((AppiumBy.NAME, value)))
        elif method == 'class_chain':
            return WebDriverWait(self.driver, timeout=70).until(ec.visibility_of_element_located((AppiumBy.IOS_CLASS_CHAIN, value)))
        elif method == 'predicate':
            return WebDriverWait(self.driver, timeout=70).until(ec.element_to_be_clickable((AppiumBy.IOS_PREDICATE, value)))
        else:
            raise Exception('Invalid Locator method.')

    def get_elements(self, locator):
        """
        Berilgan lokator bo'yicha barcha elementlarni oladi.
        :param locator: Lokator (method, value) tuple.
        :return: WebElementlar ro'yxati.
        """
        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_elements_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_elements_by_type(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_elements_by_type(self, method, value):
        """
        Lokator turi va qiymati bo'yicha barcha elementlarni oladi.
        :param method: Lokator turi.
        :param value: Lokator qiymati.
        :return: WebElementlar ro'yxati.
        """
        if method == 'accessibility_id':
            return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, value)))
        elif method == 'android':
            return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.ANDROID_UIAUTOMATOR, value)))
        elif method == 'ios':
            time.sleep(2)
            return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.IOS_UIAUTOMATION, value)))
            # return self.driver.find_elements(MobileBy.IOS_UIAUTOMATION, value)
        elif method == 'class_name':
            time.sleep(3)
            # return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.CLASS_NAME, value)))
            return self.driver.find_elements(AppiumBy.CLASS_NAME, value)
        elif method == 'id':
            time.sleep(2)
            return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.ID, value)))
            # return self.driver.find_elements(MobileBy.ID, value)
        elif method == 'xpath':
            time.sleep(2)
            return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.XPATH, value)))
            # return self.driver.find_elements(MobileBy.XPATH, value)
        elif method == 'name':
            return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.NAME, value)))
        elif method == 'class_chain':
            return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.IOS_CLASS_CHAIN, value)))
        elif method == 'predicate':
            return WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_all_elements_located((AppiumBy.IOS_PREDICATE, value)))
        else:
            raise Exception('Invalid locator method.')

    def is_visible(self, locator):
        """
        Element ko'rinadiganligini tekshirish.
        :param locator: Lokator (method, value) tuple.
        :return: True agar ko'rinadigan bo'lsa, aks holda False.
        """
        try:
            return self.get_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    def is_visible_by_pasted_data(self, locator, data):
        """
        Element ko'rinadiganligini tekshirish (ma'lumot formatlangan holda).
        :param locator: Lokator (method, value) tuple.
        :param data: Formatlanadigan ma'lumot.
        :return: True agar ko'rinadigan bo'lsa, aks holda False.
        """
        try:
            return self.get_element_by_pasted_data(locator, data).is_displayed()
        except NoSuchElementException:
            return False

    def is_visible_item(self, locator, index):
        """
        Element ro'yxatidagi ma'lum indeksdagi element ko'rinadiganligini tekshirish.
        :param locator: Lokator (method, value) tuple.
        :param index: Element indeksini olish.
        :return: True agar ko'rinadigan bo'lsa, aks holda False.
        """
        try:
            return self.get_elements(locator)[index].is_displayed()
        except (NoSuchElementException, IndexError):
            return False

    def is_present(self, locator):
        """
        Element mavjudligini tekshirish.
        :param locator: Lokator (method, value) tuple.
        :return: True agar mavjud bo'lsa, aks holda False.
        """
        try:
            self.get_element(locator)
            return True
        except NoSuchElementException:
            sleep(1)
            return False

    def wait_visible(self, locator):
        """
        Element ko'rinadigan bo'lgunga qadar kutish.
        :param locator: Lokator (method, value) tuple.
        :return: WebElement.
        """
        try:
            if self.is_visible(locator):
                return self.get_element(locator)
            else:
                sleep(1)
        except NoSuchElementException:
            sleep(1)

        raise Exception('Element never became visible: %s (%s)' % (locator[0], locator[1]))

    def wait_visible_item(self, locator, index):
        """
        Element ro'yxatidagi ma'lum indeksdagi element ko'rinadigan bo'lgunga qadar kutish.
        :param locator: Lokator (method, value) tuple.
        :param index: Element indeksini olish.
        :return: WebElement.
        """
        try:
            if self.is_visible_item(locator, index):
                return self.get_elements(locator)[index]
            else:
                sleep(1)
        except (NoSuchElementException, IndexError):
            sleep(1)

        raise Exception('Element never became visible: %s (%s[%s])' % (locator[0], locator[1], index))

    def wait_for_text(self, locator, text, try_count=50):
        """
        Element matni ko'rinadigan bo'lgunga qadar kutish.
        :param locator: Lokator (method, value) tuple.
        :param text: Kutilayotgan matn.
        :param try_count: Sinovlar soni.
        :return: True agar matn ko'rinadigan bo'lsa, aks holda Exception.
        """
        for i in range(try_count):
            try:
                element = self.get_element(locator)
                element_text = element.text
                print(element_text)
                if element_text.lower() == text.lower():
                    return True
                else:
                    pass
            except (NoSuchElementException, StaleElementReferenceException):
                pass
            sleep(1)

        raise Exception('Element text never became visible: %s (%s) - %s' % (locator[0], locator[1], text))

    def wait_for_text_item(self, locator, text):
        """
        Element ro'yxatidagi matnni kutish.
        :param locator: Lokator (method, value) tuple.
        :param text: Kutilayotgan matn.
        :return: True agar matn ko'rinadigan bo'lsa, aks holda Exception.
        """
        try:
            elements = self.get_elements(locator)
            for element in elements:
                if text in element.text:
                    return True
            sleep(1)
        except (NoSuchElementException, StaleElementReferenceException):
            sleep(1)

        raise Exception('Text never became visible: %s' % text)

    def click(self, locator):
        """
        Elementni bosish.
        :param locator: Lokator (method, value) tuple.
        """
        element = self.get_element(locator)
        element.click()

    def click_by_pasted_data(self, locator, data):
        """
        Elementni bosish (ma'lumot formatlangan holda).
        :param locator: Lokator (method, value) tuple.
        :param data: Formatlanadigan ma'lumot.
        """
        element = self.get_element_by_pasted_data(locator, data)
        element.click()

    def click_on_item(self, locator, index):
        """
        Element ro'yxatidagi ma'lum indeksdagi elementni bosish.
        :param locator: Lokator (method, value) tuple.
        :param index: Element indeksini olish.
        """
        element = self.wait_visible_item(locator, index)
        element.click()

    def clear_text(self, locator):
        """
        Element matnini tozalash.
        :param locator: Lokator (method, value) tuple.
        """
        element = self.wait_visible(locator)
        element.clear()

    def clear_text_on_item(self, locator, index):
        """
        Element ro'yxatidagi ma'lum indeksdagi element matnini tozalash.
        :param locator: Lokator (method, value) tuple.
        :param index: Element indeksini olish.
        """
        element = self.wait_visible_item(locator, index)
        element.clear()

    def get_element_text_by_pasted_data(self, locator, data):
        """
        Element matnini olish (ma'lumot formatlangan holda).
        :param locator: Lokator (method, value) tuple.
        :param data: Formatlanadigan ma'lumot.
        :return: Element matni.
        """
        element = self.get_element_by_pasted_data(locator, data)
        print("Selected element text (with pasted data) : ", element.text)
        return element.text

    def get_element_text(self, locator):
        """
        Element matnini olish.
        :param locator: Lokator (method, value) tuple.
        :return: Element matni.
        """
        element = self.get_element(locator)
        print("Selected element text : ", element.text)
        return element.text

    def enter_data(self, locator, text):
        """
        Elementga matn kiritish.
        :param locator: Lokator (method, value) tuple.
        :param text: Kiritiladigan matn.
        """
        element = self.get_element(locator)
        element.send_keys(text)

    def enter_data_to_item(self, locator, text, index):
        """
        Element ro'yxatidagi ma'lum indeksdagi elementga matn kiritish.
        :param locator: Lokator (method, value) tuple.
        :param text: Kiritiladigan matn.
        :param index: Element indeksini olish.
        """
        element = self.wait_visible_item(locator, index)
        element.send_keys(text)

    def long_press(self, locator, duration=1000):
        """
        Elementni uzoq bosish.
        :param locator: Lokator (method, value) tuple.
        :param duration: Bosish davomiyligi.
        """
        element = self.get_element(locator)
        action = TouchAction(self.driver)
        action.long_press(element, x=None, y=None, duration=duration).perform()

    def long_press_and_swipe(self, x1, y1, x2, y2, duration=1000):
        """
        Berilgan koordinatalarda uzoq bosish va surish.
        :param x1: Bosish boshlanish koordinatasi.
        :param y1: Bosish boshlanish koordinatasi.
        :param x2: Surish tugash koordinatasi.
        :param y2: Surish tugash koordinatasi.
        :param duration: Bosish davomiyligi.
        """
        action = TouchAction(self.driver)
        action.long_press(el=None, x=x1, y=y1, duration=duration).move_to(el=None, x=x2, y=y2).release().perform()

    def press_keycode(self, key_code):
        """
        Berilgan kalit kodini bosish.
        :param key_code: Kalit kodi.
        """
        self.driver.press_keycode(key_code)

    def get_element_attributes(self, locator):
        """
        Element atributlarini olish.
        :param locator: Lokator (method, value) tuple.
        :return: Atributlar lug'ati.
        """
        element = self.get_element(locator)
        return {
            'top': element.location['y'],
            'bottom': element.location['y'] + element.size['height'],
            'left': element.location['x'],
            'right': element.location['x'] + element.size['width'],
            'center_x': (element.size['width'] / 2) + element.location['x'],
            'center_y': (element.size['height'] / 2) + element.location['y'],
        }

    def pull_to_refresh(self, locator, duration=1000):
        """
        Elementni tortib yangilash.
        :param locator: Lokator (method, value) tuple.
        :param duration: Surish davomiyligi.
        """
        scrollable_element_attributes = self.get_element_attributes(locator)
        self.driver.swipe(
            scrollable_element_attributes['center_x'],
            scrollable_element_attributes['top'] + 1,
            scrollable_element_attributes['center_x'],
            scrollable_element_attributes['bottom'] - 1,
            duration
        )

    def swipe_to_left_side_of_screen(self, locator, duration=1000):
        """
        Ekranning chap tomoniga surish.
        :param locator: Lokator (method, value) tuple.
        :param duration: Surish davomiyligi.
        """
        scrollable_element_attributes = self.get_element_attributes(locator)
        self.driver.swipe(
            scrollable_element_attributes['center_x'],
            scrollable_element_attributes['right'] + 1,
            scrollable_element_attributes['center_x'],
            scrollable_element_attributes['left'] - 1,
            duration
        )

    def refresh_screen(self, x, y):
        """
        Ekranni yangilash.
        :param x: Bosish boshlanish koordinatalari.
        :param y: Bosish boshlanish koordinatalari.
        """
        actions = TouchAction(self.driver)
        actions.press(x=x[0], y=y[0]).move_to(x=x[1], y=y[1]).release().perform()

    def tap_on_by_coordinate(self, a):
        """
        Berilgan koordinatalarga bosish.
        :param a: Koordinatalar.
        """
        actions = TouchAction(self.driver)
        actions.tap(x=a[0], y=a[1]).perform()

    def hide_keyboard(self):
        """
        Klaviaturani yashirish.
        """
        try:
            sleep(1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def new_scroll(self, x1, y1, x2, y2):
        """
        Berilgan koordinatalar bo'yicha surish.
        :param x1: Bosish boshlanish koordinatasi.
        :param y1: Bosish boshlanish koordinatasi.
        :param x2: Surish tugash koordinatasi.
        :param y2: Surish tugash koordinatasi.
        """
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2)

    def new_scroll_with_duration(self, x1, y1, x2, y2, duration=800):
        """
        Berilgan koordinatalar bo'yicha surish (davomiyligi bilan).
        :param x1: Bosish boshlanish koordinatasi.
        :param y1: Bosish boshlanish koordinatasi.
        :param x2: Surish tugash koordinatasi.
        :param y2: Surish tugash koordinatasi.
        :param duration: Surish davomiyligi.
        """
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, duration=duration)
