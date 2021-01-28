""" A widget to show and list all nodes status of a network from a
configuration file.

The status of a node is defined by the chars `⬡` and `⬢` with a color.
Only `⬢` have a color other than cyan.
- Green stand for `node accessible`.
- Yellow stand for `something is wrong and can't guess if online or not`.
- Red stand for `node inaccesible`.

A `|` link two nodes between themselves. For color it have the same behavior
than the `⬢` char.

The nodes order in the configuration file define the node order rendered.

Configuration example:

    [PingNodes]
    nodes.FUR00 = "192.0.2.1"
    nodes.FUR01 = "198.51.100.145"
    nodes.FUR02 = "uwu.example.com"
"""

import schedule

from sh import ping
from sh import ErrorReturnCode_1

from moniton.jobs.common import (
    Job,
    Cursor,
)


class PingNodes(Job):

    def __init__(self, stdscr):
        super().__init__(stdscr)
        self.cursor = Cursor(3, 0)
        schedule.every(1).seconds.do(self.update_state)
        self.retry = 15 * len(self.config.nodes)
        self.duration = self.retry
        self.online = False
        schedule.every(self.duration).seconds.do(self._run_threaded)
        self.initscr()

    def reset_retry(self):
        self.retry = 15 * len(self.config.nodes)

    def initscr(self):
        self.addstr(2, 22, "INITIALIZE", self.color.white_on_black)
        self.reset_nodes_list(True)

    def reset_nodes_list(self, a=False):
        self.cursor.reset_x()
        self.addstr(
            2, 0,
            "Retry in {} seconds".format(
                str(self.retry).zfill(2)
            ),
            self.color.cyan_on_black
        )
        self.addstr(2, 20, "-", self.color.cyan_on_black)
        for i, node_data in enumerate(self.config.nodes.items()):
            name, node = node_data
            if i:
                self.addstr(self.cursor.x, 0, "|", self.color.cyan_on_black)
                self.cursor.x += 1
            self.addstr(
                self.cursor.x, 0, "⬡ " + node, self.color.cyan_on_black
            )
            self.addstr(
                self.cursor.x, 1 + len(node) + 1, " - " + name,
                self.color.cyan_on_black
            )
            self.cursor.x += 1
        self.cursor.reset_x()

    def _job(self, start=False):
        self.reset_retry()
        self.reset_nodes_list()

        for i, node_data in enumerate(self.config.nodes.items()):
            name, node = node_data
            if i:
                if self.online:
                    self.addstr(
                        self.cursor.x, 0, "|", self.color.green_on_black
                    )
                else:
                    self.addstr(
                        self.cursor.x, 0, "|", self.color.red_on_black
                    )
                self.cursor.x += 1
            check = self.check_node(node, self.cursor.x)
            if check == 0 or check == 3:
                self.addstr(
                    self.cursor.x, 0, "⬢", self.color.green_on_black
                )
                self.online = True
            elif check == 1:
                self.addstr(self.cursor.x, 0, "⬢", self.color.red_on_black)
                self.online = False
            else:
                self.addstr(
                    self.cursor.x, 0, "⬢", self.color.yellow_on_black
                )
                self.online = True
            self.addstr(
                self.cursor.x, 1, " " + node, self.color.cyan_on_black
            )
            self.addstr(
                self.cursor.x, 1 + len(node) + 1, " - " + name,
                self.color.cyan_on_black
            )
            self.cursor.x += 1

        if self.online:
            self.addstr(2, 22, "ONLINE    ", self.color.green_on_black)
        else:
            self.addstr(2, 22, "OFFLINE   ", self.color.red_on_black)

    def update_state(self):
        self.addstr(
            2, 0,
            "Retry in {} seconds".format(
                str(self.retry).zfill(2)
            ),
            self.color.cyan_on_black
        )
        if self.retry:
            self.retry -= 1

    def check_node(self, node, pos_x):
        waiting = ["⬘", "⬙", "⬖", "⬗"]
        wait = 0
        for line in ping(node, '-c', '4',  _iter=True, _ok_code=[0, 1, 2]):
            if '100% packet loss' in line:
                return 1
            elif '0% packet loss' in line:
                return 0
            elif 'packet loss' in line:
                return 3
            elif 'error' in line.lower():
                return 2
            self.addstr(
                pos_x, 0, waiting[wait] + " " + node, self.color.cyan_on_black
            )
            self.updatescr()
            wait += 1
            if wait >= len(waiting):
                wait = 0
        return 3
