from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xd6\xb6\x7f1\xda\xd0\xb0k\xb9}b\x03\xed\xd7\x15\xde'
