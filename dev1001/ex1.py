def bye_bye_three_and_five(max):
    list = []
    for i in range(max + 1):
        if (i % 3) and (i % 5) and (i != 0):
            list.append(i)
    print(list)
    return(list)

bye_bye_three_and_five(16)
bye_bye_three_and_five(89)
bye_bye_three_and_five(339)