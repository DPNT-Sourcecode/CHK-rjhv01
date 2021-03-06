from solutions.CHK import checkout_solution

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

    def test_2F(self):
        assert checkout_solution.checkout("F" * 2) == 20

    def test_3F(self):
        assert checkout_solution.checkout("F" * 3) == 20

    def test_4F(self):
        assert checkout_solution.checkout("F" * 4) == 30

    def test_5F(self):
        assert checkout_solution.checkout("F" * 5) == 30

    def test_4K(self):
        assert checkout_solution.checkout("K" * 4) == 240

    def test_3K(self):
        assert checkout_solution.checkout("K" * 3) == 190

    def test_6F(self):
        assert checkout_solution.checkout("F" * 6) == 40

    def test_3RQ(self):
        assert checkout_solution.checkout("RRRQ") == 150

    def test_4RQ(self):
        assert checkout_solution.checkout("RRRRQ") == 200

    def test_6R2Q(self):
        assert checkout_solution.checkout("R" * 6 + "Q" * 2) == 300

    def test_6R3Q(self):
        assert checkout_solution.checkout("R" * 6 + "Q" * 3) == 330

    def test_4U(self):
        assert checkout_solution.checkout("U" * 4) == 120

    def test_5U(self):
        assert checkout_solution.checkout("U" * 5) == 160

    def test_STY(self):
        assert checkout_solution.checkout("STY") == 45

    def test_4STY(self):
        assert checkout_solution.checkout("S"*4+"TY") == 90

    def test_SSSZ(self):
        assert checkout_solution.checkout("SSSZ") == 65

    def test_STXSTX(self):
        assert checkout_solution.checkout("STXSTX") == 90

    def test_STXZ(self):
        assert checkout_solution.checkout("STXZ") == 62

    def test_3Y(self):
        assert checkout_solution.checkout("Y"*3) == 45

    def test_4Y(self):
        assert checkout_solution.checkout("Y"*4) == 65
