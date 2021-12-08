import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "16_input.txt")
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    s = 0
    for line in lines:
        line = line.rstrip()
        examples, display = line.split(' | ')
        examples = examples.split(' ')
        display = display.split(' ')
        segments = {
            'up':[],
            'mid':[],
            'down':[],
            'left up':[],
            'right up':[],
            'left down':[],
            'right down':[]
        }
        digits = ['', '', '', '', '', '', '', '', '', '']
        # one = ''
        # two = ''
        # four = ''
        # seven = ''
        # eight = ''
        # nine = ''
        for e in examples:
            if len(e) == 2:
                digits[1] = e
            elif len(e) == 3:
                digits[7] = e
            elif len(e) == 4:
                digits[4] = e
            elif len(e) == 7:
                digits[8] = e
        segments['right down'] = [l for l in digits[1]]
        segments['right up'] = [l for l in digits[1]]
        for l in digits[7]:
            if l not in digits[1]:
                segments['up'].append(l)
        for l in digits[4]:
            if l not in digits[1]:
                segments['mid'].append(l)
                segments['left up'].append(l)
        #Finding nine - 4 + up + one more
        for digit in examples:
            if segments['up'][0] in digit and all([x in digit for x in digits[4]]) and len(digit) == 6:
                digits[9] = digit
        for segment in digits[9]:
            if segment not in digits[4] and segment not in segments['up']:
                segments['down'].append(segment)
        
        #Finding zero and six
        for digit in examples:
            if len(digit) == 6:
                #it's zero or six
                c = 0
                for segment in segments['mid']:
                    if segment in digit:
                        c+=1
                if c == 2 and digit != digits[9]:
                    digits[6] = digit
                elif c == 1:
                    digits[0] = digit
        for segment in digits[0]:
            if segment not in digits[9]:
                segments['left down'].append(segment)
            if segment not in digits[6]:
                segments['right up'] = [segment]
                segments['right down'].remove(segment)
        for digit in examples:
            if len(digit) == 5:
                if segments['right down'][0] in digit and segments['right up'][0] in digit:
                    digits[3] = digit
                elif segments['right down'][0] in digit:
                    digits[5] = digit
                elif segments['right up'][0] in digit:
                    digits[2] = digit

        out = ''
        for digit in display:
            for i, num in enumerate(digits):
                if equal_digits(digit, num):
                    out += str(i)
        # print()
        # print(segments)
        # print(digits)
        # print(display, out)
        s+=int(out)
    print(s)

def equal_digits(first, second):
    if len(first) != len(second):
        return False
    
    for l in first:
        if l not in second:
            return False
    return True

    

if __name__ == "__main__":
    main()