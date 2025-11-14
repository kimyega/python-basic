import random

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    print(random_pop(data))

    random.shuffle(data)
    print(data)