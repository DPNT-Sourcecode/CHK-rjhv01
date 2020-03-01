# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

ALLOWED_ITEMS = ["A", "B", "C", "D"]

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
    if "E" in skus_dict:
        num_es = skus_dict["E"]
        if "B" in skus_dict :
            skus_dict["B"] -= skus_dict["E"] // 2

        if skus_dict["B"] <= 0:
            del skus_dict["B"]

    if "A" in skus_dict:
        sum += (skus_dict["A"] // 3) * 130
        sum += (skus_dict["A"] % 3) * 50
        del skus_dict["A"]
    if "B" in skus_dict:
        sum += (skus_dict["B"] // 2) * 45
        sum += (skus_dict["B"] % 2) * 30
        del skus_dict["B"]

    # handle rest
    for key in skus_dict:
        if key == "C":
            sum += skus_dict["C"] * 20
        if key == "D":
            sum += skus_dict["D"] * 15

    return sum



