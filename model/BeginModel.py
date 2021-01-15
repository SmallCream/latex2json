from model.BaseModel import BaseModel


class BeginModel(BaseModel):
    def __init__(self, style, value, children, parent, tag="begin"):
        super().__init__(value, children, parent, tag)
        self.style = style


if __name__ == '__main__':
    begin_model = BeginModel("begin", 'value', 'children', 'parent', 'text')
    print(begin_model.tag)
