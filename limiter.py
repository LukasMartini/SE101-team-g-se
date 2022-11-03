import time


def limit(wait_time: int):
    def decorator(function):
        def limited(*args, **kwargs):
            def call_function():
                limited._last_called[args[0]] = time.time()
                return function(*args, **kwargs)

            if not hasattr(limited, "_last_called"):
                limited._last_called = {}
                call_function()
            elif time.time() - limited._last_called[args[0]] > wait_time:
                call_function()

        return limited

    return decorator
