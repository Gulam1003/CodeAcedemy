import time

def average_time(runs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for i in range(runs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                total_time += (end_time - start_time)
            average_time = total_time / runs
            print(f"Average time =  {average_time} sec, averaged over = {runs} runs")
            return result
        return wrapper
    return decorator

@average_time(runs=5)
def add_numbers(a, b):
    time.sleep(1)
    return a + b

result = add_numbers(3, 5)
print("Sum:", result)
