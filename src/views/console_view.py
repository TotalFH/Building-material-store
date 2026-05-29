class ConsoleView:
    REGIONS = {
        "1": "СПБ",
        "2": "МСК",
        "3": "КРД",
    }

    def choose_region(self) -> str:
        print("Добро пожаловать в магазин")
        print("Выберите регион:\n")

        for key, value in self.REGIONS.items():
            print(f"{key} - {value}")

        while True:
            try:
                choice = input("> ").strip()
    
                if not choice:
                    print("Введите номер региона")
                    continue
    
                region = self.REGIONS.get(choice)
    
                if region is None:
                    print("Неверный выбор. Попробуйте снова")
                    continue
    
                print(f"Вы выбрали: {region}")
                return region
    
            except KeyboardInterrupt:
                print("\nВыход из программы")
                exit()

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
