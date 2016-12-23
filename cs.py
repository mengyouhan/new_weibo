old = '0.1'
print(old)
def diff(new):
    global old
    if new == old:
        print('meiyou old:{}'.format(old))
    else:
        old = new
        print('gengxin old:{}'.format(old))