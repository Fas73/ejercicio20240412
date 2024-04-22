def main():
    a = True
    b = True
    c = False
    d = True
    e = False

    print(f"a or b: {a or b}")
    print(f"a or c: {a or c}")
    print(f"a and e: {a and e}")
    print(f"(a or e) and b: {(a or e) and b}")
    print(f"(a or e) and c: {(a or e) and c}")
    print(f"(a or e) and (c or b): {(a or e) and (c or b)}")
    print(f"((a and b) and c) or e: {((a and b) and c) or e}")

if __name__ == "__main__":
    main()

