def my_steps(n):
    if n < 1 or n > 25:
        raise ValueError("n is out of range. It should be between 1 and 25 inclusive.")
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # initialize an array to store the number of ways to reach each step.
    waysArray = [0] * (n + 1)

    # we know that there is 1 way to reach 1 step and 2 ways to reach 2 steps, so assign
    # those number of steps to their respective indices
    waysArray[1] = 1
    waysArray[2] = 2

    # calculate the number of ways for the remaining steps
    for i in range(3, n + 1):
        waysArray[i] = waysArray[i - 1] + waysArray[i - 2]

    return waysArray[n]
