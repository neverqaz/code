
import hashlib
def get_md5(str):
    m=hashlib.md5()
    m.update(str)
    return m.hexdigest()