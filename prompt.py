#!/usr/bin/python
#-*- coding:utf-8 -*-

import os

c_green="%{\033[0;32m%}"
c_end="%{\033[0m%}"

def branch():
	if os.system('git rev-parse --git-dir >/dev/null 2>&1') == 0 :
		branchName = os.popen("git branch 2>/dev/null| sed -n '/^\*/s/^\* //p'").read().split()
		print("(git:%s %s)"%(color(branchName[0]),check()))
	else :
		return 0

def color(branchName):
	return "%s%s%s"%(c_green,branchName,c_end)
'''
X          Y     Meaning
-------------------------------------------------
[AMD]   not updated
M        [ MD]   updated in index
A        [ MD]   added to index
D                deleted from index
R        [ MD]   renamed in index
C        [ MD]   copied in index
[MARC]           index and work tree matches
[ MARC]     M    work tree changed since index
[ MARC]     D    deleted in work tree
[ D]        R    renamed in work tree
[ D]        C    copied in work tree
-------------------------------------------------
D           D    unmerged, both deleted
A           U    unmerged, added by us
U           D    unmerged, deleted by them
U           A    unmerged, added by them
D           U    unmerged, deleted by us
A           A    unmerged, both added
U           U    unmerged, both modified
-------------------------------------------------
?           ?    untracked
!           !    ignored
-------------------------------------------------
'''
symbol = {
	"M":"+",
	"A":"+",
	"D":"-",
	"U":"[]",
	"C":"",
	"E":"",
	"??":"",
}

def check():
	count = [x.split(':') for x in os.popen("git status -s . | awk -f ~/.git_prompt/get.fmt").read().split()]
	stat= [ symbol[key] for key, val in count if len(key) == 1 and symbol[key] != "" ]
	return '/'.join(stat)


if __name__ == "__main__" :
	branch()
