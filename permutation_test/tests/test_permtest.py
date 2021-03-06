from unittest import TestCase
from ..functions import permutationtest
import numpy as np
import pandas as pd
import permutation_test.csv_parser as csv_parser
import permutation_test.permtest as permtest

class TestPermtest(TestCase):
    

    def test_get_data_name(self):
        treatment_names = ['mutant', 'WT']
        val= 'WT'
        ref_data_name = 'mutant'
        data_name = permtest.get_data_name(treatment_names, ref_data_name)
        self.assertEqual(data_name, val)

        val= 'mutant'
        ref_data_name = 'WT'
        data_name = permtest.get_data_name(treatment_names, ref_data_name)
        self.assertEqual(data_name, val)

    def test_get_data_2(self):
        treatment_names = ['mutant', 'WT', 'mu2']
        val= 'WT'
        ref_data_name = 'mutant'
        self.assertIsNone(permtest.get_data_name(treatment_names, ref_data_name))

    def test_get_data_3(self):
        treatment_names = ['mutant', 'WT']
        val= 'WT'
        ref_data_name = 'mu3'
        permtest.get_data_name(treatment_names, ref_data_name)
        self.assertIsNone(permtest.get_data_name(treatment_names, ref_data_name))
    
    def test_batch_permtest(self):
        dat = {'exp1' : { 'wt' : [1, 3, 0, 4], 'mutant' : [2, 4]}\
            , 'exp2' : { 'wt' : [1, 3, 0, 4], 'mutant' : [2, 4]}\
            }

        data_name = 'mutant'
        ref_data_name = 'wt'    
        res = permtest.batch_permtest(dat, data_name, ref_data_name, verbose=True)
        
        print(res)
        self.assertEqual(res[0]['p_value'], 0.33333333333333337)


    def test_permtest_with_err(self):
        ref_data = [(-1,0.1),(0,0.1),(0,0.1),(1,0.1), (3, 0.1), (3, 0.1), (4, 0.1)]
        data =  [(2, 0.1), (4, 0.1), (4, 0.1), (5, 0.1), (5, 0.1), (6, 0.1)]


        print('with err')    
        res_err = permutationtest(data, ref_data, verbose=True, n_bins=None)    
 
        
        ref_data = [-1, 0, 0, 1, 3, 3, 4]
        data =  [2, 4, 4, 5, 5, 6]


        print('no err')    
        res = permutationtest(data, ref_data, verbose=True, n_bins=None)    


        self.assertTrue(res[0]['p_value'] > 0.33333333333333337)    
    