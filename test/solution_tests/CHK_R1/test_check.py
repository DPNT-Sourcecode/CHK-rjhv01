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

    def test_2F(self):
        assert checkout_solution.checkout("F" * 2) == 20

    def test_3F(self):
        assert checkout_solution.checkout("F" * 3) == 20

    def test_4F(self):
        assert checkout_solution.checkout("F" * 4) == 30

    def test_5F(self):
        assert checkout_solution.checkout("F" * 5) == 30

    def test_4F(self):
        assert checkout_solution.checkout("F" * 4) == 30

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

    # | Item | Price | Special offers                  |
    # +------+-------+---------------------------------+
    # | A    | 50    | 3A for 130, 5A for 200          |
    # | B    | 30    | 2B for 45                       |
    # | C    | 20    |                                 |
    # | D    | 15    |                                 |
    # | E    | 40    | 2E get one B free               |
    # | F    | 10    | 2F get one F free               |
    # | G    | 20    |                                 |
    # | H    | 10    | 5H for 45, 10H for 80           |
    # | I    | 35    |                                 |
    # | J    | 60    |                                 |
    # | K    | 70    | 2K for 120                      |
    # | L    | 90    |                                 |
    # | M    | 15    |                                 |
    # | N    | 40    | 3N get one M free               |
    # | O    | 10    |                                 |
    # | P    | 50    | 5P for 200                      |
    # | Q    | 30    | 3Q for 80                       |
    # | R    | 50    | 3R get one Q free               |
    # | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | U    | 40    | 3U get one U free               |
    # | V    | 50    | 2V for 90, 3V for 130           |
    # | W    | 20    |                                 |
    # | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # +------+-------+---------------------------------+

    def test_STY(self):
        assert checkout_solution.checkout("STY") == 45

    def test_3Y(self):
        assert checkout_solution.checkout("Y"*3) == 45

    def test_4Y(self):
        assert checkout_solution.checkout("Y"*4) == 65

    def test_get_another_free(self):
        pass

    def test_get_one_free(self):
        pass
