
def create_node(data):
    return {"data": data, "next": None}

#ОЧЕРЕДЬ Queue - FIFO
queue_front = None
queue_rear = None

def queue_put(item):
    global queue_front, queue_rear
    new_node = create_node(item)
    if queue_rear is None:
        queue_front = queue_rear = new_node
    else:
        queue_rear["next"] = new_node
        queue_rear = new_node
    print(f"  В очередь добавлен: {item}")

def queue_get():
    global queue_front, queue_rear
    if queue_front is None:
        print("  Очередь пуста!")
        return None
    item = queue_front["data"]
    queue_front = queue_front["next"]
    if queue_front is None:
        queue_rear = None
    print(f"  Из очереди извлечён: {item}")
    return item

def queue_show():
    result = []
    current = queue_front
    while current is not None:
        result.append(current["data"])
        current = current["next"]
    print(f"  Очередь (FIFO): {result}")
    return result

#Stack - FILO
stack_top = None

def stack_push(item):
    global stack_top
    new_node = create_node(item)
    new_node["next"] = stack_top
    stack_top = new_node
    print(f"  В стек добавлен: {item}")

def stack_pop():
    global stack_top
    if stack_top is None:
        print("  Стек пуст!")
        return None
    item = stack_top["data"]
    stack_top = stack_top["next"]
    print(f"  Из стека извлечён: {item}")
    return item

def stack_show():
    result = []
    current = stack_top
    while current is not None:
        result.append(current["data"])
        current = current["next"]
    print(f"  Стек (FILO): {result}")
    return result

# Deque - двусторонняя очередь 
deque_front = None
deque_rear = None

def deque_put(item):
    global deque_front, deque_rear
    new_node = create_node(item)
    if deque_rear is None:
        deque_front = deque_rear = new_node
    else:
        deque_rear["next"] = new_node
        deque_rear = new_node
    print(f"  В дек (конец) добавлен: {item}")

def deque_rput(item):
    global deque_front, deque_rear
    new_node = create_node(item)
    if deque_front is None:
        deque_front = deque_rear = new_node
    else:
        new_node["next"] = deque_front
        deque_front = new_node
    print(f"  В дек (начало) добавлен: {item}")

def deque_get():
    global deque_front, deque_rear
    if deque_front is None:
        print("  Дек пуст!")
        return None
    item = deque_front["data"]
    deque_front = deque_front["next"]
    if deque_front is None:
        deque_rear = None
    print(f"  Из дека (начало) извлечён: {item}")
    return item

def deque_rget():
    global deque_front, deque_rear
    if deque_front is None:
        print("  Дек пуст!")
        return None
    
    if deque_front == deque_rear:
        item = deque_front["data"]
        deque_front = deque_rear = None
        print(f"  Из дека (конец) извлечён: {item}")
        return item
    
    current = deque_front
    while current["next"] != deque_rear:
        current = current["next"]
    
    item = deque_rear["data"]
    deque_rear = current
    deque_rear["next"] = None
    print(f"  Из дека (конец) извлечён: {item}")
    return item

def deque_show():
    result = []
    current = deque_front
    while current is not None:
        result.append(current["data"])
        current = current["next"]
    print(f"  Дек: {result}")
    return result
