from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsszeg(TestCase):
    def test_feladat07(self):
        aktualis = feladatok.feladat07()
        elvart = 4
        self.assertEqual(elvart, aktualis, "A legtovább tartó fagyos napok számát nem jól határozta meg!")
