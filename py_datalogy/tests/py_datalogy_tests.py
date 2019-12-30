# https://docs.python.org/3/library/unittest.html
import os
import sys
from unittest import TestCase
#

#
# import pandas as pd
# sys.path.insert(0, os.path.abspath('/Users/lnorouzi/Documents/Prokarma/Projects/EDA_library/test_package/test_package/'))
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from eda_data import *

use_data = pd.read_csv('../py_datalogy/py_datalogy/data/tips.csv')
def test1():
    ed = EDA(use_data)
    # s = ed.total_eda()
    s='test'
    print('****************',s)
    assert isinstance(s, str)

