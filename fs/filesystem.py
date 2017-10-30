class filesystem(object):
    def __init__(self, kargv):
        self.conf = kargv
        if not self.validate():
            raise Exception('FS setting is not correct')
    # validate the setting
    def validate(self):
        return True
    def save(self, istream, local_url):
        url = '%s/%s' % (self.conf['url'], local_url)
        f = open(url, 'wb+')
        f.write(istream.read())
        f.close()
        return True
    def delete(self, local_url):
        url = '%s/%s' % (self.conf['url'], local_url)
        os.unlink(url)
        return True
    # move file to a new location, delete = False will act as copy
    def move(self, cur_url, new_url, another_fs = None, delete=True):
        if another_fs is None:
            another_fs = self
        cur_full_url = '%s/%s' % (self.conf['url'], cur_url)
        new_full_url = '%s/%s' % (another_fs.conf['url'], new_url)
        if delete:
            shutil.move(cur_full_url, new_full_url)
        else:
            shutil.copy(cur_full_url, new_full_url)
        return True
    
