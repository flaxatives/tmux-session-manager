#!/usr/bin/python2
"""
tmux session manager - a curses based console interface to manage tmux sessions

Provides a TUI for some basic tmux session handling for when you ssh into a 
server.
"""

# most of the code below is derived from the urwid tutorial on excess.org
# so far it's really hacked together just to get something usable up
# right now, it just lets you choose a session
# TODO most everything else

import os, subprocess
import urwid


# clients
f = os.popen('tmux ls')
sessions = f.read().splitlines()
args = []


def menu(title, sessions):
    body = [urwid.Text(title), urwid.Divider()]
    for c in sessions:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, session):
    # do tmux commands
    sNum = session.split(':')[0]
    args = ['tmux', 'attach', '-t', '0']
    subprocess.call(args)

    raise urwid.ExitMainLoop()      # exit program
        
    

main = urwid.Padding(menu(u'Select tmux Session', sessions), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)

urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
