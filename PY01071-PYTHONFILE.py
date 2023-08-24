import math

def pythonfile(s):
    s = s.lower()
    return 1 if s[-3:]==".py" else 0

def check(n):
    return "yes" if (pythonfile(n)) else "no"

def main():
         n = str(input())
         print(check(n))

if __name__ == "__main__":
    main()