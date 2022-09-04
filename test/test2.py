import example_cython, example_original, time

if __name__ == '__main__':
    times = 10000
    add_times = 100

    # original
    original_total_elapse = 0.0
    for i in range(times):
        start_time = time.time()
        example_original.test(add_times)
        original_total_elapse += time.time() - start_time

    # cython
    cython_total_elapse = 0.0
    for i in range(times):
        start_time = time.time()
        example_cython.test(add_times)
        cython_total_elapse += time.time() - start_time

    print("Cython is {}x faster.".format(original_total_elapse / cython_total_elapse) )
