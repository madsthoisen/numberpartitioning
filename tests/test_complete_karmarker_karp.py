import sys
sys.path.append('../src')

import pytest

from numberpartitioning import complete_karmarkar_karp


def test_complete_karmarkar_karp():
    numbers = [4, 5, 6, 7, 8]
    expected_partitions = [((8,), (4, 7), (5, 6))]
    expected_sizes = [(8, 11, 11)]
    partition_results = []
    sizes_results = []
    res = complete_karmarkar_karp(numbers, num_parts=3)
    try:
        while True:
            result = next(res)
            partition_results.append(result.partition)
            sizes_results.append(result.sizes)
    except:
        StopIteration
    assert partition_results == expected_partitions
    assert sizes_results == expected_sizes


def test_complete_karmarkar_karp_can_give_indices():
    numbers = [4, 5, 6, 7, 8]
    expected_partitions = [((4,), (0, 3), (1, 2))]
    expected_sizes = [(8, 11, 11)]
    partition_results = []
    sizes_results = []
    res = complete_karmarkar_karp(numbers, num_parts=3, return_indices=True)
    try:
        while True:
            result = next(res)
            partition_results.append(result.partition)
            sizes_results.append(result.sizes)
    except:
        StopIteration
    assert partition_results == expected_partitions
    assert sizes_results == expected_sizes


def test_complete_karmarkar_karp_unordered():
    numbers = [5, 8, 6, 4, 7]
    expected_partitions = [((8,), (4, 7), (5, 6))]
    expected_sizes = [(8, 11, 11)]
    partition_results = []
    sizes_results = []
    res = complete_karmarkar_karp(numbers, num_parts=3)
    try:
        while True:
            result = next(res)
            partition_results.append(result.partition)
            sizes_results.append(result.sizes)
    except:
        StopIteration
    assert partition_results == expected_partitions
    assert sizes_results == expected_sizes


def test_complete_karmarkar_karp_unordered_indices():
    numbers = [5, 8, 6, 4, 7]
    expected_partitions = [((1,), (3, 4), (0, 2))]
    expected_sizes = [(8, 11, 11)]
    partition_results = []
    sizes_results = []
    res = complete_karmarkar_karp(numbers, num_parts=3, return_indices=True)
    try:
        while True:
            result = next(res)
            partition_results.append(result.partition)
            sizes_results.append(result.sizes)
    except:
        StopIteration
    assert partition_results == expected_partitions
    assert sizes_results == expected_sizes


def test_complete_karmarkar_karp_optimal_solution():
    numbers = [4, 5, 6, 7, 8]
    expected_partitions = [((6, 8), (4, 5, 7)), ((4, 5, 6), (7, 8))]
    expected_sizes = [(14, 16), (15, 15)]
    partition_results = []
    sizes_results = []
    res = complete_karmarkar_karp(numbers, num_parts=2)
    try:
        while True:
            result = next(res)
            partition_results.append(result.partition)
            sizes_results.append(result.sizes)
    except:
        StopIteration
    assert partition_results == expected_partitions
    assert sizes_results == expected_sizes


def test_complete_karmarkar_karp_larger_example():
    numbers = list(range(10, 30))
    expected_partitions = [((14, 17, 20, 23, 26, 29), (11, 12, 16, 18, 22, 24,
        27), (10, 13, 15, 19, 21, 25, 28)), ((10, 12, 16, 18, 22, 24, 28), (11,
            13, 14, 19, 21, 25, 27), (15, 17, 20, 23, 26, 29))]
    expected_sizes = [(129, 130, 131), (130, 130, 130)]
    partition_results = []
    sizes_results = []
    res = complete_karmarkar_karp(numbers, num_parts=3)
    try:
        while True:
            result = next(res)
            partition_results.append(result.partition)
            sizes_results.append(result.sizes)
    except:
        StopIteration
    assert partition_results == expected_partitions
    assert sizes_results == expected_sizes


def test_complete_karmarkar_karp_raises_unsupported_method():
    with pytest.raises(ValueError):
        complete_karmarkar_karp([1, 2, 3], method="foo")
