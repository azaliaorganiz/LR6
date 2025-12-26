import pytest
import purchase_analyzer

@pytest.fixture
def sample_file():
    return 'test.txt'

def test_read_valid_purchases(sample_file):
    purchases = purchase_analyzer.read_purchases(sample_file)
    assert len(purchases) == 3
    assert purchases[0]['name'] == 'Bread'
    assert purchases[1]['name'] == 'Mouse'


def test_skip_bad_lines(sample_file):
    purchases = purchase_analyzer.read_purchases(sample_file)
    for purchase in purchases:
        assert purchase['name'] != ''
        assert purchase['price'] > 0
        assert purchase['qty'] > 0
    assert len(purchases) == 3



def test_count_errors(sample_file):
    errors = purchase_analyzer.count_errors(sample_file)
    assert errors == 3

def test_total_spent(sample_file):
    purchases = purchase_analyzer.read_purchases(sample_file)
    total = purchase_analyzer.total_spent(purchases)
    # Bread: 10*3=30, Mouse: 25*2=50, Bus: 1.5*20=30, Итого: 110
    assert total == 110.0

def test_spent_by_category(sample_file):
    purchases = purchase_analyzer.read_purchases(sample_file)
    cats = purchase_analyzer.spent_by_category(purchases)
    assert cats['food'] == 30.0
    assert cats['tech'] == 50.0
    assert cats['transport'] == 30.0

def test_top_n_expensive(sample_file):
    purchases = purchase_analyzer.read_purchases(sample_file)
    top = purchase_analyzer.top_n_expensive(purchases, n=2)
    assert len(top) == 2
    assert top[0]['name'] == 'Mouse'  # 50 - самая дорогая
    assert top[0]['price'] * top[0]['qty'] == 50.0
