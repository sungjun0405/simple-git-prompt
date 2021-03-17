#!/bin/bash

count() 
{
	echo -e $(git status -s . | awk -f ~/.git_prompt/get.fmt )
}

count
