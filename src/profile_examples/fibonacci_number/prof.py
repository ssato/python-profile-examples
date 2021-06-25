"""main.
"""
import cProfile
import datetime
import timeit

import line_profiler
import memory_profiler


def run_fn(fun, nmax, times):
    """Wrapper function."""
    for _i in range(times):
        res = fun(nmax)

    return res


def run_with_time(fun, nmax, times):
    """A decorator to show reuslts and time elapsed.
    """
    start = timeit.default_timer()
    res = run_fn(fun, nmax, times)
    end = timeit.default_timer()
    print(datetime.timedelta(seconds=(end - start)))

    return res


def run_with_profile(fun, nmax, times):
    """A decorator to show reuslts and time elapsed.
    """
    prof = cProfile.Profile()
    res = prof.runcall(run_fn, fun, nmax, times)
    prof.print_stats()

    return res


def run_with_line_profiler(fun, nmax, times):
    """A decorator to show reuslts and time elapsed.
    """
    prof = line_profiler.LineProfiler()
    prof.add_function(fun)
    res = prof.runcall(run_fn, fun, nmax, times)
    prof.print_stats()

    return res


def run_with_memory_profiler(fun, nmax, times):
    """A decorator to show reuslts and time elapsed.
    """
    # backend: psuitl [default], posix, tracemalloc
    fun = memory_profiler.profile(fun)
    return run_fn(fun, nmax, times)


RUN_WITH_PROF_FNS = (
    run_with_time,
    run_with_profile,
    run_with_line_profiler,
    run_with_memory_profiler
)
