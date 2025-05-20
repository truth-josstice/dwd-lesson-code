# Now refactor your solutions so they use lambdas and callbacks  Also, see if you can process a single input like “28C” or “78F” 

c_to_f = lambda x: x * (9/5) + 32
f_to_c = lambda x: (x - 32) * (5/9)

def conversion_func(temperature, scale, callback_fn):
    """will process data from input and return the printed conversion"""
    output_scale = "F" if scale == "C" else "C"
    print(f'Original temperature: {temperature:.2f}°{scale}.' + '\n' + f'Converted temperature: {callback_fn(temperature):.2f}°{output_scale}')

while True:
    user_input = str(input("Enter a temperature to convert (eg 28C or 80F): "))
    temp = int(str(user_input[:-1]))
    scale = (user_input[-1])
    
    match scale:
        case "F":
            conversion_func(temp, scale, f_to_c)
        case "C":
            conversion_func(temp, scale, c_to_f)
        case _:
            print('Invalid temperature scale entered, please enter temperature ending in "C" of "F".')




# def celsius_to_fahrenheit(celsius):
#     return celsius * (9/5) + 32

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * (5/9)

# initial = float(input("Enter a temperature: "))
# init_scale = input("Please enter which scale you would like to convert to (C or F): ")

# match init_scale:
#     case "F":
#         converted_cf = celsius_to_fahrenheit(initial)
#         print(f'Original temperature: {initial:.2f}\u00B0C.\nConverted Temperature: {converted_cf:.2f}\u00B0F')
#         break
#     case "C":
#         converted_fc = fahrenheit_to_celsius(initial)
#         print(f'Original temperature: {initial:.2f}\u00B0F.\nConverted Temperature: {converted_fc:.2f}\u00B0C')
#         break
#     case _:
#         print('Invalid temperature scale, please try again.')
    





    
    
    