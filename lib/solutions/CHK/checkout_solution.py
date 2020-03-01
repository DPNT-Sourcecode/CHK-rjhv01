# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+
ALLOWED_ITEMS = ["A", "B", "C", "D", "E", "F"]


def XforY(skus_dict, item, X, Y):
    total = 0
    if item in skus_dict:
        matches = skus_dict[item] // X
        total = matches * Y
        skus_dict[item] = skus_dict[item] % X
    return total


def get_another_free(skus_dict, item, other_item, num_for_free=2):
    if other_item in skus_dict and item in skus_dict:
        skus_dict[other_item] -= skus_dict[item] // num_for_free

        if skus_dict[other_item] <= 0:
            del skus_dict[other_item]
    return skus_dict


def get_one_free(skus_dict, item, num_for_free=2):
    if item in skus_dict:
        if skus_dict[item] <= num_for_free:
            return skus_dict

        num_free = (skus_dict[item] // num_for_free)
        if skus_dict[item] % num_for_free == 0:
            num_free -= 1
        skus_dict[item] -= num_free
    return skus_dict


# items = {
#     'A':
# }

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = list(skus)

    # get number of items
    skus_dict = {}
    for sku in skus:
        if sku not in ALLOWED_ITEMS:
            return -1

        if sku in skus_dict:
            skus_dict[sku] += 1
        else:
            skus_dict[sku] = 1

    sum = 0

    skus_dict = get_another_free(skus_dict, "E", "B")
    sum += XforY(skus_dict, "A", 5, 200)
    sum += XforY(skus_dict, "A", 3, 130)
    sum += XforY(skus_dict, "B", 2, 45)
    skus_dict = get_one_free(skus_dict, "F")

    # handle rest of items
    for key in skus_dict:
        if key == "A":
            sum += skus_dict["A"] * 50
        if key == "B":
            sum += skus_dict["B"] * 30
        if key == "C":
            sum += skus_dict["C"] * 20
        if key == "D":
            sum += skus_dict["D"] * 15
        if key == "E":
            sum += skus_dict["E"] * 40
        if key == "F":
            sum += skus_dict["F"] * 10

    return sum






