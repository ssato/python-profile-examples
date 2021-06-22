"""main.
"""
import cProfile
import datetime
import timeit

import line_profiler


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
    prof.runcall(run_fun_times, times, cards_fn, suites, numbers)
    prof.print_stats()

    cards = cards_fn(suites, numbers)
    if print_results:
        print(f'cards: {sorted(cards)!r}')


def show_with_line_profiler(times, cards_fn, suites, numbers,
                            print_results=False):
    """A decorator to show reuslts and time elapsed.
    """
    prof = line_profiler.LineProfiler()
    prof.add_function(cards_fn)
    prof.runcall(run_fun_times, times, cards_fn, suites, numbers)
    prof.print_stats()

    cards = cards_fn(suites, numbers)
    if print_results:
        print(f'cards: {sorted(cards)!r}')


PROF_DEFAULT = show_with_time
PROF_MAP = dict(
    cProfile=show_with_profile,
    line_profiler=show_with_line_profiler,
)


def show(times, cards_fn, suites, numbers,
         profiler=PROF_DEFAULT, print_results=False):
    """A decorator to show reuslts and time elapsed.
    """
    show_fn = PROF_MAP.get(profiler, PROF_DEFAULT)
    show_fn(times, cards_fn, suites, numbers, print_results=print_results)
