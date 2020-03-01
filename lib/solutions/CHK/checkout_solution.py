item_price = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}


def group_discount(num_items, grouped_items, num, amount):
    total = 0

    excess_group_items = {}
    for k in grouped_items:
        if k in num_items and num_items[k] > 0:
            excess_group_items[k] = num_items[k]

    # order by most expensive excess_group_items
    ks = sorted(excess_group_items.keys(), key=item_price.get, reverse=True)

    carry_group_items = {}
    carry_cnt = 0
    for key in ks:
        cnt = excess_group_items[key]

        if key in carry_group_items:
            carry_group_items[key] += cnt
        else:
            carry_group_items[key] = cnt

        if cnt + carry_cnt >= num:
            total += amount

            # delete the carried items
            for key2 in carry_group_items:
                num_items[key2] -= carry_group_items[key2]

            carry_group_items = {
                key: (cnt + carry_cnt) - num
            }
            carry_cnt = (cnt + carry_cnt) - num
        else:
            # carry the items over
            carry_cnt += cnt
    return total


# costs Y when you buy X of item
def XforY(num_items, item, X, Y):
    total = 0
    if item in num_items:
        total = (num_items[item] // X) * Y
        num_items[item] = num_items[item] % X
    return total


# get other_item free when you buy num_for_free of item
def get_another_free(num_items, item, other_item, num_for_free=2):
    if other_item in num_items and item in num_items:
        num_items[other_item] -= num_items[item] // num_for_free

        if num_items[other_item] <= 0:
            num_items[other_item] = 0


# buy num_for_free of item and get 1 free
def get_one_free(num_items, item, num_for_free=2):
    if item in num_items:
        if num_items[item] <= num_for_free:
            return

        num_free = (num_items[item] // num_for_free)
        if num_items[item] % num_for_free == 0:
            num_free -= 1
        num_items[item] -= num_free


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = list(skus)

    # get number of items
    num_items = {}
    for sku in skus:
        if sku not in item_price.keys():
            return -1

        if sku in num_items:
            num_items[sku] += 1
        else:
            num_items[sku] = 1

    sum = 0

    # apply Special offers
    get_another_free(num_items, "E", "B")
    get_another_free(num_items, "N", "M", 3)
    get_another_free(num_items, "R", "Q", 3)
    get_one_free(num_items, "F")
    get_one_free(num_items, "U", 3)

    sum += XforY(num_items, "A", 5, 200)
    sum += XforY(num_items, "A", 3, 130)
    sum += XforY(num_items, "B", 2, 45)
    sum += XforY(num_items, "K", 2, 120)
    sum += XforY(num_items, "H", 10, 80)
    sum += XforY(num_items, "H", 5, 45)
    sum += XforY(num_items, "P", 5, 200)
    sum += XforY(num_items, "Q", 3, 80)
    sum += XforY(num_items, "V", 3, 130)
    sum += XforY(num_items, "V", 2, 90)

    sum += group_discount(num_items, ["S", "T", "X", "Y", "Z"], 3, 45)
    sum += XforY(num_items, "S", 3, 45)
    sum += XforY(num_items, "T", 3, 45)
    sum += XforY(num_items, "X", 3, 45)
    sum += XforY(num_items, "Y", 3, 45)
    sum += XforY(num_items, "Z", 3, 45)

    # handle rest of items
    for key in num_items:
        sum += num_items[key] * item_price[key]

    return sum




