def main():
    s = str(input())
    ch = ct =0
    for i in s:
        if i>='a' and i<='z':
            ct += 1
        if i>='A' and i<='Z':
            ch += 1
    if ct >= ch: print(s.lower())
    if ch > ct: print(s.upper())
if __name__ == '__main__':
    main()