import unittest
#write import statements for required classes or functions
import HourlyEmployee from Employee
import SalariedEmployee from Employee
import check_come_out_roll from Player
import non_contiguous_motif from Motif
class TestFinalExam(unittest.TestCase):

    #3 points
    #Create a test case to test the non_contiguous_motif  function with values
    #['A', 'C','G','T','A','C','G','T','G','A','C','G'] that returns three values 3, 8, and 10
    def test_non_contiguous_motif_w_value_3_8_10(self):
         self.assertEqual((['A','C','G','T','A','C','G','T','G','A','C','G']),non_contiguous_motif(3,8,10))
    

    
    #3 points
    #For the Player class create a test case, to test the check_come_out_roll
    #with argument values True, 8, and 9 the result should be 'Invalid range'
    def test_check_come_out_role_w_value_Invalid_range(self):
         self.assertEqual((8,9),check_come_out_roll('Invalid range'))
    

    
    #3 points
    #For the Player class create a test case, to test the check_come_out_roll
    #with argument values False, 4 and 7 should return 'Loser'
    def test_check_come_out_role_w_value_Loser(self):
         self.assertEqual((4,7),check_come_out_roll('Loser'))
    
    #3 points
    #Add a test case for HourlyEmployee that calls the calculate method with values 10 and 80 to yield a result of 800.
     def test_hourly_employee_w_value_800(self):
         self.assertEqual((10,80),HourlyEmployee(800))

    #3 points
    #Add a test case for SalariedEmployee that calls the calculate method with values 260000 to yield a result of 10000.
     def test_hourly_employee_w_value_10000(self):
         self.assertEqual(260000, HourlyEmployee(10000))


    

    

unittest.main(verbosity=2)
        
