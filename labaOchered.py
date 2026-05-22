class Queue:
    """Очередь - FIFO (First In, First Out)"""
    
    def __init__(self):
        self._items = []
    
    def Put(self, item):
        self._items.append(item)
        print(f"  В очередь добавлен: {item}")
    
    def Get(self):
        if not self._items:
            print("  Очередь пуста!")
            return None
        item = self._items.pop(0)
        print(f"  Из очереде извлечён: {item}")
        return item
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def show(self):
        print(f"  Очередь (FIFO): {self._items}")
        return self._items

class Stack:
    """Стек - FILO (First In, Last Out)"""
    
    def __init__(self):
        self._items = []
    
    def Push(self, item):
        self._items.append(item)
        print(f"  В стек добавлен: {item}")
    
    def Pull(self):
        if not self._items:
            print("  Стек пуст!")
            return None
        item = self._items.pop()
        print(f"  Из стека извлечён: {item}")
        return item
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def show(self):
        print(f"  Стек (FILO): {self._items}")
        return self._items

class Deque:
    
    def __init__(self):
        self._items = []
    
    def Put(self, item):
        self._items.append(item)
        print(f"  В дек (конец) добавлен: {item}")
    
    def RPut(self, item):
        self._items.insert(0, item)
        print(f"  В дек (начало) добавлен: {item}")
    
    def Get(self):
        if not self._items:
            print("  Дек пуст!")
            return None
        item = self._items.pop(0)
        print(f"  Из дека (начало) извлечён: {item}")
        return item
    
    def RGet(self):
        if not self._items:
            print("  Дек пуст!")
            return None
        item = self._items.pop()
        print(f"  Из дека (конец) извлечён: {item}")
        return item
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def show(self):
        print(f"  Дек: {self._items}")
        return self._items

class ShopQueue:
    """
    Использует Queue (FIFO) для обслуживания покупателей
    """
    
    def __init__(self, name="Магазин"):
        self.name = name
        self.queue = Queue()
        self.served_customers = Stack()  
        self.waiting_deque = Deque()    
    
    def add_customer(self, name):
        print(f"\n[+] {name} встал(а) в очередь")
        self.queue.Put(name)
        self._show_last_node()
    
    def serve_customer(self):
        print(f"\n[-] Обслуживание...")
        customer = self.queue.Get()
        if customer:
            self.served_customers.Push(customer)
            print(f" {customer} обслужен(а) и покинул(а) магазин")
        self._show_last_node()
    
    def add_urgent_customer(self, name):
        print(f"\n[!] СРОЧНО! {name} проходит без очереди!")
        self.waiting_deque.RPut(name)
        self._show_last_node()
    
    def _show_last_node(self):
        if not self.queue.is


mpty():
            print(f"  Last NodeList: {self.queue._items[-1]}")
        else:
            print(f"  Last NodeList: None")
    
    def show_status(self):
        print("\n" + "="*50)
        print(f"  Магазин: {self.name}")
        print("="*50)
        print("  ТЕКУЩАЯ ОЧЕРЕДЬ (FIFO):")
        self.queue.show()
        print("\n  ИСТОРИЯ ОБСЛУЖЕННЫХ (FILO):")
        self.served_customers.show()
        print("\n  ОСОБЫЙ ДЕК:")
        self.waiting_deque.show()
        print("="*50)
    
    def run_simulation(self):
        print("\n" + "="*50)
        print("  СИМУЛЯЦИЯ РАБОТЫ МАГАЗИНА")
        print("="*50)
        
        customers = ["Анна", "Борис", "Виктор", "Галина", "Дмитрий"]
        for c in customers:
            self.add_customer(c)
        
        print("\n" + "-"*50)
        self.show_status()
        
        self.serve_customer()
        self.serve_customer()
        self.serve_customer()
        
        print("\n" + "-"*50)
        print("\n[!] Экстренная ситуация: пришёл важный клиент!")
        self.add_urgent_customer("ЕЛЕНА (VIP)")
        
        print("\n" + "-"*50)
        self.show_status()
        
        self.serve_customer()
        self.serve_customer()
        self.serve_customer()
        
        print("\n" + "-"*50)
        print("\n[ФИНАЛЬНЫЙ СТАТУС]")
        self.show_status()
        
        print("\n" + "="*50)
        print("  РАБОТА МАГАЗИНА ЗАВЕРШЕНА")
        print("="*50)

def demonstrate_structures():
    """Демонстрация всех структур данных из файла"""
    print("\n" + ""*60)
    print("  ДЕМОНСТРАЦИЯ СТРУКТУР ДАННЫХ")
    print(""*60)
    
    # QUEUE (FIFO) 
    print("\n" + "─"*40)
    print("1. ОЧЕРЕДЬ (Queue) - FIFO")
    print("   Первый пришёл - первый ушёл")
    print("─"*40)
    q = Queue()
    q.Put("Покупатель 1")
    q.Put("Покупатель 2")
    q.Put("Покупатель 3")
    q.show()
    q.Get()
    q.Get()
    q.show()
    
    # STACK (FILO)
    print("\n" + "─"*40)
    print("2. СТЕК (Stack) - FILO")
    print("   Первый пришёл - последний ушёл")
    print("─"*40)
    s = Stack()
    s.Push("Товар A")
    s.Push("Товар B")
    s.Push("Товар C")
    s.show()
    s.Pull()
    s.Pull()
    s.show()
    
    # DEQUE 
    print("\n" + "─"*40)
    print("3. ДЕК (Deque) - двусторонняя очередь")
    print("   Put - в конец, RPut - в начало")
    print("─"*40)
    d = Deque()
    d.Put("Обычный клиент")
    d.RPut("VIP клиент")
    d.Put("Ещё один клиент")
    d.show()
    d.Get() 
    d.RGet()
    d.show()

if __name__ == "__main__":
    demonstrate_structures()
    
    print("\n" + "═"*60)
    print("  ОСНОВНАЯ СИМУЛЯЦИЯ: ОЧЕРЕДЬ В МАГАЗИНЕ")
    print("═"*60)
    shop = ShopQueue("Пятёрочка")
    shop.run_simulation()_e
