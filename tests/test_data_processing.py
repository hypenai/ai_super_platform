import unittest
import numpy as np
from src.data_processing import preprocess_data, QuantumInspiredPreprocessor

class TestDataProcessing(unittest.TestCase):
    def test_preprocess_data(self):
        processed_data = preprocess_data()
        self.assertIsNotNone(processed_data)
        self.assertIsInstance(processed_data, np.ndarray)

    def test_quantum_inspired_preprocessor(self):
        qip = QuantumInspiredPreprocessor(dimension=100)
        data = np.random.rand(10, 100)
        transformed_data = qip.transform(data)
        self.assertEqual(transformed_data.shape, data.shape)

if __name__ == '__main__':
    unittest.main()
