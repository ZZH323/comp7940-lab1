def main():
    print("Hello world")
if __name__ == '__main__':
    main()

# Ex 1
x = 52633
for i in range(x+1):
    i = i + 1
    if(x % i == 0):
        print(i)
    else:
        continue

# Ex 2
def print_factor(x):
    for i in range(x+1):
        i = i + 1
        if(x % i == 0):
            print(i)
        else:
            continue
x = 52633
print_factor(x)

# Ex 3
l = [52633, 8137, 1024, 999]
for m in range(len(l)):
    for i in range (l[m]+1):
        i = i + 1
        if(l[m] % i == 0):
            print(i)
        else:
            continue