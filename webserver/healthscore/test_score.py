import unittest
from typing import List
import flask
from healthscore import score
import score

class T1_score(unittest.TestCase):
    def test_max_score(self):
        answer_list = (['1','1','1','1','1','0','0','0','3','4','500','95'])
        self.assertEqual(score.calculate_score(answer_list),50)



if __name__ == '__main__':
    unittest.main()