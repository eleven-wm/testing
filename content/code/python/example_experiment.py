def add(a, b):
    # 修复：改回正确的加法
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def test_add_zero():
    """测试：任何数加零都等于它本身"""
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 5) == 5
    assert add(-3, 0) == -3
def test_add_negative():
    """测试：负数加法"""
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2
    assert add(3, -5) == -2