import unittest
import numpy as np
import sys
import os
import  urllib

import sidpy

sys.path.insert(0, "../../../")
usid_available = False
try:
    from SciFiReaders import Usid_reader
except ImportError:
    usid_available = True
from sidpy.sid.dataset import Dataset 
import glob


class TestUSIDReader(unittest.TestCase):
    
    def test_data_available(self):
        if usid_available:
            urllib.request.urlretrieve(r'https://www.dropbox.com/scl/fi/ggvatabim4zgbcie4yddm/HfOx_-2V_0001.h5?rlkey=rzwdutxnyb0gwu2cw3cmrjst4&dl=1', './relax_test_data.h5')
            reader = Usid_reader('relax_test_data.h5')
            self.assertIsInstance(reader, sidpy.Reader)
    
    def test_read_ndim_issue(self):
        if usid_available:
            urllib.request.urlretrieve(r'https://www.dropbox.com/scl/fi/ggvatabim4zgbcie4yddm/HfOx_-2V_0001.h5?rlkey=rzwdutxnyb0gwu2cw3cmrjst4&dl=1', './relax_test_data.h5')
            reader = Usid_reader('relax_test_data.h5')
            datasets = reader.read()
            assert isinstance(datasets, Dataset)
            h5_files = glob.glob('*.h5')
            for file_name in h5_files:
                os.remove(file_name)
            
    
if __name__ == '__main__':
    unittest.main()
    
        
        