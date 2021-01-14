def cut_file_path_suffix(file_path):
    """
    :param file_path: 文件路径
    :return: 去除后缀后的文件路径
    """
    s = []
    index_of_suffix = file_path.rfind('.')
    return file_path[:index_of_suffix]
