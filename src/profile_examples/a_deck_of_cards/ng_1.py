"""非効率な方法 (1).
"""


def cards(suites, numbers):
    """Cards generator."""
    res = []
    (suites, numbers) = (list(suites), list(numbers))
    for i in range(len(suites)):
        for j in range(len(numbers)):
            card = suites[i] + ' ' + numbers[j]
            res.append(card)

    return res
