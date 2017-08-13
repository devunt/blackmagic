import ast
import ctypes
import inspect
import traceback


class Cout:
    def __lshift__(self, v):
        print(v, end='')
        return self


class Cin:
    def __rshift__(self, v):
        caller_framestack = traceback.extract_stack()[-2]
        syntax_tree = ast.parse(caller_framestack.line)
        name = syntax_tree.body[0].value.right.id

        caller_frame = inspect.currentframe().f_back
        caller_frame.f_locals[name] = input()
        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(caller_frame), ctypes.c_int(0))

        return self


cout = Cout()
cin = Cin()
endl = '\n'
