#!/usr/bin/env python
#coding:utf-8
'''
author: tfss
e-mail: 1255791430@qq.com
desc: python自动化安装用户指定版本的python环境:2.7或者3.6
'''
#导入Python的系统编程操作模块
import os

#导入用来处理Python运行时配置以及资源，与前当程序之外的系统环境交互的模块
import sys

#判断当前用户是否是root用户
if os.getuid() == 0:
  pass
else:
  print('Not under root mode, please switch user!')
  sys.exit(1)

#获取用户输入的python安装版本
version = input('Please input wanted python version(2.7/3.6)')

#如果嫌官网下载速度太慢可以指定python3.6.5的链接地址为本人上传资源地址
#根据用户输入的python版本选择源码包下载地址
if version == '2.7':
  package_version = 'Python-2.7.13'
  url = 'https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz'
elif version == '3.6':
  package_version = 'Python-3.6.5'
  url = 'https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz'
else:
  print('Please input given version number(2.7/3.6)')
  sys.exit(1)

#拼接源码包下载地址并执行下载命令
cmd = 'wget ' + url
package_tgz = package_version + '.tgz'

if os.path.exists(package_tgz) != True:
    res = os.system(cmd)
    if res != 0 :
      print('Failed to download python source package, please inspect your network!')
      sys.exit(1)

if os.path.exists(package_version) != True:
    #解压下载的源码包
    cmd = 'tar zxvf ' + package_tgz
    res = os.system(cmd)
    #如果解压失败则删除下载的源码包并且提示用户重新执行脚本
    if res != 0:
      os.system('rm -rf ' + package_tgz)
      print('Please reexcute the script to install python')
      sys.exit(1)

#解压成功则进入解压后的源码目录中依次执行配置、编译、安装过程
cmd = 'cd ' + package_version + ' && ./configure --prefix=/usr/local/python && make && make install'

res = os.system(cmd)

#安装失败则提示用户安装失败了，让用户检查环境依赖
if res != 0:
  print('Failed to install python, please inspect dependencies for python install!')
  sys.exit(1)

# 创建软连接
if version == '2.7':
  print("版本为2.7，不需要配置软连接！")
else:
  cmd = 'ln -s /usr/local/python/bin/python3.6 /usr/local/bin/python3'
  res = os.system(cmd)
  if res != 0:
    print('软连接失败，请手动软连(ln -s /usr/local/python/bin/python3.6 /usr/bin/local/python3)')
    sys.exit(1)

