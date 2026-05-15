import pickle
import os
from functools import wraps

def cache(file_name=None, use_args=True, use_kwargs=False, use_pickle=False):
    def decorator(func):
        cache_data = {}
        if file_name and os.path.exists(file_name):
            try:
                if use_pickle:
                    with open(file_name, 'rb') as f:
                        cache_data = pickle.load(f)
                else:
                    import json
                    with open(file_name, 'r', encoding='utf-8') as f:
                        cache_data = json.load(f)
                print(f"Загружено {len(cache_data)} записей из {file_name}")
            except Exception as e:
                print(f"Ошибка загрузки: {e}")
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache_data
            key_parts = []
            if use_args:
                key_parts.append(('args', args))
            if use_kwargs:
                key_parts.append(('kwargs', tuple(sorted(kwargs.items()))))
            
            key = tuple(key_parts) if key_parts else ('no_args',)
            try:
                key_str = str(key)
            except:
                key_str = repr(key)
            
            if key_str in cache_data:
                print(f"Кэш: {args} {kwargs}")
                return cache_data[key_str]
            
            print(f"Вычисление: {args} {kwargs}")
            result = func(*args, **kwargs)
            cache_data[key_str] = result
    
            if file_name:
                try:
                    if use_pickle:
                        with open(file_name, 'wb') as f:
                            pickle.dump(cache_data, f)
                    else:
                        import json
                        with open(file_name, 'w', encoding='utf-8') as f:
                            json.dump(cache_data, f, ensure_ascii=False, indent=2, default=str)
                except Exception as e:
                    print(f"Ошибка сохранения: {e}")
            
            return result
        
        return wrapper
    return decorator
