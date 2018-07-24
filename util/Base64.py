# coding=utf-8
import base64
import hashlib

key = 'YXNqYWhzaXlnd3lpcWh1d2'

#加密
def md5hex(data):
    m2 = hashlib.md5()
    m2.update(data.encode("utf-8"))
    return m2.hexdigest()

def encrypt(data):
    text = base64.b64encode(data.encode('utf-8'))
    text = str(text,'utf-8')
    count = text.count('=')
    text = key + text.replace('=', '')+str(count)+key
    return text
 
def decrypt(data):
    data = data.replace(key,'')
    count = data[len(data)-1 : len(data)]
    data = data[0 : len(data)-1]
    for i in range(int(count)):
        data = data + '='
    text = base64.b64decode(data.encode('utf-8'))
    text = str(text,'utf-8')
    return text

#print(decrypt(encrypt('50683412saihs8t6ygutftg˵��2LiuLin')))
#print(md5hex('HDS_TANZIMINhds123456'))