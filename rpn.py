#!/usr/bin/env python3

def calculate(myarg1):
	for token in myarg1.split():
    print(token)

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()
