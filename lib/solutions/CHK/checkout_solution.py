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


def get_one_free(item_count, num_for_free=2):
    num_free = (item_count // num_for_free)
    if item_count % num_for_free == 0:
        num_free -= 1
    return item_count - num_free

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

    # handle special offers
    # assuming that "2E get one B" free takes precedence to "2B for 45"
    if "E" in skus_dict:
        # 2E get one B
        if "B" in skus_dict:
            skus_dict["B"] -= skus_dict["E"] // 2

            if skus_dict["B"] <= 0:
                del skus_dict["B"]

    if "A" in skus_dict:
        # 3A for 130, 5A for 200
        while skus_dict["A"] >= 5:
            skus_dict["A"] -= 5
            sum += 200
        sum += (skus_dict["A"] // 3) * 130
        sum += (skus_dict["A"] % 3) * 50
        del skus_dict["A"]

    if "B" in skus_dict:
        # 2B for 45
        sum += (skus_dict["B"] // 2) * 45
        sum += (skus_dict["B"] % 2) * 30
        del skus_dict["B"]

    if "F" in skus_dict and skus_dict["F"] > 2:
        # 2F get one F free
        skus_dict["F"] = get_one_free(skus_dict["F"])

    # handle rest of items
    for key in skus_dict:
        if key == "C":
            sum += skus_dict["C"] * 20
        if key == "D":
            sum += skus_dict["D"] * 15
        if key == "E":
            sum += skus_dict["E"] * 40
        if key == "F":
            sum += skus_dict["F"] * 10

    return sum






