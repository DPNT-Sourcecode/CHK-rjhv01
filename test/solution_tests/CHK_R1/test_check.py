from solutions.CHK import checkout_solution


# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

class TestSum():
    def test_AAA(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_BB(self):
        assert checkout_solution.checkout("BB") == 45

    def test_BAABA(self):
        assert checkout_solution.checkout("BAABA") == 175

    def test_invalid1(self):
        assert checkout_solution.checkout("-") == -1

    # def test_invalid2(self):
    #     assert checkout_solution.checkout("E") == -1

    def test_invalid3(self):
        assert checkout_solution.checkout("") == 0

    def test_BAAAB(self):
        assert checkout_solution.checkout("BAAA") == 160

    def test_A(self):
        assert checkout_solution.checkout("A") == 50

    def test_AxA(self):
        assert checkout_solution.checkout("AxA") == -1

    def test_a(self):
        assert checkout_solution.checkout("a") == -1

    # +------+-------+------------------------+
    # | Item | Price | Special offers         |
    # +------+-------+------------------------+
    # | A    | 50    | 3A for 130, 5A for 200 |
    # | B    | 30    | 2B for 45              |
    # | C    | 20    |                        |
    # | D    | 15    |                        |
    # | E    | 40    | 2E get one B free      |
    # +------+-------+------------------------+

    def test_5A(self):
        assert checkout_solution.checkout("A" * 5) == 200

    def test_6A(self):
        assert checkout_solution.checkout("A" * 6) == 250

    def test_11A(self):
        assert checkout_solution.checkout("A" * 11) == 450

    def test_BEE(self):
        assert checkout_solution.checkout("BEE") == 80

    def test_E(self):
        assert checkout_solution.checkout("E") == 40

    def test_4E2B(self):
        assert checkout_solution.checkout("EEBEEB") == 160


