#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time     : 2018/7/27 14:14
# @Author   : crabtesting@163.com
# @File     : GlobalPara.py
import os
import time
import shutil
from crabTesting.ConstantPara import *
from crabTesting.SwitchPara import *

curdir = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

def global_CTbefore():
    print("="*18," crabTesting start ","="*18)
    # nowpath = os.getcwd() # 执行路径
    global global__CTrunflag
    global__CTrunflag = True
    global__logDir = global_logDir()
    if os.path.exists("%s/Log"%(curdir)):
        allLogdir = os.listdir("%s/Log"%(curdir))
        if len(allLogdir) >= constant_logNum:
            allLogdir.sort()
            for i in range(len(allLogdir) + 1 - constant_logNum):
                shutil.rmtree("%s/Log/%s"%(curdir,allLogdir[i]))
    print("LogDir = %s ;"%(global__logDir))
    options = {"outputdir":global__logDir}
    return options

def global_CTafter():
    if global_driver():
        global_driver().quit()
    print("="*18," crabTesting end ","="*18)

def global_CTrunflag():
    global global__CTrunflag
    try:
        global__CTrunflag
    except:
        global__CTrunflag = False
    return global__CTrunflag

def global_crabTestingDir():
    return curdir

def global_logDir():
    global global__logDir
    try:
        global__logDir
    except:
        nowtime = time.strftime("%Y-%m-%d.%H%M%S",time.localtime())
        global__logDir = "%s/Log/%s"%(curdir,nowtime)
        os.mkdir(global__logDir)
    return global__logDir

def global_downloadDir(flag = False):
    global__downloadDir = "%s/Download"%(curdir)
    return global__downloadDir

def global_driver(flag = False):
    global global__driver
    if flag:
        global__driver = flag
    try:
        global__driver
    except:
        global__driver = False
    return global__driver

def global_curSelectCom(flag = False,value = False):
    if switch_curSelectFlag:
        global global__curSelectCom
        if flag:
            if flag == {}:
                global__curSelectCom = flag
            elif value:
                global__curSelectCom[flag] = value
        try:
            global__curSelectCom
        except:
            global__curSelectCom = {}
        return global__curSelectCom
    else:
        return False