import csv

# Result
EvilMan = 'DLX26mmbPunP15JjTUbqj2M5ZPASmQ5lqi'
target_addr = 'D8t5PGChNNidpcEwvoGTqFnEymqKeu3cSb'
value_on_target = 1736746.5599999996


def find_possible_targets(file_path, target_addr, value_on_target):
    amounts = {}
    childs = [target_addr]
    with open(file_path) as f:
        file = csv.reader(f)

        for line in file:
            from_addr, to_addr, value, *_, fee, _ = line[0].split(";")
            value, fee = float(value), float(fee)
            
            if to_addr in childs:
                childs.append(from_addr)
                amounts[to_addr] = amounts.get(to_addr, 0) - value
                amounts[from_addr] = amounts.get(from_addr, 0) + value
                
    return [addr for addr, amount in amounts.items() if amount >= value_on_target]

print(find_possible_targets("output.csv", target_addr, value_on_target))
