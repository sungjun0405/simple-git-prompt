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
	read modified added deleted renamed copied unmerged untracked<<< $( echo | xargs -n 1 -P 7 ~/.git_prompt/count.sh )

	coment=""
	if [ $deleted != 0 ] && [ $modified != 0 ] || [ $added != 0 ]; then
		coment=$coment"¡¾"
	elif [ $modified != 0 ] || [ $added != 0 ]; then
		coment=$coment"+"
	elif [ $deleted != 0 ]; then
		coment=$coment"-"
	fi
	if [ $unmerged != 0 ]; then
		coment=$coment">[¡¾]<"
	fi
	if [ $renamed != 0 ]; then
		coment=$coment""
	fi
	if [ $copied != 0 ]; then
		coment=$coment""
	fi
	if [ $untracked != 0 ]; then
		coment=$coment""
	fi
	echo -ne $coment
}

branch
