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


def group_discount(items_cnt, grouped_items, num, amount):
    grouped_discount_items = ""

    # order by most expensive excess_group_items
    for key in sorted(items_cnt.keys(), key=item_price.get, reverse=True):
        if key in grouped_items:
            grouped_discount_items += key * items_cnt[key]
            # remove from items_cnt
            items_cnt[key] = 0

    excess_items = len(grouped_discount_items) % num
    if excess_items != 0:
        # add excess items back to items_cnt
        items_left = grouped_discount_items[-excess_items:]
        for item in items_left:
            items_cnt[item] += 1

    return (len(grouped_discount_items) // num) * amount


# costs Y when you buy X of item
def XforY(items_cnt, item, X, Y):
    total = 0
    if item in items_cnt:
        total = (items_cnt[item] // X) * Y
        items_cnt[item] = items_cnt[item] % X
    return total


# get other_item free when you buy num_for_free of item
def get_another_free(items_cnt, item, other_item, num_for_free=2):
    if other_item in items_cnt and item in items_cnt:
        items_cnt[other_item] -= items_cnt[item] // num_for_free

        if items_cnt[other_item] <= 0:
            items_cnt[other_item] = 0


# buy num_for_free of item and get 1 free
def get_one_free(items_cnt, item, num_for_free=2):
    if item in items_cnt:
        if items_cnt[item] <= num_for_free:
            return

        num_free = (items_cnt[item] // num_for_free)
        if items_cnt[item] % num_for_free == 0:
            num_free -= 1
        items_cnt[item] -= num_free


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = list(skus)

    # get number of items
    items_cnt = {}
    for sku in skus:
        if sku not in item_price.keys():
            return -1

        if sku in items_cnt:
            items_cnt[sku] += 1
        else:
            items_cnt[sku] = 1

    sum = 0

    # apply Special offers
    get_another_free(items_cnt, "E", "B")
    get_another_free(items_cnt, "N", "M", 3)
    get_another_free(items_cnt, "R", "Q", 3)
    get_one_free(items_cnt, "F")
    get_one_free(items_cnt, "U", 3)
    sum += XforY(items_cnt, "A", 5, 200)
    sum += XforY(items_cnt, "A", 3, 130)
    sum += XforY(items_cnt, "B", 2, 45)
    sum += XforY(items_cnt, "K", 2, 120)
    sum += XforY(items_cnt, "H", 10, 80)
    sum += XforY(items_cnt, "H", 5, 45)
    sum += XforY(items_cnt, "P", 5, 200)
    sum += XforY(items_cnt, "Q", 3, 80)
    sum += XforY(items_cnt, "V", 3, 130)
    sum += XforY(items_cnt, "V", 2, 90)
    sum += group_discount(items_cnt, ["S", "T", "X", "Y", "Z"], 3, 45)
    sum += XforY(items_cnt, "S", 3, 45)
    sum += XforY(items_cnt, "T", 3, 45)
    sum += XforY(items_cnt, "X", 3, 45)
    sum += XforY(items_cnt, "Y", 3, 45)
    sum += XforY(items_cnt, "Z", 3, 45)

    # handle normal items
    for key in items_cnt:
        sum += items_cnt[key] * item_price[key]

    return sum


