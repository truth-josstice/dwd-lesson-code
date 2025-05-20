item_prices = {
    "coffee": {
        "costs": {
            "small": 3.00,
            "medium": 3.50,
            "large": 4.0,
            "soy": .5,
            "almond": .75,
            True: 1.0, 
            False: 0
        }
        
    },
    "tea": {
        "costs": {
            "regular": 2.5,
            "herbal": 2.75,
            "soy": .5,
            "almond": .75
        }
    },
    "croissant": 3.25,
    "muffin": 3.00,
    "misc": {
        "members": 0.10,
        "tax": 0.10
    }

}

def calculate_item_price(item_name, quantity, **options):
    match item_name:
        case 'coffee':
            subtotal = []
            for k, v in options.items():
                subtotal.append(item_prices["coffee"]["costs"].get(v))
            sub_q = (sum(subtotal)) * quantity
            return sub_q
        case 'tea':
            subtotal = []
            for k, v in options.items():
                subtotal.append(item_prices["tea"]["costs"].get(v))
            sub_q = (sum(subtotal)) * quantity
            return sub_q
        case 'croissant':
            subtotal = item_prices["croissant"] * quantity
            return subtotal
        case 'muffin':
            subtotal = item_prices["muffin"] * quantity
            return subtotal
        case _:
            print('Invalid menu item selected.')

def apply_discount_and_gst(subtotal, is_loyalty_member=False, loyalty_discount_rate=0.10, gst_rate=0.10):
    if is_loyalty_member == True:
        disc_sub = subtotal - (subtotal * loyalty_discount_rate)
        tax = disc_sub * gst_rate
        fin_total = disc_sub + tax
        return (disc_sub, tax, fin_total)
    else:
        tax = subtotal * gst_rate
        fin_total = subtotal + tax
        return (subtotal, tax, fin_total)
    
def generate_order_receipt(customer_name, order_items, is_loyalty_member=False):
    receipt_data = []
    
    current_subtotal = 0.0
    for i in order_items:
        item = calculate_item_price(i[0], i[1], **i[2])
        current_subtotal += item
        receipt_line = []
        for v in i[2].values():
            if v == True:
                v = 'w extra shot'
            elif v == False:
                v = ''
            receipt_line.append(v)
        if len(i[2])>=3:
            f_str = str.title(f'{i[1]} x {receipt_line[0]} {receipt_line[1]} {i[0]} {receipt_line[2]}: ${item:.2f}')
            receipt_data.append(f_str)
        elif len(i[2])>=1:    
            f_str = str.title(f'{i[1]} x {receipt_line[0]} {receipt_line[1]} {i[0]}: ${item:.2f}')
            receipt_data.append(f_str)
        else:
            f_str = str.title(f'{i[1]} x {i[0]}: ${item:.2f}')
            receipt_data.append(f_str)
    disc_tax = apply_discount_and_gst(current_subtotal, is_loyalty_member)
    if is_loyalty_member==True:
        receipt_str = str.title(f'-' * 9 + 'Your Receipt' + '-' * 9 + '\n' f'Customer Name: {customer_name}\n' + '\n'.join(receipt_data) + '\n' + '-' * 30 + '\n' + f'Subtotal: ${current_subtotal}' + '\n' + f'Loyalty Discount (10%): -${(current_subtotal)*0.1:.2f}' + '\n' + f'subtotal after discount: ${disc_tax[0]:.2f}' + '\n' + f'GST (10%): ${disc_tax[1]:.2f}' + '\n' + '-' * 30 + '\n' + (f'GRAND TOTAL: ${disc_tax[2]:.2f}') + '\n' + '=' * 30 + '\n')
    else:
        receipt_str = str.title(f'-' * 9 + 'Your Receipt' + '-' * 9 + '\n' f'Customer Name: {customer_name}\n' + '\n'.join(receipt_data) + '\n' + '-' * 30 + '\n' + f'Subtotal: ${current_subtotal:.2f}' + '\n' + f'GST (10%): ${disc_tax[1]:.2f}' + '\n' + '-' * 30 + '\n' + (f'GRAND TOTAL: ${disc_tax[2]:.2f}') + '\n' + '=' * 30 + '\n')
    print(receipt_str) 
    
order_1 = [
    ("coffee", 2, {"size": "small", "milk": "soy", "extra_shot": True}),
    ("coffee", 1, {"size": "medium", "milk": "soy", "extra_shot": False}),
    ("muffin", 4, {})
]
order_2 = [
    ("coffee", 3, {"size": "large", "milk": "almond", "extra_shot": True}),
    ("tea", 5, {"type": "regular", "milk": "soy"})
]
order_3 = [
    ("coffee", 2, {"size": "large", "extra_shot": True}),
    ("croissant", 5, {})
]
order_4 = [
    ("tea", 5, {"type": "herbal", "milk": "almond"})
]

