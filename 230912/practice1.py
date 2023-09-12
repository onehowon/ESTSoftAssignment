def print_args_kwargs(*args, **kwargs):
    print('args:', args)
    for x in args:
        print(x)
    print('kwargs:', kwargs)
    for x in kwargs:
        print(x)
        print(kwargs[x])


inputlist = [100, True, 'leehojun']
inputdic = {'score':100, 'name':'leehojun', 'age':'10'}
print_args_kwargs(*inputlist)
print('--------')
print_args_kwargs(**inputdic)
print('----------')
print_args_kwargs(*inputlist, **inputdic)