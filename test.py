def prefix_decorator(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(prefix, end=" ")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefix_decorator("Log:")
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")  # This will print: "Log: Hello, Alice!"
