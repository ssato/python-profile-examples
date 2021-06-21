"""効率的な方法 (1).
"""


def each_card(suites, numbers):
    """Generator version of cards generator."""
    for suite in suites:
        for number in numbers:
            yield f'{suite} {number}'


def cards(suites, numbers):
    """Cards generator."""
    return list(each_card(suites, numbers))
