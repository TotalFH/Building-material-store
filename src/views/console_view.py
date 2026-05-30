from models.product import Product


class ConsoleView:
    def choose_region(self, regions: list[str]) -> str:
        regions_map = {str(i + 1): region for i, region in enumerate(regions)}

        print("Добро пожаловать в магазин")
        print("Выберите регион:\n")
        for key, value in regions_map.items():
            print(f"{key} - {value}")
        print("\nДля выхода из программы нажмите 'q'\n")

        while True:
            choice = self.get_input("> ")

            if choice == "q":
                exit()
            if not choice:
                print("Введите номер региона")
                continue

            region = regions_map.get(choice)

            if region is None:
                print("Неверный выбор. Попробуйте снова")
                continue

            print(f"Вы выбрали: {region}")
            return region

    def show_products(self, products, region: str) -> None:
        print("\nКАТАЛОГ ТОВАРОВ\n")
    
        print(f"{'ID':<3} {'НАЗВАНИЕ':<45} {'КАТЕГОРИЯ':<15} {'ЦЕНА':>8}")
        print("-" * 80)
    
        for product in products:
            price = product.price.get(region, "-")
    
            print(
                f"{product.id:<3} "
                f"{product.name:<45} "
                f"{product.category.name:<15} "
                f"{price:>8}"
            )


    def choose_product(self, products) -> Product | None:
        while True:
            choice = self.get_input("\nВведите ID товара: ")
            
            if choice == "q":
                exit()

            if choice == "0":
                return None

            if not choice:
                print("Введите ID товара")
                continue
    
            if not choice.isdigit():
                print("ID должен быть числом")
                continue
    
            product_id = int(choice)
    
            for product in products:
                if product.id == product_id:
                    print(f"\nВы выбрали: {product.name}")
                    return product
    
            print("Товар не найден")


    def confirm_order(self) -> str:
        while True:
            choice = input("\nОформляем заявку? (y/n, 0 - назад): ").strip().lower()

            if choice == "y":
                return "yes"

            if choice == "n":
                return "no"

            if choice == "0":
                return "back"

            print("Введите y, n или 0 для возврата")


    def get_input(self, message: str) -> str:
        try:
            return input(message).strip()
        except KeyboardInterrupt:
            print("\nВыход из программы")
            exit()

    def show_offer(self, offer: dict) -> None:
        print("\n" + "=" * 50)
        print("        СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ")
        print("=" * 50)
    
        if offer["type"] == "discount":
            print(f"\n  {offer['product'].name}")
            print(f"\n  Старая цена:  {offer['old_price']:.2f}")
            print(f"  Новая цена:   {offer['final_price']:.2f}  (-5%)")
        else:
            print(f"\n  Предлагаем товар:    {offer['product'].name}")
            print(f"  Цена:         {offer['final_price']:.2f}")
            print(f"\n  Дешевле чем:  {offer["old_product"].name} -- {offer['old_price']:.2f}")
    
        print("=" * 50)

    def show_success(self) -> None:
        print("/n" + "Заказ успешно создан, возврат на главную страницу")

    def show_error(self, error_message: str) -> None:
        print(error_message)


