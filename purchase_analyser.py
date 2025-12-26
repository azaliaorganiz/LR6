def read_purchases(path):
    result = []
    with open(path, 'r') as file:
        lines = [i.strip() for i in file.readlines()]
        for row in lines:
            line = row.split(';')
            if len(line) == 5:
                line = [v.strip() for v in line]
                if '' in line:
                    continue
                try:
                    price = float(line[3])
                    qty = float(line[4])
                    if price >= 0 and qty > 0:
                        result.append({
                            'date': line[0],
                            'category': line[1],
                            'name': line[2],
                            'price': price,
                            'qty': qty
                        })
                except:
                    continue
    return result


def count_errors(path):
    error_count = 0
    with open(path, 'r') as file:
        lines = [i.strip() for i in file.readlines()]
        for row in lines:
            if not row:
                error_count += 1
                continue

            line = row.split(';')
            if len(line) != 5:
                error_count += 1
                continue

            line = [v.strip() for v in line]
            if '' in line:
                error_count += 1
                continue

            try:
                price = float(line[3])
                qty = float(line[4])
                if price < 0 or qty <= 0:
                    error_count += 1
            except:
                error_count += 1
    return error_count
def total_spent(purchases):
    total = 0
    for dct in purchases:
        total += dct['price'] * dct['qty']
    return total

def spent_by_category(purchases):
    total = {}
    for dct in purchases:
        category = dct['category']
        cost = dct['price']*dct['qty']
        total[category] = total.get(category, 0) + cost
    return total

def top_n_expensive(purchases, n = 3):
    sorted_dct = sorted(purchases, key = lambda x: x['price'] * x['qty'], reverse = True)
    return sorted_dct[:n]

def write_report(purchases, errors, out_path):
    lines = []
    lines.append(f"Количество валидных строк: {len(purchases)}\n")
    lines.append(f"Количество ошибочных строк: {errors}\n")
    lines.append(f"Общая сумма: {total_spent(purchases)}\n")
    lines.append("Сумма по категориям:\n")
    for key, value in spent_by_category(purchases).items():
        lines.append(f"{key}: {value}\n")
    lines.append(f"Топ-3 покупок:\n")
    for dct in top_n_expensive(purchases):
        lines.append(f"{dct['name']}: {dct['price'] * dct['qty']}\n")
    with open(out_path, 'w') as f:
        f.writelines(lines)
