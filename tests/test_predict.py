import sys
import unittest

import predict


class PredictCompatibilityTests(unittest.TestCase):
    def test_ensure_numpy_compat_registers_numpy_core(self):
        sys.modules.pop("numpy._core", None)

        result = predict.ensure_numpy_compat()

        self.assertTrue(result)
        self.assertIn("numpy._core", sys.modules)


if __name__ == "__main__":
    unittest.main()
