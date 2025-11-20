def main():
    n=int(input("what's n?"))
    for s in sheep(n):
        print(s)

def sheep(s):
    for i in range(s):
        yield "🐑"*i

if __name__=="__main__":
    main()
