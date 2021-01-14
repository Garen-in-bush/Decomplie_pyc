import os
import sys
from decompile.utils import cut_file_path_suffix

# _author: 李某人
# E-mail: 594680963@qq.com


class Decompile:
    """
      将指定目录下所有的pyc文件反编译为py文件
    """
    def __init__(self, absolute_path):
        """
        :param absolute_path: pyc文件存放路径
        """
        self.file_path = absolute_path

    def run(self):
        self.decompile_all(self.file_path)

    @staticmethod
    def decompile_all(file_path):
        """
        :param file_path: 绝对路径
        :return: None
        """
        for file_name in os.listdir(file_path):
            if os.path.isdir(os.path.join(file_path, file_name)):
                Decompile.decompile_all(os.path.join(file_path, file_name))
            else:
                if file_name.split('.')[-1] == 'pyc':
                    Decompile.decompile_one(os.path.join(file_path, file_name))

    @staticmethod
    def decompile_one(file_path):
        """
        :param file_path: 绝对路径
        :return:
        """
        file_path = cut_file_path_suffix(file_path)
        command = 'uncompyle6 -o %s.py %s.pyc' % (file_path, file_path)
        os.system(command)

    @staticmethod
    def parsing_parameters(parameters):
        if len(parameters) == 1:
            print('decompile_pyc:')
            print('    -h or --help for help')
            print('--------------------------------------')
            print('    options:')
            print('        -c: to decompile pyc files')
            print('            decompile_pyc -c dir_name')
        elif parameters[1] == '-h' or parameters[1] == '--help':
            print('decompile_pyc:')
            print('    options:')
            print('        -c: to decompile pyc files')
            print('            decompile_pyc -c dir_name')
        elif parameters[1] == '-c':
            decompile_item = Decompile(parameters[2])
            decompile_item.run()
            print('All pyc files have been decompiled successfully')


def main():
    Decompile.parsing_parameters(sys.argv)


