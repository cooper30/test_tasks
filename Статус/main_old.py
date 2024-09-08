from typing import Any


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.parent = None
#         self.children = []


class TreeStore:
    NOT_FOUND_MSG = "Элемент с id {} не найден."
    ROOT_ELEMENT = "root"

    def __init__(self, items: list[dict[str, Any]]):
        self._items = items
        self._items_cache = {}

        for item in items:
            self._items_cache[item["id"]] = {
                "item": item,
                "children": [],
                "parents": [],
            }

        for item in items:
            item_id = item["id"]
            parent_id = item["parent"]
            if parent_id != self.ROOT_ELEMENT:
                self._items_cache[parent_id]["children"].append(self._items_cache[item_id]["item"])

            while parent_id != self.ROOT_ELEMENT:
                self._items_cache[item_id]["parents"].append(self._items_cache[parent_id]["item"])
                parent_id = self._items_cache[parent_id]["item"]["parent"]

    def _checkItemExists(self, id: int) -> None:
        if id not in self._items_cache:
            raise ValueError(self.NOT_FOUND_MSG.format(id))

    def getAll(self):
        return self._items

    def getItem(self, id: int) -> dict:
        self._checkItemExists(id)
        return self._items_cache[id]["item"]

    def getChildren(self, id: int) -> list[dict]:
        self._checkItemExists(id)
        return self._items_cache[id]["children"]

    def getAllParents(self, id: int) -> List[Dict]:
        self._checkItemExists(id)
        return self._items_cache[id]["parents"]


if __name__ == "__main__":
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    ts = TreeStore(items)

    # Тесты
    print(ts.getAll())  # [{"id":1,"parent":"root"}, ...]
    print(ts.getItem(7))  # {"id":7,"parent":4,"type":None}
    print(ts.getChildren(4))  # [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
    print(ts.getChildren(5))  # []
    print(ts.getAllParents(7))  # [{"id":4,"parent":2,"type":"test"}, ...]
