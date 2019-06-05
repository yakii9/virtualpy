# Virtualpy

## 简介

Virtualpy是一个python虚拟环境管理工具。使用它可以方便的创建、删除、修改和管理python虚拟环境，目前仅支持windows端。

## 安装

克隆项目后，根目录下有打包好的.exe程序，添加程序目录到windows环境变量，重启终端即可使用。

**注意：本工具是在virtualenv的基础上进行的二次开发，在使用前需要确保已经安装virtualenv，否则软件无法正常运行**

安装[Virtualenv](https://virtualenv.pypa.io)

## 使用

在终端中直接输入virtualpy即可使用。

命令：

virtualpy help:获取帮助

delete env   删除env虚拟环境

create env   创建env的虚拟环境。activate env 在env的虚拟环境中执行命令。
   	-c: 干净的python环境

activate env 在env的虚拟环境中执行命令。

listall      列出所有的虚拟环境

版本：

V0.1