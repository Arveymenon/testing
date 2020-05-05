def square(x):
    return x*x

def main():
    for i in range(12):
        print("{} is square of {}".format(i, square(i)))

if __name__ == "__main__":
    main()
    pass