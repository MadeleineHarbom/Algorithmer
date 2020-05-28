
def test_D_2014(self):
    self.assertEqual(ncpc_functions.D_2014([1,4,1,4], [1,6,1,6]), "Emma")
    self.assertEqual(ncpc_functions.D_2014([1,8,1,8], [1,10,2,5]), "Tie")
    self.assertEqual(ncpc_functions.D_2014([2,5,2,7], [1,5,2,5]), "Gunnar")