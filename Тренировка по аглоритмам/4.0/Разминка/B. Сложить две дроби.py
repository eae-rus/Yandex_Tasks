import math

def main():
    a, b, c, d  = list(map(int, input().split()))
    numerator = a * d + b * c
    denominator = b * d
    gcd = math.gcd(numerator, denominator) # наибольший общий делитель (НОД)
    print(numerator // gcd, denominator // gcd)
        
if __name__ == '__main__':
	main()