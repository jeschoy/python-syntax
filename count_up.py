def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    while start <= stop:
        print(start)
        start = start + 1

    # alternatively:
    # ranges = list(range(start, stop + 1))
    # for num in ranges:
    #     print(num)


count_up(5, 7)        
