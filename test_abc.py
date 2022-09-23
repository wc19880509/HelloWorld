#***********************************************
#
#      Filename: test_abc.py
#
#        Author: Chen Wanng 
#          Mail: wc19880509@gmail.com
#   Description: ---
#        Create: 2022-09-23 18:26:14
# Last Modified: 2022-09-23 18:26:14
#***********************************************

import pytest
class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")
        assert 1, "Error Image" # 断言失败```
