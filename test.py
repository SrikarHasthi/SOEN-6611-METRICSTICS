import unittest
from metristic import METRICSTICS

class TestMETRICSTICS(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.metrics = METRICSTICS(self.data)

    def test_mean(self):
        self.assertEqual(self.metrics.mean(), 3.0)

    def test_median(self):
        self.assertEqual(self.metrics.median(), 3)

    def test_mode(self):
        self.assertEqual(self.metrics.mode(), [1, 2, 3, 4, 5])

    def test_standard_deviation(self):
        self.assertAlmostEqual(self.metrics.standard_deviation(), 1.4142, places=4)

    def test_mad(self):
        self.assertEqual(self.metrics.mad(), 1.2)

    def test_min_max(self):
        self.assertEqual(self.metrics.min_max(), (1, 5))

    def test_empty_data(self):
        metrics = METRICSTICS([])
        self.assertEqual(metrics.mean(), 0)
        self.assertIsNone(metrics.median())
        self.assertEqual(metrics.mode(), [])
        self.assertEqual(metrics.standard_deviation(), 0)
        self.assertEqual(metrics.mad(), 0)
        self.assertEqual(metrics.min_max(), (None, None))

    def test_single_data_point(self):
        metrics = METRICSTICS([5])
        self.assertEqual(metrics.mean(), 5)
        self.assertEqual(metrics.median(), 5)
        self.assertEqual(metrics.mode(), [5])
        self.assertEqual(metrics.standard_deviation(), 0)
        self.assertEqual(metrics.mad(), 0)
        self.assertEqual(metrics.min_max(), (5, 5))

    def test_even_number_data_point(self):
        metrics = METRICSTICS([1, 2, 3, 4, 5, 6])
        self.assertEqual(metrics.mean(), 3.5)
        self.assertEqual(metrics.median(), 3.5)
        self.assertEqual(metrics.mode(), [1, 2, 3, 4, 5, 6])
        self.assertAlmostEqual(metrics.standard_deviation(), 1.7078, places=4)
        self.assertEqual(metrics.mad(), 1.5)
        self.assertEqual(metrics.min_max(), (1, 6))

    def test_negative_numbers(self):
        metrics = METRICSTICS([-1, -2, -3, -4, -5])
        self.assertEqual(metrics.mean(), -3.0)
        self.assertEqual(metrics.median(), -3)
        self.assertEqual(metrics.mode(), [-5, -4, -3, -2, -1])
        self.assertAlmostEqual(metrics.standard_deviation(), 1.4142, places=4)
        self.assertEqual(metrics.mad(), 1.2)
        self.assertEqual(metrics.min_max(), (-5, -1))

    def test_duplicate_values(self):
        metrics = METRICSTICS([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
        self.assertAlmostEqual(metrics.mean(), 3.6667, places=4)
        self.assertEqual(metrics.median(), 4)
        self.assertEqual(metrics.mode(), [5])
        self.assertAlmostEqual(metrics.standard_deviation(), 1.2472, places=4)
        self.assertAlmostEqual(metrics.mad(), 1.0667, places=4)
        self.assertEqual(metrics.min_max(), (1, 5))

    def test_large_data_set(self):
        data = list(range(1, 10001))
        metrics = METRICSTICS(data)
        self.assertEqual(metrics.mean(), 5000.5)
        self.assertEqual(metrics.median(), 5000.5)
        self.assertEqual(metrics.mode(), list(range(1,10001)))
        self.assertAlmostEqual(metrics.standard_deviation(), 2886.7513, places=4)
        self.assertAlmostEqual(metrics.mad(), 2500, places=4)
        self.assertEqual(metrics.min_max(), (1, 10000))

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            metrics = METRICSTICS([1, 2, 3, 4, "5"])
        with self.assertRaises(UnboundLocalError):
            metrics.mean()
        with self.assertRaises(UnboundLocalError):
            metrics.median()
        with self.assertRaises(UnboundLocalError):
            metrics.mode()
        with self.assertRaises(UnboundLocalError):
            metrics.standard_deviation()
        with self.assertRaises(UnboundLocalError):
            metrics.mad()
        with self.assertRaises(UnboundLocalError):
            metrics.min_max()

if __name__ == '__main__':
    unittest.main()