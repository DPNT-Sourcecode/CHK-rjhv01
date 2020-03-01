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


def group_discount(skus_dict, grouped_items, num, amount):
    total = 0

    excess_group_items = {}
    for k in grouped_items:
        if k in skus_dict and skus_dict[k] > 0:
            excess_group_items[k] = skus_dict[k] % num

    # order by most expensive excess_group_items
    excess_group_items = sorted(excess_group_items, key=item_price[excess_group_items.get].get, reverse=True)

    carry_group_items = {}
    carry_cnt = 0
    for key in excess_group_items:
        cnt = excess_group_items[key]
        if key in carry_group_items:
            carry_group_items[key] += cnt
        else:
            carry_group_items[key] = cnt

        if cnt + carry_cnt >= num:
            total += amount
            # delete the carried items
            for key2 in carry_group_items:
                cnt2 = carry_group_items[key2]
                skus_dict[key2] -= cnt2

            carry_group_items = {
                key: (cnt + carry_cnt) - num
            }
            carry_cnt = (cnt + carry_cnt) - num
        else:
            # carry the items over
            carry_cnt += cnt
    return total


# costs Y when you buy X of item
def XforY(skus_dict, item, X, Y):
    total = 0
    if item in skus_dict:
        total = (skus_dict[item] // X) * Y
        skus_dict[item] = skus_dict[item] % X
    return total


# get other_item free when you buy num_for_free of item
def get_another_free(skus_dict, item, other_item, num_for_free=2):
    if other_item in skus_dict and item in skus_dict:
        skus_dict[other_item] -= skus_dict[item] // num_for_free

        if skus_dict[other_item] <= 0:
            del skus_dict[other_item]
    return skus_dict


# buy num_for_free of item and get 1 free
def get_one_free(skus_dict, item, num_for_free=2):
    if item in skus_dict:
        if skus_dict[item] <= num_for_free:
            return skus_dict

        num_free = (skus_dict[item] // num_for_free)
        if skus_dict[item] % num_for_free == 0:
            num_free -= 1
        skus_dict[item] -= num_free
    return skus_dict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = list(skus)

    # get number of items
    skus_dict = {}
    for sku in skus:
        if sku not in item_price.keys():
            return -1

        if sku in skus_dict:
            skus_dict[sku] += 1
        else:
            skus_dict[sku] = 1

    sum = 0

    # apply Special offers
    skus_dict = get_another_free(skus_dict, "E", "B")
    skus_dict = get_another_free(skus_dict, "N", "M", 3)
    skus_dict = get_another_free(skus_dict, "R", "Q", 3)
    skus_dict = get_one_free(skus_dict, "F")
    skus_dict = get_one_free(skus_dict, "U", 3)
    sum += XforY(skus_dict, "A", 5, 200)
    sum += XforY(skus_dict, "A", 3, 130)
    sum += XforY(skus_dict, "B", 2, 45)
    sum += XforY(skus_dict, "K", 2, 120)
    sum += XforY(skus_dict, "H", 10, 80)
    sum += XforY(skus_dict, "H", 5, 45)
    sum += XforY(skus_dict, "P", 5, 200)
    sum += XforY(skus_dict, "Q", 3, 80)
    sum += XforY(skus_dict, "V", 3, 130)
    sum += XforY(skus_dict, "V", 2, 90)

    sum += XforY(skus_dict, "S", 3, 45)
    sum += XforY(skus_dict, "T", 3, 45)
    sum += XforY(skus_dict, "X", 3, 45)
    sum += XforY(skus_dict, "Y", 3, 45)
    sum += XforY(skus_dict, "Z", 3, 45)
    sum += group_discount(skus_dict, ["S","T","X","Y","Z"], 3, 45)

    # handle rest of items
    for key in skus_dict:
        sum += skus_dict[key] * item_price[key]

    return sum





