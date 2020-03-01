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

    def test_invalid2(self):
        assert checkout_solution.checkout("E") == -1

    def test_invalid3(self):
        assert checkout_solution.checkout("") == -1

    def test_BAAAB(self):
        assert checkout_solution.checkout("BAAA") == 160

    def test_A(self):
        assert checkout_solution.checkout("A") == 50

    def test_AxA(self):
        assert checkout_solution.checkout("AxA") == -1

    def test_a(self):
        assert checkout_solution.checkout("a") == -1

