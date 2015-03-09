
numbers = {
        '0' : 'zero',
        '1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine',
        '10' : 'ten',
        '11' : 'eleven',
        '12' : 'twelve',
        '13' : 'thirteen',
        '14' : 'fourteen',
        '15' : 'fifteen',
        '16' : 'sixteen',
        '17' : 'seventeen',
        '18' : 'eighteen',
        '19' : 'nineteen',
    }

tens = {
        '2' : 'twenty',
        '3' : 'thirty',
        '4' : 'forty',
        '5' : 'fifty',
        '6' : 'sixty',
        '7' : 'seventy',
        '8' : 'eighty',
        '9' : 'ninety'
    }

def getNumberAsString(x):
    string = ''
    num_list = list(str(x))
    while (len(num_list) > 0):
        if (num_list[0] == '0'):
            x = 1+1
        elif (len(num_list) == 4):
            string += numbers[num_list[0]] + 'thousand'
        elif (len(num_list) == 3):
            string += numbers[num_list[0]] + 'hundred'
            if (num_list[1] > '0' or num_list[2] > '0'):
                string += 'and'
        elif (len(num_list) == 2):
            if (num_list[0] >= '2'):
                string += tens[num_list[0]]
            else:
                num_list[1] = num_list[0] + num_list[1]
        else:
            string += numbers[num_list[0]]
        num_list = num_list[1:]
    return string

def getSeriesStringSize(number):
    string = ''
    for x in range(0,number+1):
        string += getNumberAsString(x)
    return len(string)

if __name__ == '__main__':
    print("[Begin]")
    print("Number as String:", getSeriesStringSize(5))
    print("Number as String:", getSeriesStringSize(1000))

