import unittest
import sys
import urllib.request
import sidpy
import urllib
import os
sys.path.append("../../../../")
import SciFiReaders as sr

root_path = "https://github.com/pycroscopy/SciFiDatasets/blob/main/data/microscopy/spm/afm/"


class TestBruker(unittest.TestCase):

    def test_load_test_bruker_force_file(self):
        # Test if the force curve file can be successfully read
        file_path = 'force_bruker.001'
        urllib.request.urlretrieve(root_path + "/BrukerReader_ForceCurve_Sapphire_TAP525.001?raw=true", file_path)
        data_translator = sr.BrukerAFMReader(file_path)
        datasets = data_translator.read(verbose=False)
        assert len(datasets) == 2, "Length of dataset should be 2 but is instead {}".format(len(datasets))
        
        for ind in range(len(datasets)):
            assert type(datasets[ind])== sidpy.sid.dataset.Dataset, "Dataset No. {} not read in as sidpy dataset" \
                    "but was instead read in as {}".format(ind, type(datasets[ind]))

            assert datasets[ind].shape[0]==512, "Dataset[{}] is of size 512 but was read in as {}".format(ind, datasets[ind].shape[0])
            assert type(datasets[ind]._axes[0]) == sidpy.sid.dimension.Dimension, "Dataset should have dimension type " \
                                           "of sidpy Dimension, but is instead {}".format(type(datasets[ind]._axes))

        os.remove(file_path)

    def test_load_test_bruker_image_file(self):
        # Test if the Bruker images file can be read in correctly
        file_path = 'image_bruker.001'
        urllib.request.urlretrieve(root_path + "/BrukerReader_Image.001?raw=true", file_path)
        
        data_translator = sr.BrukerAFMReader(file_path)
        datasets = data_translator.read(verbose=True)
        
        assert len(datasets)==8, "Length of dataset should be 8 but is instead {}".format(len(datasets))
        
        for ind in range(len(datasets)):
            assert type(datasets[ind])== sidpy.sid.dataset.Dataset, "Dataset No. {} not read in as sidpy dataset" \
                    "but was instead read in as {}".format(ind, type(datasets[ind]))

            assert datasets[ind].shape==(512, 512), "Dataset[{}] is of size (256,256) but was read in as {}".format(ind, datasets[ind].shape)
            assert type(datasets[ind]._axes[0]) == sidpy.sid.dimension.Dimension, "Dataset should have dimension type " \
                                           "of sidpy Dimension, but is instead {}".format(type(datasets[ind]._axes))

        os.remove(file_path)

        
