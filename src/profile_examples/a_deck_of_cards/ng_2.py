"""非効率な方法 (2).
"""


def cards(suites, numbers):
    """Cards generator."""
    res = []
    for suite in suites:
        for number in numbers:
            card = f'{suite} {number}'
            res.append(card)

    return res
