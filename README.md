fork一份到自己的仓库

克隆git 到/opt目录内，为了实现python环境的版本控制（指的是安装包、回滚包），所有操作都在git目录中执行，执行完了，可以提交到github保存，方便复制环境到其它机器

从Install开始！

基于virtualenv+virtualenvwrapper


实现的效果：
-   不和全局环境冲突，全局环境就是用root用户安装在默认位置的python环境，相对应本方法安装的python不在默认位置，而是指定在/opt/pyenv/python目录内
- /opt/pyenv/python，用源码包安装多个版本的环境
- /opt/pyenv/pyruntime，虚拟环境和版本
- 借助virtualenv创建虚拟环境，用virtualenvwrapper实现环境的管理（创建、删除、切换）
- 在对应的环境内使用命令 pip freeze > requirements.txt  备份环境的库，同时push到github保存
  
  
  
  
使用方法：
-  1.切换到非root用户，指的是开发者用户，可能单机多用户
-  2.在pyruntime中创建项目目录，复制环境控制脚本
-  3.执行： source ~/py_multi/virtualenv_3.8.1.sh
-  4.查看当前版本下已经存在的虚拟环境：workon  或  lsv
-  5.创建新的虚拟环境：mkv xxxx_py3.8.1   ,一般与文件夹相同
-  6.使用环境 workon xxxx_py3.8.1
-  7.安装包 pip install xxxx  
-  8.备份包： pip freeze > requirements.txt
-  9.上传到git ， git push
-  10.退出环境：deactivate
-  11.删除环境：rmv xxxx_py3.8.1，别删错了，没有撤销
