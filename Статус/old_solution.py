from pprint import pprint
from typing import List, Dict, Optional


class TreeStore:
    def __init__(self, items: List[Dict]) -> None:
        self.items = items

        self.item_dict = {item['id']: item for item in items}
        self.children_dict = {item['id']: [] for item in items}
        # pprint(self.item_dict)
        # pprint(self.children_dict)

        for item in items:
            parent_id = item['parent']
            if parent_id != "root":
                self.children_dict.setdefault(parent_id, []).append(item)

        # pprint(self.children_dict)

    def _check_exists_element_by_id(self, id: int) -> None:
        if id not in self.item_dict:
            raise ValueError(f"Элемент с id {id} не найден.")

    def getAll(self) -> List[Dict]:
        return self.items

    def getItem(self, id: int) -> Optional[Dict]:
        self._check_exists_element_by_id(id)
        return self.item_dict.get(id)

    def getChildren(self, id: int) -> List[Dict]:
        self._check_exists_element_by_id(id)
        return self.children_dict.get(id, [])

    def getAllParents(self, id: int) -> List[Dict]:
        self._check_exists_element_by_id(id)

        parents = []
        item = self.getItem(id)
        parent_id = item["parent"]

        while parent_id != "root":
            parent_item = self.getItem(parent_id)
            parents.append(parent_item)
            parent_id = parent_item["parent"]

        return parents


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