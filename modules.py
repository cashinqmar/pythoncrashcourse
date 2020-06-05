import datetime
from datetime import date
import time
from time import time

import validator
from validator import validate_email
#pip module

from camelcase import CamelCase

today=date.today()
timestamp=time()

print(today)
print(timestamp)

c=CamelCase()

email='testtest.com'

if validate_email(email):
    print('email valid')
else:
    print('not valid')


print(c.hump('hello there world'))