def main():
    n=int(input("what's n?"))
    for s in sheep(n):
        print(s)

def sheep(s):
    flock=[]
    for i in range(s):
        flock.append("🐑"*i)
    return flock

if __name__=="__main__":
    main()
