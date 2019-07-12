#!usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        try:
            u1, u2, country, u3, payment = line.strip().split(',')
            print(country + "\t" + str(payment))
        except:
            print("Invalid input line")

if __name__ == "__main__":
    main()
