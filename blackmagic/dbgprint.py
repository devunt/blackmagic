import ast
import traceback


def dbgprint(*args):
    args = list(args[::-1])
    caller = traceback.extract_stack()[-2]
    syntax_tree = ast.parse(caller.line)
    names = syntax_tree.body[0].value.args
    for name in names:
        try:
            eval("print(f'{name.id} = {args.pop()}')")
        except SyntaxError:
            print('{} = {}'.format(name.id, args.pop()))
