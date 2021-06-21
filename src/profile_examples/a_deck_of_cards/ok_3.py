"""効率的な方法 (3).
"""


def each_card(suites, numbers):
    """Generator version of cards generator."""
    for suite in suites:
        for number in numbers:
            yield f'{suite} {number}'


def cards(suites, numbers):
    """Cards generator."""
    return [*each_card(suites, numbers)]
