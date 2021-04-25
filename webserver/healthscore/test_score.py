import unittest
#from typing import List
#import flask

import score

class T1_score(unittest.TestCase):
    def test_max_min_score(self):
        #test maximum score is 50
        answer_list = (['1','1','1','1','1','0','0','0','3','4','500','95'])
        self.assertEqual(score.calculate_score(answer_list),50)

        # test minimum score is less than 1
        answer_list = (['0', '0', '0', '0', '0', '1', '1', '1', '6', '2', '175', '21'])
        self.assertLess(score.calculate_score(answer_list), 1)

    def test_bmi(self):
        #tests bmi function is accurate
        #bmi = ('6','2','175')
        self.assertEqual(score.calculate_bmi(6,2,175),22.5)



if __name__ == '__main__':
    unittest.main()