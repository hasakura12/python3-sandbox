# ref: https://code.visualstudio.com/docs/python/testing
# pip install -U pytest
# pytest --version

import main    # The code to test

def test_increment():
    assert main.reverse([1,2,3]) == [3,2,1]
