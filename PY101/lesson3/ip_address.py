def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    str_length = len(dot_separated_words)
    if str_length == 4:
        while str_length > 0:
            word = dot_separated_words.pop()
            str_length -= 1
            if not is_an_ip_number(word):
                break

        return True
    return False

print(is_dot_separated_ip_address("10.4..3"))