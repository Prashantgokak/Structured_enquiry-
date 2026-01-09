# test_student.py

from student import calculate_average, assign_grade

# -------- GRADE S --------
def test_grade_S_lower():
    assert assign_grade(calculate_average(90, 90, 90)) == "S"

def test_grade_S_middle():
    assert assign_grade(calculate_average(95, 95, 95)) == "S"

def test_grade_S_upper():
    assert assign_grade(calculate_average(100, 100, 100)) == "S"


# -------- GRADE A --------
def test_grade_A_lower():
    assert assign_grade(calculate_average(80, 80, 80)) == "A"

def test_grade_A_middle():
    assert assign_grade(calculate_average(85, 85, 85)) == "A"

def test_grade_A_upper():
    assert assign_grade(calculate_average(89.99, 89.99, 89.99)) == "A"


# -------- GRADE B --------
def test_grade_B_lower():
    assert assign_grade(calculate_average(65, 65, 65)) == "B"

def test_grade_B_middle():
    assert assign_grade(calculate_average(72, 72, 72)) == "B"

def test_grade_B_upper():
    assert assign_grade(calculate_average(79.99, 79.99, 79.99)) == "B"


# -------- GRADE C --------
def test_grade_C_lower():
    assert assign_grade(calculate_average(50, 50, 50)) == "C"

def test_grade_C_middle():
    assert assign_grade(calculate_average(58, 58, 58)) == "C"

def test_grade_C_upper():
    assert assign_grade(calculate_average(64.99, 64.99, 64.99)) == "C"


# -------- GRADE D --------
def test_grade_D_lower():
    assert assign_grade(calculate_average(40, 40, 40)) == "D"

def test_grade_D_middle():
    assert assign_grade(calculate_average(45, 45, 45)) == "D"

def test_grade_D_upper():
    assert assign_grade(calculate_average(49.99, 49.99, 49.99)) == "D"


# -------- GRADE F --------
def test_grade_F():
    assert assign_grade(calculate_average(30, 30, 30)) == "F"
