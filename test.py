import unittest
from metristic import METRICSTICS

class TestMETRICSTICS(unittest.TestCase):

    def setUp(self):
        # Create test data for each test case
        self.data = [1, 2, 3, 4, 5]
        self.metrics = METRICSTICS(self.data)

    def test_mean(self):
        self.assertEqual(self.metrics.mean(), 3.0)

    def test_median(self):
        self.assertEqual(self.metrics.median(), 3)

    def test_mode(self):
        self.assertEqual(self.metrics.mode(), [1, 2, 3, 4, 5])

    def test_standard_deviation(self):
        self.assertAlmostEqual(self.metrics.standard_deviation(), 1.5811, places=4)

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

    def test_negative_numbers(self):
        metrics = METRICSTICS([-1, -2, -3, -4, -5])
        self.assertEqual(metrics.mean(), -3.0)
        self.assertEqual(metrics.median(), -3)
        self.assertEqual(metrics.mode(), [-5, -4, -3, -2, -1])
        self.assertAlmostEqual(metrics.standard_deviation(), 1.5811, places=4)
        self.assertEqual(metrics.mad(), 1.2)
        self.assertEqual(metrics.min_max(), (-5, -1))

    def test_floating_point_numbers(self):
        metrics = METRICSTICS([1.5, 2.5, 3.5])
        self.assertAlmostEqual(metrics.mean(), 2.5, places=4)
        self.assertAlmostEqual(metrics.median(), 2.5, places=4)
        self.assertEqual(metrics.mode(), [1.5, 2.5, 3.5])
        self.assertAlmostEqual(metrics.standard_deviation(), 0.8165, places=4)
        self.assertAlmostEqual(metrics.mad(), 0.6667, places=4)
        self.assertEqual(metrics.min_max(), (1.5, 3.5))

    def test_duplicate_values(self):
        metrics = METRICSTICS([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
        self.assertAlmostEqual(metrics.mean(), 3.0)
        self.assertEqual(metrics.median(), 3)
        self.assertEqual(metrics.mode(), [3, 4, 5])
        self.assertAlmostEqual(metrics.standard_deviation(), 1.0, places=4)
        self.assertAlmostEqual(metrics.mad(), 0.8, places=4)
        self.assertEqual(metrics.min_max(), (1, 5))

    def test_large_data_set(self):
        data = list(range(1, 10001))
        metrics = METRICSTICS(data)
        self.assertEqual(metrics.mean(), 5000.5)
        self.assertEqual(metrics.median(), 5000)
        self.assertEqual(metrics.mode(), [1])
        self.assertAlmostEqual(metrics.standard_deviation(), 2886.8956, places=4)
        self.assertAlmostEqual(metrics.mad(), 2886.5, places=4)
        self.assertEqual(metrics.min_max(), (1, 10000))

    def test_mixed_data_types(self):
        metrics = METRICSTICS([1, 2, 3, 4, "5"])
        with self.assertRaises(TypeError):
            metrics.mean()
        with self.assertRaises(TypeError):
            metrics.median()
        with self.assertRaises(TypeError):
            metrics.mode()
        with self.assertRaises(TypeError):
            metrics.standard_deviation()
        with self.assertRaises(TypeError):
            metrics.mad()
        with self.assertRaises(TypeError):
            metrics.min_max()

if __name__ == '__main__':
    unittest.main()