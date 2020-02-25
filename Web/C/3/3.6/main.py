from http import cookies

my_cookie = cookies.SimpleCookie()
my_cookie['user'] = 'Stepan'
my_cookie['hash'] = 'eGhiex0paiT8zaYeieJie6saRo1sha5T'

print(my_cookie)