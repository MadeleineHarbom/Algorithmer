

def test_G_2014(self):
    self.assertEqual(ncpc_functions.G_2014(4, 4, [1, 2, 3, 4]), 4)
    self.assertEqual(ncpc_functions.G_2014(12, 3, [2, 3, 4, 5, 6, 7, 4, 7, 8, 8, 12, 12]), 2)
    self.assertEqual(ncpc_functions.G_2014(5, 4, [2, 3, 1, 5, 4]), 3)