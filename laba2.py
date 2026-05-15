combinations = {
    frozenset(["огонь", "вода"]): "пар",
    frozenset(["огонь", "земля"]): "лава",
    frozenset(["вода", "земля"]): "грязь",
    frozenset(["воздух", "вода"]): "дождь",
    frozenset(["воздух", "огонь"]): "энергия",
    frozenset(["воздух", "земля"]): "пыль",
    frozenset(["пар", "воздух"]): "облако",
    frozenset(["лава", "вода"]): "камень",
}

class Element:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        key = frozenset([self.name, other.name])
        
        if key in combinations:
            result_name = combinations[key]
            return Element(result_name)
        
        return None

    def decompose(self):
        for elements, result in combinations.items():
            if result == self.name:
                return tuple(elements)
        return None

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Element('{self.name}')"


class AlchemyGame:
    def __init__(self):
        self.elements = {
            "огонь": Element("огонь"),
            "вода": Element("вода"),
            "земля": Element("земля"),
            "воздух": Element("воздух"),
        }

    def combine(self, name1, name2):
        if name1 not in self.elements:
            print(f" Элемент '{name1}' не найден!")
            return None
        
        if name2 not in self.elements:
            print(f" Элемент '{name2}' не найден!")
            return None
        
        elem1 = self.elements[name1]
        elem2 = self.elements[name2]
        
        result = elem1 + elem2
        
        if result is not None:
            if result.name not in self.elements:
                self.elements[result.name] = result
                print(f" {name1} + {name2} = {result.name.upper()} ")
            else:
                print(f" {name1} + {name2} = {result.name} (уже есть)")
            return result
        
        print(f" {name1} + {name2} = ничего")
        return None

    def decompose(self, name):
        if name not in self.elements:
            print(f" Элемент '{name}' не найден!")
            return None
        
        result = self.elements[name].decompose()
        
        if result:
            print(f" {name} = {result[0]} + {result[1]}")
        else:
            print(f" {name} - базовый элемент (нельзя разложить)")
        
        return result

    def show_elements(self):
        if not self.elements:
            print("Нет элементов")
            return []
        
        print("\n ВАШИ ЭЛЕМЕНТЫ:")
        print("-" * 25)
        for i, name in enumerate(sorted(self.elements.keys()), 1):
            print(f"  {i}. {name}")
        print("-" * 25)
        print(f"Всего: {len(self.elements)} элементов\n")
        
        return list(self.elements.keys())
    
    def show_available_recipes(self):
        print("\n ДОСТУПНЫЕ РЕЦЕПТЫ:")
        print("-" * 25)
        
        found = False
        for (elem1, elem2), result in combinations.items():
            elem1, elem2 = tuple(elem1)
            if elem1 in self.elements and elem2 in self.elements:
                if result not in self.elements:
                    print(f"  {elem1} + {elem2} = {result}")
                    found = True
        
        if not found:
            print("  Нет новых рецептов!")
        print("-" * 25)
    
    def reset(self):
        self.elements = {
            "огонь": Element("огонь"),
            "вода": Element("вода"),
            "земля": Element("земля"),
            "воздух": Element("воздух"),
        }
        print(" Игра сброшена!")


def play_game():
    game = AlchemyGame()
    
    print("=" * 45)
    print("         АЛХИМИЯ (простая версия)")
    print("=" * 45)
    print("\nКоманды:")
    print("  combine <элемент1> <элемент2>  - соединить элементы")
    print("  decompose <элемент>            - разложить элемент")
    print("  list                           - показать все элементы")
    print("  recipes                        - показать доступные рецепты")
    print("  reset                          - начать заново")
    print("  exit                           - выйти")
    print("\n" + "=" * 45)
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command == "exit":
            print("До свидания!")
            break
        
        elif command == "list":
            game.show_elements()
        
        elif command == "recipes":
            game.show_available_recipes()
        
        elif command == "reset":
            game.reset()
        
        elif command.startswith("combine"):
            parts = command.split()
            if len(parts) == 3:
                _, elem1, elem2 = parts
                game.combine(elem1, elem2)
            else:
                print("Использование: combine <элемент1> <элемент2>")
                print("Пример: combine огонь вода")
        
        elif command.startswith("decompose"):
            parts = command.split()
            if len(parts) == 2:
                _, elem = parts
                game.decompose(elem)
            else:
                print("Использование: decompose <элемент>")
                print("Пример: decompose пар")
        
        elif command == "help":
            print("\nДоступные команды:")
            print("  combine <элемент1> <элемент2>  - соединить два элемента")
            print("  decompose <элемент>            - разложить элемент")
            print("  list                           - показать все элементы")
            print("  recipes                        - показать возможные новые рецепты")
            print("  reset                          - начать игру заново")
            print("  exit                           - выйти")
        
        else:
            print("Неизвестная команда. Введите 'help' для справки.")


def demo_mode():
    print("\n" + "=" * 45)
    print("         ДЕМОНСТРАЦИОННЫЙ РЕЖИМ")
    print("=" * 45)
    
    game = AlchemyGame()
    
    print("\nНачальные элементы:", list(game.elements.keys()))
    
    print("\n--- СОЗДАЁМ НОВЫЕ ЭЛЕМЕНТЫ ---")
    game.combine("огонь", "вода")
    game.combine("огонь", "земля")
    game.combine("вода", "земля")
    game.combine("воздух", "вода")
    game.combine("воздух", "огонь")
    game.combine("воздух", "земля")
    game.combine("пар", "воздух")
    game.combine("лава", "вода")
    
    print("\n--- РАЗЛАГАЕМ ЭЛЕМЕНТЫ ---")
    game.decompose("пар")
    game.decompose("лава")
    game.decompose("облако")
    game.decompose("камень")
    game.decompose("огонь")
    
    print("\n--- ИТОГОВЫЙ СПИСОК ---")
    game.show_elements()
    
    print("\n--- ДОСТУПНЫЕ РЕЦЕПТЫ ---")
    game.show_available_recipes()


if __name__ == "__main__":
    print("Выберите режим:")
    print("1. Демонстрационный режим (автоматический)")
    print("2. Интерактивный режим (играть самому)")
    
    choice = input("\nВаш выбор (1 или 2): ").strip()
    
    if choice == "1":
        demo_mode()
    elif choice == "2":
        play_game()
    else:
        print("Неверный выбор. Запускаем демонстрационный режим.")
        demo_mode()
