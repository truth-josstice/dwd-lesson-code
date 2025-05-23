import csv


def display_order():
    with open ('order.csv') as f:
        total = 0.0
        reader = csv.DictReader(f)
        for row in reader:
            line_total = float(row['unit_price']) * int(row['qty'])
            total += line_total
            print(f'{row['qty']}x {row['item']} @ ${float(row['unit_price']):.2f} = ${line_total:.2f}')
        print(f'\nTotal: ${total:.2f}')

        


def add_item():
    with open ('order.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['Chips', 6.50, 1])
        


if __name__ == '__main__':
    add_item()
    display_order()
