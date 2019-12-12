from bottle import route
from bottle import run
from bottle import HTTPError

import album

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Album {} nie jest znaleziony".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Lista albumów {}<br>".format(artist)
        result += "<br>".join(album_names)
    return result


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)



