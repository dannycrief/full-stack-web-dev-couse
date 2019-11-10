from sample_tag import Tag

with Tag("h1") as tag:
    tag.text = "Hello World"
    tag.attributes["class"] = "my_amazing_class"

with Tag("img", True) as tag:
    tag.attributes["class"] = "my_amazing_class"
    tag.attributes["src"] = "./tmp/my-logo.png"