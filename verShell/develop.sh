#!/bin/bash

c_green="%{\033[0;32m%}"
c_end="%{\033[0m%}"

branch() 
{
	if git rev-parse --git-dir >/dev/null 2>&1
	then
		branchName="(git:"$(color)$(git branch 2>/dev/null| sed -n '/^\*/s/^\* //p')${c_end}$(check)") "
	else
		return 0
	fi
	echo -e $branchName

}

branch_no_color() 
{
	if git rev-parse --git-dir >/dev/null 2>&1
	then
		branchName="(git:"$(git branch 2>/dev/null| sed -n '/^\*/s/^\* //p') $(check)") "
	else
		return 0
	fi
	echo -e $branchName

}

color()
{
	color=${c_green}
	echo -ne $color
}

check()
{
	IFS=' ' 
	read -a vCounts <<< `~/.git_prompt/count2.sh`
	for ent in "${vCounts[@]}"
	do
		IFS=':' read -r key val <<< $ent
	done
}

branch
