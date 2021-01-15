
class BaseModel:

    def __init__(self, value, children, parent, tag='text'):
        """
        基类
        :param value: 值
        :param children: 子类列表
        :param parent: 父类
        :param tag: 标签类别，包括
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.parent = parent

    def to_text(self):
        """


        自定义转换
        :return:
        """
        pass

    def to_json(self):
        """
        model转换成json
        :return:
        """

    def modify_value(self):
        """
        自定义修改value
        :return:
        """