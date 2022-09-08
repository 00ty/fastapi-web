import hashlib,base64,os

def get_password_hash(password: str) -> str:
    return hashlib.sha1(password.encode('utf-8')).hexdigest()
    
def verify_password(password: str, hashed_password: str) -> bool:
    hash_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    if hash_password == hashed_password :
        return True
        pass
    return False
# 生成token
def get_token(index: str,str_obj: str) -> str:
    sha1 = hashlib.sha1(str_obj.encode('utf-8')).hexdigest()
    token = base64.b64encode(sha1.encode('utf-8'))
    # 写文件
    fo = open(f'data/token/{index}.log', 'wb')
    fo.write(token)
    fo.close()
    return token.decode().replace('=', '')
# 验证Token
def has_token(tokenStr: str):
  try:
    token = tokenStr.split('.')[2]
    username = tokenStr.split('.')[0]
  except Exception:
    return False
  file_name = f'data/token/{username}.log'
  if os.path.exists(file_name) == False:
    return False
  file= open(file_name,'r')
  data = file.read()
  file.close()
  if data.replace('=', '') == token:
    return True
  return False
