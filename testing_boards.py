from main import *

# # TEST 1 - START POSITION
# c = Chess('rnbq1bnr/pppkpppp/8/2p2p1R/4P3/5N2/PPPP1PPP/RNBQKB1R w KQ - 2 3')
# c.show_board()
# c.show_moves()

# # TEST 2 - ONE KING POSITION
# c = Chess('8/8/8/3ppp3/3pKp3/3ppp3/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 3 -  TWO KINS POSITION
# c = Chess('8/3PPP2/3PkP2/3PPP2/8/3ppp2/3pKp2/3ppp2 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 4 - ONE ROOK POSITION
# c = Chess('8/8/8/8/8/8/8/7R w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 5 - ONE ROOK POSITION
# c = Chess('8/8/8/8/8/7p/8/5P1R w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 6 - SEVERAL ROOKS POSITION
# c = Chess('r6R/8/8/8/8/8/8/r6R w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 7 - ONE BISHOP POSITION
# c = Chess('8/8/8/8/4B3/8/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 8 - ONE QUEEN POSITION
# c = Chess('8/8/8/8/4Q3/8/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 9 - ONE KNIGHT POSITION
# c = Chess('8/8/8/8/4N3/8/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 10 - ONE KNIGHT POSITION
# c = Chess('8/8/8/8/7N/8/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()


# # TEST 11 - SEVERAL PAWNS POSITION
# c = Chess('8/4p3/4p3/8/8/4P3/4P3/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 12 - SEVERAL PAWNS POSITION
# c = Chess('8/8/8/8/8/3p1p2/4P3/8 w - - 0 1')
# c.show_board()
# c.show_moves()


# # TEST 13 - Move in two cells for white pawn
# c = Chess('8/8/8/4Pp2/8/8/8/K7 w KQkq f6 0 3')
# c.show_board()
# print(c.move_in_two_cells)
# c.show_moves()


# # TEST 14 - Move in two cells for black pawn
# c = Chess('8/8/8/8/2Pp4/8/8/8 b KQkq c3 0 3')
# c.show_board()
# print(c.move_in_two_cells)
# c.show_moves()
#
# # Test 15 - Kings attack after rook move
# c = Chess('1k2r3/8/8/8/8/8/4R3/4K3 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 15 - Kings attack after rook move 2
# c = Chess('3r4/3r4/8/8/3R4/8/3K4/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 16 - Kings attack after bishop move 1
# c = Chess('4q3/8/8/8/4B3/4K3/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 17 - Kings attack after bishop move 2
# c = Chess('8/q7/8/8/3B4/4K3/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 18 - Kings attack after bishop move 3
# c = Chess('8/b7/1q6/8/3B4/4K3/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 19 - Kings attack after queen move 1
# c = Chess('3q4/3q4/8/8/3Q4/8/3K4/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 20 - Kings attack after queen move 1
# c = Chess('8/8/7b/2q5/8/4Q3/3K4/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 21 - Special test to check attack to king
# c = Chess('8/8/8/3Q4/5n2/4R3/r3K3/B5N1 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 22 - Special test to check attack to king
# c = Chess('8/8/8/3Q4/6n1/4R3/r3K3/B5N1 w - - 0 1')
# c.show_board()
# c.show_moves()


# # Test 23 - Special test to check attack to king
# c = Chess('8/8/8/3Q4/4qn2/4R3/r3K3/Br4N1 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 24 - Special test to check attack to king
# c = Chess('8/8/8/b4Q2/4qn1b/4R3/rB2K3/1r4N1 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 24 - Special test to check attack to king
# c = Chess('8/8/8/b4Q2/4qn1b/4R3/rB2K2r/1r4N1 w - - 0 1')
# c.show_board()
# c.show_moves()

# # Test 25 - Special test to check attack to king
# c = Chess('n7/8/8/b4Q2/4q2b/4R3/rB2Kqr1/1r4N1 w - - 0 1')
# c.show_board()
# c.show_moves()


# # Test 26 - Special test to check attack to king with pawns
# c = Chess('8/8/q7/8/8/3P4/4K3/8 w - - 0 1')
# c.show_board()
# c.show_moves()
#
# # Test 27 - Special test to check attack to king with pawns
# c = Chess('8/8/8/8/8/8/r2PK3/8 w - - 0 1')
# c.show_board()
# c.show_moves()
#
# # Test 28 - Special test to check attack to king with pawns
# c = Chess('8/8/8/1q6/4b3/3P4/4K3/8 w - - 0 1')
# c.show_board()
# c.show_moves()
#
# # Test 29 - Special test to check attack to king with pawns
# c = Chess('8/8/8/8/1q6/4b3/3P4/4K3 w - - 0 1')
# c.show_board()
# c.show_moves()

# # # Test 30 - Two cells move.
# c = Chess('k3r3/8/8/3pP3/8/8/4K3/8 w - - 0 3')
# c.show_board()
# c.show_moves()
# #
#
# # # Test 31 - Two cells move.
# c = Chess('k4r2/8/8/3pP3/8/8/4K3/8 w - d6 0 3')
# c.show_board()
# c.show_moves()


# # # Test 32 - Two cells move.
# c = Chess('8/8/8/8/5p2/4K3/2R5/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # # Test 33 - Kings castling.
c = Chess('8/8/8/5r2/8/8/8/4K2R w KAha - 0 1')
c.show_board()
c.show_moves()


# Clasical position
# c = Chess('rnbq1bnr/pppkpppp/8/2p2p1R/4P3/5N2/PPPP1PPP/RNBQKB1R w KQ - 2 3')
# c.show_board()
# c.show_moves()

# @check_time
# def test_time():
#     for _ in range(10_000):
#         c = Chess('rnbq1bnr/pppkpppp/8/2p2p1R/4P3/5N2/PPPP1PPP/RNBQKB1R w KQ - 2 3')
#
#
# test_time()
