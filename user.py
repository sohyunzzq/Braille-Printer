import serial
import time

### 사용자 환경에 맞게 포트 수정
PORT = 'COM4'

# 해당 문자에 맞는 점자
braille = {
    'a': ['OX', 'XX', 'XX'], 'b': ['OX', 'OX', 'XX'], 'c': ['OO', 'XX', 'XX'], 'd': ['OO', 'XO', 'XX'],
    'e': ['OX', 'XO', 'XX'], 'f': ['OO', 'OX', 'XX'], 'g': ['OO', 'OO', 'XX'], 'h': ['OX', 'OO', 'XX'],
    'i': ['XO', 'OX', 'XX'], 'j': ['XO', 'OO', 'XX'], 'k': ['OX', 'XX', 'OX'], 'l': ['OX', 'OX', 'OX'],
    'm': ['OO', 'XX', 'OX'], 'n': ['OO', 'XO', 'OX'], 'o': ['OX', 'XO', 'OX'], 'p': ['OO', 'OX', 'OX'],
    'q': ['OO', 'OO', 'OX'], 'r': ['OX', 'OO', 'OX'], 's': ['XO', 'OX', 'OX'], 't': ['XO', 'OO', 'OX'],
    'u': ['OX', 'XX', 'OO'], 'v': ['OX', 'OX', 'OO'], 'w': ['XO', 'OO', 'XO'], 'x': ['OO', 'XX', 'OO'],
    'y': ['OO', 'XO', 'OO'], 'z': ['OX', 'XO', 'OO'], '1': ['OX', 'XX', 'XX'], '2': ['OX', 'OX', 'XX'],
    '3': ['OO', 'XX', 'XX'], '4': ['OO', 'XO', 'XX'], '5': ['OX', 'XO', 'XX'], '6': ['OO', 'OX', 'XX'],
    '7': ['OO', 'OO', 'XX'], '8': ['OX', 'OO', 'XX'], '9': ['XO', 'OX', 'XX'], '0': ['XO', 'OO', 'XX'],
    '.': ['XX', 'OO', 'XO'], ',': ['XX', 'OX', 'XX'], '!': ['XX', 'OO', 'OX'], '?': ['XX', 'OX', 'OO'],
    ':': ['XX', 'OO', 'XX'], ';': ['XX', 'OX', 'OX'], '-': ['XX', 'XX', 'OO'], '(': ['XX', 'OO', 'OO'],
    ')': ['XX', 'OO', 'OO'], '<': ['OX', 'OX', 'XO'], '>': ['XO', 'XO', 'OX'], '/': ['XO', 'XX', 'OX'],
    "'": ['XX', 'XX', 'OX'], '*': ['XX', 'XO', 'OX'], '#': ['XO', 'XO', 'OO'], ' ': ['XX', 'XX', 'XX'],
    'Number': ['XO', 'XO', 'OO'], 'Letter': ['XX', 'XO', 'XO']
}

result = []

num_digit = 0
num_letter = 0

texts = list(input())

for char in texts:
    if char.isdigit():
        # 지금이 숫자
        num_letter = 0
        if num_digit == 0:
            # 숫자 처음 입력
            result.append('Number')
            num_digit = 1
    else:
        # 지금이 영어
        num_digit = 0
        if num_letter == 0:
            # 영어 처음 입력
            result.append('Letter')
            num_letter = 1

    result.append(char)

# 출력할 내용 'Letter h i Number 7 꼴'
print(result, '\n')

# 점자에서 O인 핀만 숫자로 보내주기
send = []
for item in result:
    for i in range(3):
        if braille[item][i][0] == 'O':
            send.append(i+1)
    for i in range(3):
        if braille[item][i][1] == 'O':
            send.append(i+4)

    # 구분을 위해 0 넣기
    send.append(0)

# 아두이노 연결
ardu = serial.Serial(PORT, 9600)
time.sleep(2)

for code in send:
    print(code)
    ardu.write(f"{code}\n".encode())
    time.sleep(0.01)

for item in result:
    for line in braille[item]:
        print(line)
    print()

ardu.close()