from unittest import TestCase
from package1.Worker import Worker

class TestWorker(TestCase):

    def setUp(self):
        self.sagi = Worker("Sagi", "Marshel", 1950, 11, 23, "35 Dvora", "Israel")
        self.adi = Worker("Adi", "Hoe", 2020, 11, 20, "666 Hell", "Pakistan")
        self.shlomi = Worker("Shlomi", "Nahmias", 2025, 10, 7, "85 Yavne", "Egypt")
        pass

    def test_full_name(self):
        # self.assertTrue(self.sagi.full_name() == "Sagi Marshel")
        # self.assertFalse(self.adi.full_name() == "Adi Isuf")
        pass
    def test_age_past(self):
        self.assertTrue(self.sagi.age_past(),70)

    # def test_age_future(self):
    #     self.assert ("" , self.shlomi.age())
    #
    # def test_age_curent(self):
    #     self.assertEqual("0" , self.adi.age())


    def test_days_to_birthday(self):
        self.shlomi.days_to_birthday()
        print(self.shlomi.days_to_birthday())

    def test_greet(self):
        pass
    def test_location(self):
        pass

    def tearDown(self):
        print("TearDown")

    def test_age_check(self):
        pass

