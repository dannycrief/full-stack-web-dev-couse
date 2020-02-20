import time
import bottle


# working from the console
# words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# for word in words:
#     print(word)
#     time.sleep(2)

@bottle.route('/words')
def word_spammer():
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    for word in words:
        yield word
        time.sleep(2)


# check it out
# for w in word_spammer():
#     print(w.upper())

if __name__ == '__main__':
    bottle.run(port=9999)