generate_order_receipt('alex', order_1, is_loyalty_member=False)
generate_order_receipt('jim', order_2, is_loyalty_member=True)
generate_order_receipt('pete', order_3, True)
generate_order_receipt('ruddeger', order_4)


# apply_discount_and_gst(calculate_item_price('coffee', 5, size='small', milk='soy', extra_shot=True), True, 0.1, 0.1)
# calculate_item_price('coffee', 1, size='medium', milk='soy', extra_shot=False)
# calculate_item_price('coffee', 3, size='large', milk='almond', extra_shot=True)
# calculate_item_price('coffee', 2, size='large', extra_shot=True)
# apply_discount_and_gst(calculate_item_price('tea', 5, type='regular', milk='soy')) 
# calculate_item_price('tea', 5, type='herbal', milk='almond')
# apply_discount_and_gst(calculate_item_price('croissant', 5), True)
# calculate_item_price('muffin', 4)

# p_coffee = {"small": 3.00, "medium": 3.50, "large": 4.00}
# p_tea = {"regular": 2.50, "herbal": 2.75}
# p_pastry = {"croissant": 3.25, "muffin": 3.00}
# p_extras = {"soy milk": 0.50, "almond milk": 0.75, "extra shot": 1.00}
# p_misc = {"members": 0.90, "GST": 0.10}

# def coffee_price(size):
#     match size:
#         case 'small':
#             total_price = p_coffee["small"]
#             return total_price
#         case 'medium':
#             total_price = p_coffee["medium"]
#             return total_price
#         case 'large':
#             total_price = p_coffee["large"]
#             return total_price

# def coffee_extras(*args):
#     match args:
#         case ('soy', False):
#             extras_price = p_extras["soy milk"]
#             return extras_price
#         case ('almond', False):
#             extras_price = p_extras["almond milk"]
#             return extras_price
#         case ('soy', True):
#             extras_price = p_extras["soy milk"] + p_extras["extra shot"]
#             return extras_price
#         case ('almond', True):
#             extras_price = p_extras["almond milk"] + p_extras["extra shot"]
#             return extras_price
#         case (True, ):
#             return p_extras['extra shot']
#         case _:
#             return

# def tea_price(*args):
#     match args:
#         case ('regular', 'soy'):
        
#         case ('regular', 'almond'):
        
#         case ('herbal', )


# def calculate_item_price(item_name, quantity, **options):
#     if item_name == 'coffee':
#         if dict(options).__contains__('milk'):
#             total_price = (coffee_price(options['size']) + coffee_extras(options['milk'], options['extra_shot'])) * quantity
#             print(total_price)
        
#         elif not dict(options).__contains__('milk'):
#             total_price = (coffee_price(options['size']) + coffee_extras(options['extra_shot'])) * quantity 
#             print(total_price)
    
#     elif item_name == 'tea':
#         if dict(options).__contains__('milk'):
#             total_price = p_tea['regular'] * quantity
#             print(total_price)
    



# Abandoned code beneath here :D

# calculate_item_price('coffee', size='medium')
# calculate_item_price('coffee', size='large')

# def calculate_item_price(item_name, **options):
#     if item_name == 'coffee':
#         match options['size'] and options['extra_shot']:
#             case 'small' | True:
#                 total_price = p_coffee["small"] + p_extras["extra shot"]
#                 print(f'Small {item_name} with extra shot: ${total_price:.2f}')
#             case 'medium' | True:
#                 total_price = p_coffee["medium"] + p_extras["extra shot"]
#                 print(f'Small {item_name} with extra shot: ${total_price:.2f}')
#             case 'large' | True:
#                 total_price = p_coffee["large"] + p_extras["extra shot"]
#                 print(f'Small {item_name} with extra shot: ${total_price:.2f}')
            
        
        # match options:
        #     case {'size': 'small'}:
        #         total_price += p_coffee["small"]
        #         print(f'Small {item_name}: ${total_price:.2f}')
        #     case {'size': 'medium'}:
        #         total_price += p_coffee["medium"]
        #         print(f'Medium {item_name}: ${total_price:.2f}')
        #     case {'size': 'large'}:
        #         total_price += p_coffee['large']
        #         print(f'Large {item_name}: ${total_price:.2f}')
        #     case _:
        #         print('Invalid size selected')            