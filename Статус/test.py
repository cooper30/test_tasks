import unittest

from main import TreeStore


class TestTreeStore(unittest.TestCase):

    def setUp(self):
        self.items = [
            {"id": 1, "parent": "root"},
            {"id": 3, "parent": 1, "type": "test"},
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 5, "parent": 2, "type": "test"},
            {"id": 6, "parent": 2, "type": "test"},
            {"id": 8, "parent": 4, "type": None},
            {"id": 7, "parent": 4, "type": None},
            {"id": 2, "parent": 1, "type": "test"}
        ]
        self.ts = TreeStore(self.items)

    def test_get_all(self):
        self.assertEqual(self.ts.getAll(), self.items)

    def test_get_item(self):
        self.assertEqual(self.ts.getItem(7), {"id": 7, "parent": 4, "type": None})

    def test_get_children(self):
        self.assertEqual(self.ts.getChildren(4),
                         [{"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}])
        self.assertEqual(self.ts.getChildren(5), [])  # Элемент 5 не имеет дочерних

    def test_get_all_parents(self):
        self.assertEqual(
            self.ts.getAllParents(7),
            [
                {'id': 7, 'parent': 4, 'type': None},
                {"id": 4, "parent": 2, "type": "test"},
                {"id": 2, "parent": 1, "type": "test"},
                {"id": 1, "parent": "root"}
            ],
        )

        self.assertEqual(
            self.ts.getAllParents(2),
            [
                {"id": 2, "parent": 1, "type": "test"},
                {"id": 1, "parent": "root"}
            ],
        )

        self.assertEqual(
            self.ts.getAllParents(1),
            [
                {"id": 1, "parent": "root"}
            ],
        )

    def test_get_item_not_found(self):
        with self.assertRaises(ValueError) as context:
            self.ts.getItem(99)  # Элемент с id 99 не существует
        self.assertEqual(str(context.exception), "Элемент с id 99 не найден.")

    def test_get_children_not_found(self):
        with self.assertRaises(ValueError) as context:
            self.ts.getChildren(99)  # Элемент с id 99 не существует
        self.assertEqual(str(context.exception), "Элемент с id 99 не найден.")

    def test_get_all_parents_not_found(self):
        with self.assertRaises(ValueError) as context:
            self.ts.getAllParents(99)  # Элемент с id 99 не существует
        self.assertEqual(str(context.exception), "Элемент с id 99 не найден.")


if __name__ == '__main__':
    unittest.main()
