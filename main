import purchase_analyzer

def main():
    purchases = purchase_analyzer.read_purchases('purchases.txt')
    err_count = purchase_analyzer.count_errors('purchases.txt')
    purchase_analyzer.write_report(purchases, err_count, 'report.txt')
    print(f"Отчёт сохранён в файл: report.txt")

if __name__ == '__main__':
    main()
