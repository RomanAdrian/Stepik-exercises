first_number = int(input())

d = dict(input().split() for _ in range(first_number))


def description(**kwargs):
    for k,v in kwargs.items():
       return "The " + str(k) + " " + ": " + str(v)

print(description(**d))