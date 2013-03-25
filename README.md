# Intro
I wanted an easy way to ssh into my server, then manage my sessions right away.
So I wrote it in Python using the curses library. Also, it uses vim-like key-
bindings.

# Prerequisites
-   Python 2.x
-   tmux
-   urwid

# Usage
Run the script and there will be a menu showing your acive sessions and the
active clients. Navigate using j,k or ↑,↓ and press <Enter> to attach to that
session.

## Keybinds
-   j,k         move up, move down
-   ↑,↓         move up, move down
-   Enter       attach to session
-   dd          kill session
-   x           detach client
-   r           rename session
-   ggdG        kill server
-   o           new session


