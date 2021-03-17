#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import git

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
	stat= [ symbol[key] for key, val in count if symbol[key] != "" ]
	return '/'.join(stat)


if __name__ == "__main__" :
	branch()
