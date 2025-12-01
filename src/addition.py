# app.py
# This is a test commit
def add(r1, r2):
    return r1 + r2

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
