def ggt(a, b):
    while b:
        a, b = b, a % b
    return a

def kgv(a, b):
    return abs(a * b) // ggt(a, b)

def main():
    num1 = int(input("Gib eine Zahl ein: "))
    num2 = int(input("Gib eine weitere Zahl ein: "))

    gcd = ggt(num1, num2)
    lcm = kgv(num1, num2)

    print("Der größte gemeinsame Teiler von", num1, "und", num2, "ist:", gcd)
    print("Der kleinsten gemeinsamen Vielfachen von", num1, "und", num2, "ist:", lcm)

if __name__ == "__main__":
    main()