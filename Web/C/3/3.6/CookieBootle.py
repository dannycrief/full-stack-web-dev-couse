import bottle


@bottle.route('/')
def default():
    if bottle.request.get_cookie('visited'):
        return {
            'visited': True,
            'message': 'Welcome here again'
        }
    bottle.response.set_cookie('visited', 'yes')
    return {
        'visited': False,
        'message': 'You here at first.'
    }


if __name__ == '__main__':
    bottle.run(port=9090)
