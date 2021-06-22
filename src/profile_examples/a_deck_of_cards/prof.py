"""main.
"""
import cProfile
import datetime
import timeit


def show_with_time(times, cards_fn, suites, numbers, print_results=False):
    """A decorator to show reuslts and time elapsed.
    """
    start = timeit.default_timer()
    for _i in range(times):
        cards = cards_fn(suites, numbers)
    end = timeit.default_timer()
    print(datetime.timedelta(seconds=(end - start)))
    if print_results:
        print(f'cards: {sorted(cards)!r}')


def run_fun_times(times, cards_fn, suites, numbers):
    """wrapper to get profile data.
    """
    for _i in range(times):
        cards = cards_fn(suites, numbers)

    return cards


def show_with_profile(times, cards_fn, suites, numbers, print_results=False):
    """A decorator to show reuslts and time elapsed.
    """
    prof = cProfile.Profile()
    prof.enable()
    prof.runcall(run_fun_times, times, cards_fn, suites, numbers)
    prof.print_stats()

    cards = cards_fn(suites, numbers)
    if print_results:
        print(f'cards: {sorted(cards)!r}')
