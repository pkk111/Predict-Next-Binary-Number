import random

string = ""
count = 100
while count > 0:
    print("Print a random string containing 0 or 1:")
    inp_str = [x for x in list(input()) if x == '0' or x == '1']
    count -= len(inp_str)
    string += "".join(inp_str)
    if count > 0:
        print("Current data length is {0}, {1} symbols left".format(100 - count, count))
    else:
        print("Final data string:")
print(string)

traid = ['000', '001', '010', '011', '100', '101', '110', '111']


def getcount(string, traid, key):
    cnt = 0
    string_len = len(string)
    substring_len = len(traid + key)
    for i in range(string_len - substring_len + 1):
        if string[i: i + substring_len] == traid + key:
            cnt += 1
    return cnt


traid_list = {traid[i]: [getcount(string, traid[i], '0'), getcount(string, traid[i], '1')] for i in range(len(traid))}

print('You have $1000. Every time the system successfully predicts your next press, you lose $1.'
      '\nOtherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')
print("Print a random string containing 0 or 1")
balance = 1000
new_string = input()


def predict(trad):
    if traid_list[trad][0] > traid_list[trad][1]:
        return '0'
    elif traid_list[trad][0] == traid_list[trad][1]:
        return str(round(random.random()))
    return '1'


while balance > 0 and new_string != 'enough':
    new_string = ''.join([x for x in new_string if x == '0' or x == '1'])
    first = round(random.random())
    second = round(random.random())
    third = round(random.random())
    pred_string = str(first) + str(second) + str(third)
    correct = 0
    new_string_length = len(new_string)
    if new_string_length > 3:
        for i in range(new_string_length - 3):
            pred_string += predict(new_string[i:i+3])
            if new_string[i+3: i+3+1] == pred_string[i+3: i+3+1]:
                correct += 1

        print('prediction:')
        print(pred_string)
        print(f'Computer guessed right {correct} out of {new_string_length -3} symbols ({round(correct * 100 / (new_string_length -3), 2)} %)')
        balance -= 2 * correct - (new_string_length - 3)
        print(f'Your balance is now ${balance}')

        for i in traid:
            traid_list[i][0] += getcount(new_string, i, '0')
            traid_list[i][1] += getcount(new_string, i, '1')

    print("Print a random string containing 0 or 1:")
    new_string = input()

print('Game over!')
