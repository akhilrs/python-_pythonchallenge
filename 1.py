import string

puzzle_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl \
        zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq \
        pcamkkclbcb. lmu ynnjw ml rfc spj."

lower_string_arr = [ a for a in string.ascii_lowercase]

decoded_string = ''
for char in puzzle_string:
    if char in ["'", " ", ".", "(", ")"]:
        decoded_string += char
    else:
        char_index = lower_string_arr.index(char)
        if(char_index >= len(lower_string_arr) - 2):
            decoded_string += lower_string_arr[abs(len(lower_string_arr) - char_index -2 )]
        else:
            decoded_string += lower_string_arr[lower_string_arr.index(char) + 2]

print(decoded_string)
