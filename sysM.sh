#!/bin/sh
xid="$(tabbed -c -d -s -r 2 st -w x)"
st -w "$xid" btop &
st -w "$xid" doas nethogs &
