"""
Track whether a function is successful or not.
"""
import time

# Proper way of passing arguements to decorators. Use a wrapper function that gathers the args and kwargs
def LogErrors(func):
    """ A decorator that logs to a file in the ./logs/ folder whether the function succeeded or not, with what parameters it was called, and at what time it succeeded or failed."""

    def wrapper(*params, **k_params):
        try: 
            s = func(*params, **k_params)
            directory = os.path.dirname(os.path.abspath(func.__module__))
            directory = f"{directory}/logs/"
            if not os.path.exists(f"{directory}"):
                os.makedirs(f"{directory}")
            log_file = open(f"{directory}{func.__name__}_success.log", "a")
            log_file.write(f"{time.ctime()}: {func.__name__}({params},{k_params}) returned {str(s)}. return type: {type(s)}\n")
            log_file.close()
        except Exception as e:
            directory = os.path.dirname(os.path.abspath(func.__module__))
            directory = f"{directory}/logs/"
            if not os.path.exists(f"{directory}"):
                os.makedirs(f"{directory}")
            log_file = open(f"{directory}{func.__name__}_error.log", "a")
            log_file.write(f"{time.ctime()}: Error with {func.__name__}({params},{k_params}):{str(e)}.\n")
            log_file.close()
            
    return wrapper
