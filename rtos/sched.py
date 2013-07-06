"""
A model of the RTOS schedulers in Python.

This can be used for testing purposes to ensure implementation matches the model.

"""
from itertools import product


def head(iter_):
    """Return the first item in an iterator, or None if the iterator is empty."""
    try:
        return next(iter_)
    except StopIteration:
        return None


def rotate(sequence, n):
    """Rotate a sequence by n positions.

    Note: This function returns a new list; it does not mutate the seqeunce.

    """
    return sequence[n:] + sequence[:n]


def incmod(i, n):
    return (i + 1) % n


class BaseSched:
    def __init__(self, runnable):
        self.runnable = runnable
        self.size = len(runnable)

    @property
    def indexed(self):
        """Return the runnable list as tuples (index, runnable)."""
        return list(enumerate(self.runnable))

    @property
    def runnable_str(self):
        return ''.join(['X' if r else ' ' for r in self.runnable])

    def get_next(self):
        """Based on the scheduling algorithm return the next task to run.

        This method may mutate the scheduler object.

        This method should be implemented by a sub-class.

        """
        raise Exception("get_next should be implemented by sub-class.")


class RrSched(BaseSched):
    """A model of the round-robin scheduler."""

    def __init__(self, runnable, cur):
        super().__init__(runnable)
        self.cur = cur

    def __str__(self):
        return '<RrSched cur={} runnable=[{}]>'.format(self.cur, self.runnable_str)

    def get_next(self):
        next_ = head(idx for idx, runnable in rotate(self.indexed, incmod(self.cur, self.size)) if runnable)
        self.cur = self.size - 1 if next_ is None else next_
        return next_

    @classmethod
    def states(cls, n, assume_runnable=False):
        """Return all possible round-robin scheduler states for n tasks.

        If assume_runnable is True then only include states where at least one task is runnable.

        """
        g = (cls(*s) for s in product(product((True, False), repeat=n), range(n)))
        return filter(lambda s: any(s.runnable), g) if assume_runnable else g


class PrioSched(BaseSched):
    """A model of the strict priority scheduler."""

    def __str__(self):
        return '<PrioSched runnable=[{}]>'.format(self.runnable_str)

    def get_next(self):
        return head(idx for idx, runnable in self.indexed if runnable)

    @classmethod
    def states(cls, n, assume_runnable=False):
        """Return all possible priority scheduler states for n tasks.

        If assume_runnable is True then only include states where at least one task is runnable.

        """
        g = (cls(s) for s in product((True, False), repeat=n))
        return filter(lambda s: any(s.runnable), g) if assume_runnable else g


if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--assume-runnable', action='store_true',
                        help="Ensure schedulers have at least 1 runnable task.")
    parser.add_argument('--sched', choices=['prio', 'rr'], required=True)
    parser.add_argument('N', type=int,
                        help="Number of tasks in scheduler.")
    args = parser.parse_args()

    sched_class = { 'prio': PrioSched, 'rr': RrSched }[args.sched]

    for s in sched_class.states(args.N, args.assume_runnable):
        before = str(s)
        next_ = s.get_next()
        after = str(s)
        print("{:>5}  {}  {} ".format(next_, before, after))
