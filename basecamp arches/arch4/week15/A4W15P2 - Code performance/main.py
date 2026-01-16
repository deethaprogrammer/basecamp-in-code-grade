import time

def time_wrapper(func):
    def elapsed_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"executed in: {duration} seconds")
        return result
    return elapsed_time

@time_wrapper
def multiply(x: int, y: int):
    multi = x * y
    return multi

if __name__ == "__main__":
    print(multiply(4, 6))