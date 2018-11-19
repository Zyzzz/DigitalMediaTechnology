class global_var:
    '''需要定义全局变量的放在这里，最好定义一个初始值'''
    index = 0

# 对于每个全局变量，都需要定义get_value和set_value接口
def set_page(index):
    global_var.index = index
def get_page():
    return global_var.index