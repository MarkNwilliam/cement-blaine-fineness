import unittest
from blaine import surface_from_reference, surface_direct


class TestSurfaceFromReference(unittest.TestCase):
    def test_example(self):
        # reference 3200 cm2/g, ref_time 45, sample 52s, K=1 -> ~3697
        s = surface_from_reference(3200, 45, 52, 1.0, 1.0)
        self.assertAlmostEqual(s, 3697.78, places=1)

    def test_zero_time_raises(self):
        with self.assertRaises(ValueError):
            surface_from_reference(3200, 0, 52, 1.0, 1.0)

    def test_identity(self):
        # same time as reference -> returns reference surface
        s = surface_from_reference(3200, 45, 45, 1.0, 1.0)
        self.assertAlmostEqual(s, 3200, places=9)


class TestSurfaceDirect(unittest.TestCase):
    def test_positive(self):
        s = surface_direct(3.15, 52, 0.5)
        self.assertGreater(s, 0)

    def test_invalid_porosity(self):
        with self.assertRaises(ValueError):
            surface_direct(3.15, 52, 1.0)


if __name__ == "__main__":
    unittest.main()
