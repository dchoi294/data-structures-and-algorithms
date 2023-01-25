from python.code_challenges.merge_sort import merge_sort


def test_merge_sort():
    arr = [8, 4, 23, 42, 16, 15]
    actual = merge_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_merge_sort_reverse_sorted():
    arr = [20, 18, 12, 8, 5, -2]
    actual = merge_sort(arr)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_merge_sort_few_unique():
    arr = [5, 12, 7, 5, 5, 7]
    actual = merge_sort(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_merge_sort_nearly_sorted():
    arr = [2, 3, 5, 7, 13, 11]
    actual = merge_sort(arr)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
