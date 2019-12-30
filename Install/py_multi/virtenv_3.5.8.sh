#!/bin/bash

# User specific aliases and functions
alias mkv='mkvirtualenv' # 创建一个虚拟环境 mkv myenvs
alias rmv='rmvirtualenv' # 删除虚拟环境 rmv  myenvs
alias lsv='lsvirtualenv' # 查看所有的虚拟环境

export WORKON_HOME=~/.virtualenvs3.5.8 #指定virtualenvwrapper环境的目录

export VIRTUALENVWRAPPER_PYTHON=/opt/pyenv/python/py3.5.8/bin/python3 #指定python版本

#确保这个文件在不同版本是相同的
#或者确保不同py版本安装virtualenvwrapper版本是相同的
source ~/.local/bin/virtualenvwrapper.sh  
export LD_LIBRARY_PATH="/usr/local/lib"
