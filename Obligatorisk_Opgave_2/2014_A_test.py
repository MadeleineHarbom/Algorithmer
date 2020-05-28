def test_A_2014(self):
    self.assertEqual(ncpc_functions.A_2014(4, 4, [[1, 2, 2],[2, 3, 1],[3, 4, 1],[4, 1, 2]]), 3)
    self.assertEqual(ncpc_functions.A_2014(5, 5, [[1, 2, 1],[2, 3, 1],[2, 4, 1],[2, 5, 1],[4, 5, 1]]), "impossible")
    self.assertEqual(ncpc_functions.A_2014(4, 5, [[1, 2, 1],[2, 3, 0],[2, 4, 1],[3, 1, 1],[3,4,1]]), 2)