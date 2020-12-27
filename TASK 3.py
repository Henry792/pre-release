class Tools:
    def __init__(self, name, cost, image_file_name):
        self.__name = name
        self.__cost = cost
        self.__image_file_name = image_file_name

    def set_name(self, new_name):
        self.__name = new_name

    def set_cost(self, new_cost):
        self.__cost = new_cost

    def set_image_file_name(self, new_image_file_name):
        self.__image_file_name = new_image_file_name

    def get_cost(self):
        return self.__cost

    def get_name(self):
        return self.__name

    def get_image_file_name(self):
        return self.__image_file_name


class Shelf:
    def __init__(self, position):
        self.__position = position
        self.__content = [''] * 10
        self.__pointer = 1

    def add_tool(self, tool_object):
        self.__content[self.__pointer] = tool_object
        self.__pointer += 1

    def get_content(self):
        return self.__content


def output_shelf_tools(shelf_object):
    i = 1
    array = shelf_object.get_content
    while array[i] != '':
        print('name of tool', array[i].get_name, end=" ")
        print('cost of tool', array[i].get_cost)
        i += 1
