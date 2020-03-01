
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

ALLOWED_ITEMS = ["A", "B", "C", "D"]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = sorted(skus)
    skus_dict = {}
    for sku in skus:
        if sku not in ALLOWED_ITEMS:
            return -1
        if sku in skus_dict:
            skus_dict[sku] += 1
        else:
            skus_dict = 1


