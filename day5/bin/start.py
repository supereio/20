#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

#主要启动程序
if __name__ == '__main__':
    main.run()