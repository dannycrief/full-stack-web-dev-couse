from trello import TrelloApi

api_key = '4bc1fc7385ed7fdf3134f511c5531d03'
token = '38ca4209db4c5a0b77233ca3dc7762dbf473e825658db23353bffc0dcae6ee64'
trello = TrelloApi(api_key, token)

response = trello.boards.new('Created with API')
print(response)

board_id = response['id']
for column in trello.boards.get_list(board_id):
    print(column['name'])

for column in trello.boards.get_list(board_id):
    if 'To Do' in column['name']:
        list_id = column['id']
        print(trello.lists.get_card(list_id))

# card = trello.cards.new('Start learning Trello API', list_id)
# print(card)
