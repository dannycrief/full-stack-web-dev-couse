from http import cookies
from datetime import timedelta, datetime as dt

c = cookies.SimpleCookie()

c['partial_cookie'] = 'cookie_value'
c['partial_cookie']['path'] = '/pyw/test'
c['partial_cookie']['domain'] = 'skillfactory'
c['partial_cookie']['secure'] = True

c['cookie_expiring_age'] = 'expires in 5 minutes'
c['cookie_expiring_age']['max-age'] = 300  # in seconds

c['expires_at_time'] = 'cookie_value'
time_to_live = timedelta(hours=1)
expiration = (dt(2020, 2, 26, 19, 30, 14) + time_to_live)

c['expires_at_time']['expires'] = expiration.strftime('%a, %d %b %Y %H:%M:%S')

print(c)
print('==================')
print(c.js_output())
