class html_element:

    __template = '<{0[tag]} {0[class]} {0[attr]}>{0[innerHTML]}</{0[tag]}>'
    
    def __init__(self, tag):
        self.__attr = {}
        self.__class = []
        self.__tag = tag
        self.__content = ''

    def toString(self):
        return html_element.__template.format({ \
            'tag': self.__tag, \
            'class': 'class="%s"'%(' '.join(self.__class)), \
            'attr': ' '.join(['%s="%s"'%(key, value) for key, value in self.__attr.items()]),\
            'innerHTML': self.__content, \
        })

    def attr(self, key, value):
        if self.__attr.has_key(key) and value == None:
            self.__attr.pop(key)
            return self
        self.__attr[key] = value
        return self

    def addClass(self, value):
        self.__class.append(value)
        return self

    def removeClass(self, value):
        self.__class.remove(value) if value in self.__class else None
        return self

    def html(self, value):
        self.__content = value
        return self

if __name__ == '__main__':
    print html_element('div').addClass('col-xs-12').attr('data-toggle', 'modal').attr('data-target', '#modal').html('test').toString()

