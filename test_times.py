

from times import compute_overlap_time, time_range
from pytest import raises

def test_generic_case():
    #large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    #short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = None


    r1 = time_range("2024-01-01 10:00:00","2024-01-01 12:00:00")
    r2 = time_range("2024-01-01 13:00:00","2024-01-01 14:00:00")


    assert compute_overlap_time(r1,r2) == expected


def test_case_2():
    
  
  

    range1 = [
    ("2024-01-01 10:00:00", "2024-01-01 10:30:00"),
    ("2024-01-01 11:00:00", "2024-01-01 11:30:00")
]

    range2 = [
        ("2024-01-01 10:15:00", "2024-01-01 10:45:00"),
        ("2024-01-01 11:15:00", "2024-01-01 11:45:00")
    ]

    expected = [
        ("2024-01-01 10:15:00", "2024-01-01 10:30:00"),
        ("2024-01-01 11:15:00", "2024-01-01 11:30:00")
    ]

    assert compute_overlap_time(range1,range2) == expected


def inverse_times():

    with raises(ValueError):
        time_range("2024-01-01 12:00:00", "2024-01-01 10:00:00")

inverse_times()



    