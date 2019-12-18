# takes a list of numbers as a parameter
def addition(numbers):

    sum = 0

    for number in numbers:

        sum += number

    return sum


# takes a list of numbers and the total to be subtracted from as a parameter
def subtraction(numbers, total):

    for number in numbers:

        total -= number

    return total


# takes the state (add or subtract), list of numbers and the total to be subtracted from (if state supports it) as a parameter
def main(state, numbers, total):

    if state == "subtract":

        return subtraction(numbers, total)

    elif state == "add":

        return addition(numbers)
