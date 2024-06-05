from tests.pytest_cache.initial_test import InitialTest


class TestAppLockTime(InitialTest):
    def test_app_lock_time(self, init):
        assert self.app_lock_time_f.check_app_lock_time()