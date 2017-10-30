import resource

class test:
    def __init__(self):
        self.test = 'test'

#
# Get the dependence
#
# @param objs list
# @return function
def require(objs):
    def fun(real_func):
	def fake_func(*argv, **kargv):
            for obj in objs:
	        kargv[obj] = resource_manger.get_maker(obj)(*argv)
	    rt = real_func(*argv, **kargv)
	    return rt
	return fake_func
    return fun
		
@require(['test', 'abc'])
def abc(ab, resource=None):
    print ab
    return 'fuck you', 'hahaha'

class tc:
    @require(['fuck', 'you', 'hahaha'])
    def test(self, aa):
        print aa

a = abc('fuck you')
print a

b = tc()
b.test('class')

