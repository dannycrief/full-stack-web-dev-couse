import json

fp = open("file.txt")


def handle_json_document(document):
    pass


try:
    document = json.load(fp)
    result = handle_json_document(document)
except json.decoder.JSONDecodeError as err:
    print("This is an error JSON", err)
finally:
    fp.close()
