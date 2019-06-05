# -*- coding: utf-8 -*-
import os
import fire
import shutil
import re

def create(*args):
    if len(args) == 1:
        if args[0] in env_list:
            print("此虚拟环境已存在，创建失败！")
        else:
            command = "cd C:\\Users\\tyler\\.virtualenvs && virtualenv " + args[0]
            os.system(command)
    if len(args) > 1:
        option = ""
        for i in args[1:]:
            if i == "-c":
                option += "--no-site-packages "
            else:
                option += i
                option += " "
        command = "cd C:\\Users\\tyler\\.virtualenvs && virtualenv " + option + args[0]
        os.system(command)

def activate(name):
    if name in env_list:
        global command_list
        flag = get_input(name)
        if len(command_list) > 0:
            command = "cd C:\\Users\\tyler\\.virtualenvs\\" + name + "\\Scripts && activate"
            for i in command_list:
                command += " && " + i
            os.system(command)
            command_list = []
            print("当前虚拟环境为：" + name + "。命令执行完成！")
        else:
            if flag == 0:
                print("成功退出！")
            else:
                print("没有可以执行的命令！")
        if flag == 1:
            return activate(name)
    else:
        print("虚拟环境不存在！切换失败！")
def delete(name):
    if name in env_list:
        shutil.rmtree("C:\\Users\\tyler\\.virtualenvs\\"+name)
        path = "C:\\Users\\tyler\\.virtualenvs"
        env_list_tem = os.listdir(path)
        if name in env_list_tem:
            print("虚拟环境删除失败！")
        else:
            print("虚拟环境删除成功！")
    else:
        print("该虚拟环境不存在，删除失败！")
def listall(*args):
    for i in env_list:
        print(i)
def help():
    command_help = ''' 本工具帮忙管理python虚拟环境，需要先安装virtualenv工具。\n 
 Command:
 create env   创建env的虚拟环境。\n activate env 在env的虚拟环境中执行命令。
    -c: 干净的python环境
 delete env   删除env虚拟环境
 listall      列出所有的虚拟环境'''
    print(command_help)

def get_input(name):
    command = input(name + "> ")
    global command_list
    if command == "q":
        return 0
    if command == "run":
        return 1
    if command == "list":
        for i in command_list:
            print(str(command_list.index(i)+1) + ":" + i)
        return get_input(name)
    prog= re.compile(r'^del [0-9]+([,，][0-9]+)*\s*',flags=0)
    if prog.match(command):
        del_list = re.split(r'[,\s]', command)
        del_list = del_list[1:]
        command_list_tem = []
        for i in range(len(command_list)):
            if str(i+1) not in del_list:
                command_list_tem.append(command_list[i])
        command_list = command_list_tem
        print("Delete successfully!")
        return get_input(name)
    else:
        command_list.append(command)
        return get_input(name)
if __name__ == '__main__':
    command_list = []
    path = "C:\\Users\\tyler\\.virtualenvs"
    env_list = os.listdir(path)
    fire.Fire()