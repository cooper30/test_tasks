from typing import Any

# Описание метода getAllParents(id) противоречит тестовым данным.
# Исходя из задания, метод getAllParents(id)
# "Принимает id элемента и возвращает массив из цепочки родительских элементов,
# начиная от самого элемента, чей id был передан в аргументе и до корневого элемента",
# а в тестовом примере видим элементы начиная от первого родителя текущего элемента до корневого элемента.
# ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]
# Задание выполнено согласно описанию работы метода.
class TreeStore:
    ROOT_ELEMENT = "root"

    def __init__(self, items: list[dict[str, Any]]):
        self._items = items

        self._items_by_id = {}
        self._children_by_parent_id = {}
        self._parents_by_child_id = {}

        items.sort(key=lambda i: i["id"])
        for item in items:
            item_id = item["id"]
            parent_id = item["parent"]

            self._items_by_id[item_id] = item

            if parent_id == self.ROOT_ELEMENT:
                continue

            if parent_id not in self._children_by_parent_id:
                self._children_by_parent_id[parent_id] = [item]
            else:
                self._children_by_parent_id[parent_id].append(item)

            if item_id not in self._parents_by_child_id:
                self._parents_by_child_id[item_id] = [
                    self._items_by_id[parent_id],
                    *self._parents_by_child_id.get(parent_id, ()),
                ]
            else:
                self._parents_by_child_id[item_id].append(self._items_by_id[parent_id])

    def _checkItemExists(self, item_id: int) -> None:
        if item_id not in self._items_by_id:
            raise ValueError(f"Элемент с id {item_id} не найден.")

    def getAll(self) -> list[dict[str, Any]]:
        return self._items

    def getItem(self, item_id: int) -> dict[str, Any]:
        self._checkItemExists(item_id)
        return self._items_by_id[item_id]

    def getChildren(self, parent_id: int) -> list[dict[str, Any]]:
        self._checkItemExists(parent_id)
        return self._children_by_parent_id.get(parent_id, [])

    def getAllParents(self, child_id: int) -> list[dict[str, Any]]:
        self._checkItemExists(child_id)
        return [
            self.getItem(child_id),
            *self._parents_by_child_id.get(child_id, ()),
        ]


def main():
    items = [
        {"id": 1, "parent": "root"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 8, "parent": 4, "type": None},
        {"id": 7, "parent": 4, "type": None},
        {"id": 2, "parent": 1, "type": "test"}
    ]

    ts = TreeStore(items)

    # Тесты
    print(ts.getAll())  # [{"id":1,"parent":"root"}, ...]
    print(ts.getItem(7))  # {"id":7,"parent":4,"type":None}
    print(ts.getChildren(4))  # [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
    print(ts.getChildren(5))  # []
    print(ts.getAllParents(7))  # [{"id":4,"parent":2,"type":"test"}, ...]


if __name__ == "__main__":
    main()
