from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsszeg(TestCase):
    def test_feladat03(self):
        aktualis = feladatok.feladat03()
        elvart = 24
        self.assertEqual(elvart, aktualis, "Az legkisebbet nem jól határozta meg!")
