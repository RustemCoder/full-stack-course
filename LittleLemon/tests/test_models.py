class MenuTest(TestCase):
    def setUp(self) -> None:
        self.item1 = Menu.objects.create(
            title = 'Pizza',
            price = 12.99,
            inventory = 10
        )

    def test_create_menu_item(self) -> None:
        item2 = Menu.objects.create(
            title = 'Burger',
            price = 17.99,
            inventory = 5
        )
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(item2.title, 'Burger')
        self.assertEqual(item2.price, Decimal(17.99))
        self.assertEqual(item2.inventory, 5)
