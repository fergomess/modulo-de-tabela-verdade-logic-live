from enum import Enum


class ChoicesEnum(Enum):

    def __init__(self, code, display_name=''):
        self.code = code
        self.display_name = display_name

    def __eq__(self, other):
        if not other:
            raise ValueError()
        return self.code == other if type(other) == int else self.code == other.code

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def choices(klass):
        return tuple([(b.code, b.display_name) for a, b in klass.__members__.items()])

    @classmethod
    def get(klass, index):
        choices = klass.choices()
        for t_index, t_value in choices:
            if t_index == index:
                return t_value
        return None