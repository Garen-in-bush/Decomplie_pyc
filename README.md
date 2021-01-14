uncompile_pyc
=================================== 
安装：
-----------------------------------
### 方法1 从安装包安装
```shell
pip install decompile_pyc
```
### 方法2 源码安装
```shell
git clone https://github.com/Garen-in-bush/Decomplie_pyc.git
```
进入到setup.py所在的目录，执行
```shell
python setup.py sdist bdist_wheel
cd dist
pip install xxx.tar.gz
```
或者
```shell
pip install xxx.wheel
```
使用
--------------------------------
### 进入对应的python环境(如果有多个虚拟环境的话)
```shell
decompile_pyc -c path  # path为需要反编译的文件所在目录
```
### https://zhuanlan.zhihu.com/p/344278133
