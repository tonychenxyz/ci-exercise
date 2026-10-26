import itertools

import pytest

CASES = ((10, 1), (10, 2), (20, 0.1), (10, 0.1), (0.1234, 0.02))


@pytest.fixture(params=list(itertools.permutations(CASES, 2)))
def ab(request):
    return request.param
