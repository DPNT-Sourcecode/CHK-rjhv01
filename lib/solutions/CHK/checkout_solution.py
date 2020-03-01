# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# +------+-------+------------------------+

ALLOWED_ITEMS = ["A", "B", "C", "D", "E", "F"]

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
        total_f = skus_dict["F"]
        for i in range(total_f):
            if i % 2 == 0:
                total_f -= 1
        skus_dict["F"] = total_f

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



