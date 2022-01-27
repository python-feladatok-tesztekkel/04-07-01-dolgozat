from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsszeg(TestCase):
    def test_feladat04(self):
        aktualis = feladatok.feladat04()
        elvart = 8
        self.assertEqual(elvart, aktualis, "A 100 legközelebbi számot nem jól határozta meg!")
