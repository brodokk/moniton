import curses
import schedule
import time

from termcolor import colored

import moniton.jobs
from moniton.config import (
    Color,
)
from moniton.utils import launch_splash_screen

def draw(stdscr):
    k = 0

    color = Color()

    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)

    splash_screen = launch_splash_screen(color)

    for job in moniton.jobs.get_jobs():
        job(stdscr, color)

    splash_screen.refresh()
    time.sleep(4)

    while (k != ord('q')):
        k = stdscr.getch()
        schedule.run_pending()
        curses.doupdate()
        time.sleep(0.1)

def main():
    curses.wrapper(draw)


if __name__ == "__main__":
    main()
