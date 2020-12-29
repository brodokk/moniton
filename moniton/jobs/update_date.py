""" A widget to show clocks of differents timezones.
"""

import curses
import schedule

from datetime import datetime
import pytz

from moniton.jobs.common import Job


class UpdateDate(Job):

    def __init__(self, stdscr, color):
        super().__init__(stdscr, color)
        schedule.every(1).seconds.do(self._run_threaded)

    def _job(self):
        utc_datetime = "UTC " + self._return_time('UTC')
        self.addstr(0, 0, str(utc_datetime), self.color.cyan_on_black)

        cet_datetime = "CET " + self._return_time('Europe/Paris')
        self.addstr(
            0, len(str(cet_datetime)) + 4,
            str(cet_datetime), self.color.cyan_on_black
        )

        est_datetime = "EST " + self._return_time('US/Eastern')
        self.addstr(
            0, curses.COLS - len(str(est_datetime)) * 2 - 4,
            str(est_datetime), self.color.cyan_on_black
        )

        pst_datetime = "PST " + self._return_time('US/Pacific')
        self.addstr(
            0, curses.COLS - len(str(pst_datetime)),
            str(pst_datetime), self.color.cyan_on_black
        )

    def _return_time(self, tz):
        return datetime.now(pytz.timezone(tz)).strftime('%H:%M:%S (%I%p)')
