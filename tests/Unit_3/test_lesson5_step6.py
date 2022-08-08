"""
    Найдите там параметр, который в случае неожиданного прохождения теста, помеченного как xfail, 
    отметит в отчете этот тест как упавший. Пометьте таким образом первый тест из этого тестового набора.

    @pytest.mark.xfail(strict=True)
    
    pytest -rX -v Unit_3\test_lesson5_step6.py
    
    https://docs.pytest.org/en/latest/reference/reference.html?highlight=xfail#pytest.mark.xfail
"""

import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
