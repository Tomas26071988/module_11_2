import inspect

def introspection_info(obj):
    info = {'type': type(obj).__name__,  # тип объекта
            'attributes': [attr for attr in dir(obj) if not attr.startswith('__') and not callable(getattr(obj, attr))],     # атрибут объекта
            'methods': [meth for meth in dir(obj) if meth.startswith('__')],    # метод объекта
            'module': inspect.getmodule(introspection_info).__name__,}      # модуль объекта

    return info




number_info = introspection_info(42)
print(number_info)

