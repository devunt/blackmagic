import ast
import traceback


def dbgprint(*args):
    args = list(args[::-1])
    caller = traceback.extract_stack()[-2]
    syntax_tree = ast.parse(caller.line)
    names = syntax_tree.body[0].value.args
    for name in names:
        print(f'{name.id} = {args.pop()}')
