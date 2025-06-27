from __future__ import division, print_function, unicode_literals, absolute_import
import unittest
import numpy as np
import sys

import sidpy
hyperspy_available = True
try:
    import hyperspy.api as hs
    import hyperspy.datasets.artificial_data as ad
except ImportError:
    hyperspy_available = False
sys.path.append("../")
import SciFiReaders


class TestHyperspy(unittest.TestCase):
    def test_signal_1d(self):
        if hyperspy_available:
            s = ad.get_low_loss_eels_signal()
            self.assertTrue(s.metadata.Signal.signal_type == 'EELS')
            dataset = SciFiReaders.convert_hyperspy(s)
            self.assertIsInstance(dataset, sidpy.Dataset)

    def test_signal_2d(self):
        if hyperspy_available:
            s = ad.get_atomic_resolution_tem_signal2d()
            dataset = SciFiReaders.convert_hyperspy(s)
            self.assertIsInstance(dataset, sidpy.Dataset)

    def test_spectral_images(self):
        if hyperspy_available:
            s = ad.get_low_loss_eels_line_scan_signal()
            self.assertTrue(s.metadata.Signal.signal_type == 'EELS')
            dataset = SciFiReaders.convert_hyperspy(s)
            self.assertIsInstance(dataset, sidpy.Dataset)

    def test_image_stack(self):
        if hyperspy_available:
            s = hs.signals.Signal2D(np.ones((3, 5, 4)))
            dataset = SciFiReaders.convert_hyperspy(s)
            self.assertIsInstance(dataset, sidpy.Dataset)

    def test_4d_images(self):
        if hyperspy_available:
            s = hs.signals.Signal2D(np.ones((3, 2, 5, 4)))
            dataset = SciFiReaders.convert_hyperspy(s)
            self.assertIsInstance(dataset, sidpy.Dataset)


if __name__ == '__main__':
    unittest.main()
