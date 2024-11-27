from stairmaster import climb_stairs

def test_1_step():
    assert climb_stairs(1) == 1

def test_2_step():
    assert climb_stairs(2) == 2

def test_3_step():
    assert climb_stairs(3) == 3

def test_10_step():
    assert climb_stairs(10) == 89

def test_30_step():
    assert climb_stairs(30) == 1346269

def test_35_step():
    assert climb_stairs(35) == 14930352

# def test_40_step():
#     assert climb_stairs(40) == 165580141

# def test_50_step():
#     assert climb_stairs(50) == 20365011074
