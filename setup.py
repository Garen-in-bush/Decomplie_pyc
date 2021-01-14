#! /usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='decompile_pyc',
    author='jiahao.li',
    version='0.0.2',
    license='MIT',
    long_description=long_description,  # 将说明文件设置为README.md
    long_description_content_type="text/markdown",
    description='反编译指定目录下所有pyc文件',
    author_email='594680963@qq.com',
    url='https://github.com/Garen-in-bush/Decomplie_pyc',
    packages=find_packages(),
    # 依赖包
    install_requires=[
        'uncompyle6 >= 3.7.4'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
    entry_points={
        'console_scripts':
            [
                'decompile_pyc = decompile.decompile_pyc:main',
            ]
    }
)
