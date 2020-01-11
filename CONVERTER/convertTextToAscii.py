def CONVERT_TEXT_TO_ASCII(text):
    x = ''.join(str(ord(num)) for num in text).replace('0', '')
    if len(x) % 3 == 0:
        return x
    else:
        while len(x) % 3 > 0:
            x = x[:-1]
        return x