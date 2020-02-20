import sys
import json
import collections


def load_log(path):
    """
    Принимает на вход путь к файлу с журналом, десериализуем его и возвращает список отфильтрованных событий
    """
    fp = open(path, encoding='utf-8')
    events = []
    for line in fp: # читаем файл построчно
        event = json.loads(line) # десериализуем JSON документ
        if not event["detectedDuplicate"] and not event["detectedCorruption"]:
            # сохраняем в список events отфильтрованные события
            events.append(event)
    return events # возвращаем полученный список событий


def main():
    log_path = sys.argv[1]
    events = load_log(log_path)

    user_agents = set()
    total_sum = 0
    # Создаем счетчик для хранения количества звездочек, для каждого товара
    favourite_items = collections.Counter()

    for event in events:
        user_agents.add(event["userAgentName"])
        if event["eventType"] == "itemBuyEvent":
            total_sum += event["item_price"]
        # если событие типа itemFavEvent
        elif event["eventType"] == "itemFavEvent":
            # запоминаем идентификатор товара
            item_id = event["item_id"]
            # увеличиваем счетчик для данного идентификатора товара
            favourite_items[item_id] += 1

    print("Количество браузеров: ", len(user_agents))
    print("Общая сумма покупок: ", total_sum)

    # Выводим количество различных товаров, добавленных в избранное
    print("Количество различных товаров, добавленных в избранное: ", len(favourite_items))

    # Для каждого идентификатора товара выводим количество звездочек
    for item_id, cnt in favourite_items.items():
        print("{} - {}".format(item_id, cnt))


if __name__ == "__main__":
    main()