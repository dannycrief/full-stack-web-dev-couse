import zipfile
from event_parser import create_event_obj

events = []

with zipfile.ZipFile("data_500.zip") as zipf:
	with zipf.open("data_500.json") as jsonf:
		for idx, line in enumerate(jsonf):
			if idx == 20:
				break
			event_obj = create_event_obj(line)
			events.append(event_obj)


item_prices = []
for event in events:
	item_prices.append(int(event.item_price))

print(sum(item_prices))
