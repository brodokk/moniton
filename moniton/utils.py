import curses
import time

from moniton.config import (
    Color,
)

def launch_splash_screen():
    logo = [
        "                          :*                      ",
        "                   %#:     ##*                    ",
        "                 :&BB:     %BB@:                  ",
        "                 @BBB:     %BBB%                  ",
        "                 *$@&!     :%*::                  ",
        "                 ::                               ",
        "              !$#SBS@!       :%$*:                ",
        "             $BBBBBBBB*     !SBBBS@:              ",
        "            @BBBBBBBBBS:    #BBBBBBS%             ",
        "           $BBBBBBBBBBB%   *BBBBBBBBB@            ",
        "          !BBBBBBBBBBBB@   $BBBBBBBBBB&:          ",
        "          @BBBBBBBBBBBB#   &BBBBBBBBBBB&:   :     ",
        "  :*     :SBBBBBBBBBBBB#   #BBBBBBBBBBBB$   $$    ",
        " !S&     :SBBBBBBBBBBBB&  :SBBBBBBBBBBBBS:  #B%   ",
        ":#BS:     #BBBBBBBBBBBB%  :SBBBBBBBBBBBBS: *BBB!  ",
        "%BBB*     %BBBBBBBBBBBS:   &BBBBBBBBBBBB@  !&&#$  ",
        "*%*$*      &BBBBBBBBBB%    !BBBBBBBBBBB#:         ",
        "  !**:     :$SBBBBBBS%      *#BBBBBBB#%  !%@@%:   ",
        ":&BBBS@:     :*$@@$*:         !%$$%*:  !&BBBBBS%  ",
        "%BBBBBBS%                             %BBBBBBBBB% ",
        "@BBBBBBBB&!                          @BBBBBBBBBBS:",
        "$BBBBBBBBBS%                        @BBBBBBBBBBBB%",
        "*BBBBBBBBBBB@:                     %BBBBBBBBBBBBB@",
        ":BBBBBBBBBBBB#!                   :SBBBBBBBBBBBBB$",
        " &BBBBBBBBBBBBB*                  *BBBBBBBBBBBBBB*",
        " *BBBBBBBBBBBBBS:                 *BBBBBBBBBBBBB& ",
        "  &BBBBBBBBBBBBB!                 :SBBBBBBBBBBB&: ",
        "  :&BBBBBBBBBBB@        !!!!:      !#BBBBBBBB#%   ",
        "    %#BBBBBBS&*      !@SBBBBS@*      !*%$$%!:     ",
        "      !*$$*!:      !&BBBBBBBBBB#*                 ",
        "                  %BBBBBBBBBBBBBB&!               ",
        "                 $BBBBBBBBBBBBBBBBB%              ",
        "                $BBBBBBBBBBBBBBBBBBB%             ",
        "               $BBBBBBBBBBBBBBBBBBBBS:            ",
        "              !BBBBBBBBBBBBBBBBBBBBB#             ",
        "              $BBBBBBBBBBBBBBBBBBBBS!             ",
        "              !BBBBBBBBBBBBBBBBBBB$:              ",
        "               !&BBBBBBBBBBBBBS&%:                ",
        "                 :*$@&&&&@$%*!:                   ",
    ]
    start_line = curses.LINES // 2  - (len(logo) + 2) // 2
    splash_screen_col = len(logo[0])
    splash_screen = curses.newwin(
        len(logo) + 4, splash_screen_col,
        start_line,
        curses.COLS // 2 - len(logo[0]) // 2
    )

    for line in range(0, len(logo)):
        splash_screen.addstr(
            line + 1,
            1,
            logo[line],
            Color().cyan_on_black
        )
        splash_screen.refresh()
        time.sleep(0.05)

    time.sleep(0.75)

    text = "        Loading paws...        "

    splash_screen.addstr(
        (len(logo) + 10) // 2,
        splash_screen_col // 2 - len(text) // 2,
        text,
        Color().cyan_on_black
    )

    return splash_screen
