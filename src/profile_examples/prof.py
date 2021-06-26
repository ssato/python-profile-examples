"""Profiling functions.
"""
import collections
import cProfile
import datetime
import inspect
import timeit

import line_profiler
import memory_profiler


def run_with_time(func, *args, **kwargs):
    """Show reuslts and time elapsed using timeit."""
    start = timeit.default_timer()
    res = func(*args, **kwargs)
    end = timeit.default_timer()
    print(datetime.timedelta(seconds=(end - start)))

    return res


def run_with_profile(func, *args, **kwargs):
    """Show reuslts and time profile using cProfile."""
    prof = cProfile.Profile()
    res = prof.runcall(func, *args, **kwargs)
    prof.print_stats()

    return res


def run_with_line_profiler(func, *args, **kwargs):
    """Show reuslts and time profile using line_profiler."""
    prof = line_profiler.LineProfiler()
    prof.add_function(inspect.unwrap(func))
    res = prof.runcall(func, *args, **kwargs)
    prof.print_stats()

    return res


def run_with_memory_profiler(func, *args, **kwargs):
    """Show reuslts and memory profile using memory_profiler."""
    # .. note::
    #    I don't know how to profile wrapped functions *and* call wrapper
    #    functions like run_with_memory_profiler does.
    pfn = memory_profiler.profile(func)
    return pfn(*args, **kwargs)


RUN_WITH_PROF_FNS = collections.OrderedDict((
    (run_with_time, True),
    (run_with_profile, True),
    (run_with_line_profiler, True),
    (run_with_memory_profiler, False)
))


# pylint: disable=too-few-public-methods
class ProfiledRunner:
    """A class to run function with profiling.
    """
    def __init__(self, callables, full: bool = False,
                 show_results: bool = False):
        """initialize it."""
        self.callables = [
            (c, c.__doc__ or repr(c)) for c in callables if callable(c)
        ]
        self.full = full
        self.show_results = show_results

    def run(self, *args, **kwargs):
        """Run callables with profiling."""
        if self.full:
            profile_fns = list(RUN_WITH_PROF_FNS.keys())
        else:
            profile_fns = [p for p, flg in RUN_WITH_PROF_FNS.items() if flg]

        for pfn in profile_fns:
            print(f'########### {pfn.__doc__} ###########\n')
            for fun, desc in self.callables:
                print(f'## {desc}')
                res = pfn(fun, *args, **kwargs)

        # The reuslts of each calls should be same for all and only the last
        # result will be shown.
        if self.show_results:
            print(f'\n{res!r}')
