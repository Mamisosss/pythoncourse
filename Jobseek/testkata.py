def solution():
    user_string = input("")
    n = int(len(user_string))
    list_char = []

    if n == 0:
        print(list_char)
    elif n % 2 == 0 and not n == 0:
        j = int(n/2)
        for i in range(j):
            list_char.append(user_string[2*i] + user_string[2*i+1])
        print(list_char)
    else:
        j = int((n-1)/2)
        for i in range(j):
            list_char.append(user_string[2*i] + user_string[2*i+1])
        list_char.append(user_string[n-1] + "_")
        print(list_char)
    pass
solution()