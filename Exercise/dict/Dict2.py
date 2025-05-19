import statistics

stocks = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}
def printAll():
    for stock, price in stocks.items():
        avg = statistics.mean(price)
        print(f"{stock} ==> {price} ==> avg: ", round(avg, 2))


def add():
    stock = input("Enter a stock ticker to add:")
    price = float(input("Enter price of this stock:"))
    if stock in stocks:
        stocks[stock].append(price)
    else:
        stocks[stock] = [price]
    printAll()


def main():
    operation = input("Enter operation (print, add or amend):")
    if operation.lower() == 'print':
        printAll()
    elif operation.lower() == 'add':
        add()
    else:
        print("Unsupported operation:",operation)

if __name__ == '__main__':
    main()
