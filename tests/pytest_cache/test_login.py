from tests.pytest_cache.initial_test import InitialTest


class TestLogin(InitialTest):
    def tset_login(self, init):
        assert self.login_f.check_login("966026869", "1234567abcd*")
