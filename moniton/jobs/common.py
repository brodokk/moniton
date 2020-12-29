import threading

from moniton.config import (
    config,
    Config,
)


class Cursor:

    def __init__(self, x, y):
        self._base_x = x
        self._base_y = y
        self.x = x
        self.y = y

    def reset_x(self):
        self.x = self._base_x

    def reset_y(self):
        self.y = self._base_y

    def reset(self):
        self.reset_x()
        self.reset_y()


class Job:

    def __init__(self, stdscr, color):
        self.color = color
        self.cursor = Cursor(0, 0)
        if self.__class__.__name__ in config:
            job_config = config[self.__class__.__name__]
            self.config = Config(job_config)
        self.stdscr = stdscr

    def _run_threaded(self):
        job_thread = threading.Thread(target=self._job)
        job_thread.start()

    def addstr(self, *args, **kwargs):
        self.stdscr.addstr(*args, **kwargs)

    def updatescr(self):
        self.stdscr.noutrefresh()
