from task import Tag

paragraph = Tag(
    "p",
    klass=("text-align-right", "text-nice"),
    id="heading-text",
    data_bind="a1-above"
)
paragraph.text = "Some text inside tag"
print(paragraph)
