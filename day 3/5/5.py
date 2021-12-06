'''
Solution for exercise 5 of Advent of Code 2021

Input is read into the lines array, then the number of ones at each position is counted.
Since the numbers are binary there are two options at each position - there are more ones if 
number of them is bigger than half of all numbers.
'''

def main():
    f = open("5/5_input.txt", "r")
    lines = f.readlines()
    f.close()

    ones = [0]*12
    for line in lines:
        for i in range(12):
            ones[i] += int(line[i])
    gamma = [1 if ones[i]>len(lines)/2 else 0 for i in range(12)]
    epsilon = [0 if ones[i]>len(lines)/2 else 1 for i in range(12)]
    val_g = 0
    val_e = 0
    for i in range(12):
        val_g += gamma[12-i-1]*2**i
        val_e += epsilon[12-i-1]*2**i
    print(val_g, val_e, val_g*val_e)

if __name__ == "__main__":
    main()