'''
Created on Mar 2, 2013

@author: sushantw
'''
import unittest 
import review

'''To Yelp Employees:
        If you want to check any test case, please make sure to add \" and \', escape characters for any quotation symbols within the string '''
    
 
# The following is the class in which all functions will be ran by unittest
class ReviewTest(unittest.TestCase):
    ''' Main class for add testing; Can be added to a suite'''
 
# The function "setUp" will always be ran in order to setup the
# test environment before all the tests have run.
    def setUp(self):
        '''Verify environment is setup properly''' # Printed if test fails
        pass
 
# The function "tearDown" will always be ran in order to cleanup the
# test environment after all the tests have run.
    def tearDown(self):
        '''Verify environment is tore down properly''' # Printed if test fails
        pass
 
# Functions beginning with "test" will be ran as a unit test.
    def test_case1(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc(" There are different biryanis all over bay area. This place has a pretty good chicken biryani. May be the other reviewers mentioned about the mutton biryani which is not on par with chicken biryani. Also I have tried the Vijyawada chicken biryani. Its a different flavor and awesome taste. Its made to order and it has an excellent flavor to it. The buffet here is a real cheap but very good tasting food. They have this surprise south indian dishes such as kolambu, sambar, rasam, vada, pagoda, bisibeda bath etc.. that is excellent. The south india parotta I had in this place is the best parotta in the valley, it tastes even better than anjappar parotta. Even though this place is known for biryani. This place also silently serves dosa which is really yummy. Its on par with dosa palace dosa with really good chutney and sambar. I would also try the chicken chukka, pepper chicken and request for higher spicy level if you are into more hot food. I would also try the Indo-chinese dishes like chicken fried rice, chicken manchurian and chilly chicken. That really gives a twist. ts a great to-go place to take good Indian food home.", ["biryani"]),True)
 

   
    def test_case2(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc(" The best Indian food in west Seattle, hands down!! I lived in little india in Queens for the last decade where they had very authentic Indian cuisine, and this is the best I have found since returning to the northwest.  You seriously should dine here.  We had the cheese pakoras, which were delicately fried and not too oily which is a common mistake, then we split the Chicken Makhni (Butter Chicken) and the Chicken Tikka Masala.  They are similar dishes and I wanted to see if they each held up their own identity. The Makhni held up well as my favorite go to Indian dish, at a selected 4 stars of spicyness it was just hot enough without taking away from the flavor, then the Tikka Masala was maybe the best I have ever tasted.  And I have tasted a lot. The chicken was perfectly cooked in both dishes and the balance of flavors and spices in the saucewas superb.  Please support this business.  It was slow on a Thursday night and it would have been great to see it full.  Whether or not you love indian food already or are interested I trying it for the first time, go to the Royal Indian Grill. It is just plain great", ["Indian","Hotels"]),True)
        
    def test_case3(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("deep dish pizza", ["deep","dish","pizza"]),True)
        
    def test_case4(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("deep dish pizza", ["hi"]),True)
        
    def test_case5(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("deep dish pizza", ["deep"]),True)
        
    def test_case6(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("deep                   dish pizza", ["deep"]),True)
        
    def test_case7(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("deep dish pizza. thats because deep pizza is never dish.blah blah blah blah blah blah blah blah blah blah blah blabh . blah blah blah blah blah b. blah balkhj", ["deep","sun"]),True)
        
    def test_case8(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("Its hard to beat an eatery that focuses on bacon and delivers it in meals of high quality and thoughtful design. Our first go around with Bacon Bacon was via their mobile truck which has since burned to the ground (not a grease fire, but an engine fire. New one on the way we hear), and that was amazing. Amazing savory combinations, some with excellent spicy options. For me, it just did not get much better than that.Now, visiting the store, the excellence continues. I had the the Hot Italian. My lady had the fried chicken sandwich. We split a side of Porky Fries.Heres the thing: these sandwiches and the fries could have been served sans bacon in any other restaurant and they would have been MAGNIFICENT. But here, they are thoughtfully paired with bacon and their magnificence increases exponentially. If you like great lunch [or breakfast] food at a reasonable price, the Bacon Bacon is worth a visit. If you like great lunch [or breakfast] food at a reasonable price and also love bacon, THEN YOU MUST VISIT.", ["bacon","sandwich"]),True)
        
    def test_case9(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("Negative 5 stars is more like it- this place should be called New India Bizarre - cramped, disorganized, dirty, and run by an individual who clearly takes no pride in his business.  If you happen to be of the Caucasian persuasion, you are much more likely to have your questions answered and be rung up in a timely manner - and the owner probably wont stay on his cell phone the entire time you are transacting your business, roll his eyes at you, or give you attitude since ringing you up is clearly distracting him from his very important conversation- no, that kind of treatment is reserved for those of us blessed with copious amounts of melanin.  I havent quite figured out if this disturbingly persistent trend among brethren from the Indian sub-continent is a remnant of British imperialism, simple self-hatred, or inextricably the result of both, but I simply have no tolerance for minorities who choose to pander after others like their money is somehow greener than mine.It really doesnt matter to me that you are 1 of only 2 Indian grocery stores in SF, and the only one near downtown - its still NOT OK for you to take undue advantage of your customers by charging them ridiculous amounts of money for expired groceries and oil-drenched samosas served alongside runny, watery chutney.  I much rather dine-in at Mehfil or Lahore Karahi, or even hoof it to Berkeley, Fremont, or San Jose, than spend any of my money on the likes of you.", ["indian","grocery","store"]),True)
        
    def test_case10(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("Negative 5 stars is more like it- this place should be called New India Bizarre - cramped, disorganized, dirty, and run by an individual who clearly takes no pride in his business.  If you happen to be of the Caucasian persuasion, you are much more likely to have your questions answered and be rung up in a timely manner - and the owner probably wont stay on his cell phone the entire time you are transacting your business, roll his eyes at you, or give you attitude since ringing you up is clearly distracting him from his very important conversation- no, that kind of treatment is reserved for those of us blessed with copious amounts of melanin.  I havent quite figured out if this disturbingly persistent trend among brethren from the Indian sub-continent is a remnant of British imperialism, simple self-hatred, or inextricably the result of both, but I simply have no tolerance for minorities who choose to pander after others like their money is somehow greener than mine.It really doesnt matter to me that you are 1 of only 2 Indian grocery stores in SF, and the only one near downtown - its still NOT OK for you to take undue advantage of your customers by charging them ridiculous amounts of money for expired groceries and oil-drenched samosas served alongside runny, watery chutney.  I much rather dine-in at Mehfil or Lahore Karahi, or even hoof it to Berkeley, Fremont, or San Jose, than spend any of my money on the likes of you.", ["indian","grocery"]),True)
    def test_case11(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("Negative 5 stars is more like it- this place should be called New India Bizarre - cramped, disorganized, dirty, and run by an individual who clearly takes no pride in his business.  If you happen to be of the Caucasian persuasion, you are much more likely to have your questions answered and be rung up in a timely manner - and the owner probably wont stay on his cell phone the entire time you are transacting your business, roll his eyes at you, or give you attitude since ringing you up is clearly distracting him from his very important conversation- no, that kind of treatment is reserved for those of us blessed with copious amounts of melanin.  I havent quite figured out if this disturbingly persistent trend among brethren from the Indian sub-continent is a remnant of British imperialism, simple self-hatred, or inextricably the result of both, but I simply have no tolerance for minorities who choose to pander after others like their money is somehow greener than mine.It really doesnt matter to me that you are 1 of only 2 Indian grocery stores in SF, and the only one near downtown - its still NOT OK for you to take undue advantage of your customers by charging them ridiculous amounts of money for expired groceries and oil-drenched samosas served alongside runny, watery chutney.  I much rather dine-in at Mehfil or Lahore Karahi, or even hoof it to Berkeley, Fremont, or San Jose, than spend any of my money on the likes of you.", ["indian","store"]),True)

    def test_case12(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc("Negative 5 stars is more like it- this place should be called New India Bizarre - cramped, disorganized, dirty, and run by an individual who clearly takes no pride in his business.  If you happen to be of the Caucasian persuasion, you are much more likely to have your questions answered and be rung up in a timely manner - and the owner probably wont stay on his cell phone the entire time you are transacting your business, roll his eyes at you, or give you attitude since ringing you up is clearly distracting him from his very important conversation- no, that kind of treatment is reserved for those of us blessed with copious amounts of melanin.  I havent quite figured out if this disturbingly persistent trend among brethren from the Indian sub-continent is a remnant of British imperialism, simple self-hatred, or inextricably the result of both, but I simply have no tolerance for minorities who choose to pander after others like their money is somehow greener than mine.It really doesnt matter to me that you are 1 of only 2 Indian grocery stores in SF, and the only one near downtown - its still NOT OK for you to take undue advantage of your customers by charging them ridiculous amounts of money for expired groceries and oil-drenched samosas served alongside runny, watery chutney.  I much rather dine-in at Mehfil or Lahore Karahi, or even hoof it to Berkeley, Fremont, or San Jose, than spend any of my money on the likes of you.", ["india","store"]),True)
        
            
    def test_case13(self):
        '''Printed if the test fails'''
        self.assertEqual(review.highlightDoc(" I like fish. Little stars deep dish pizza sure is fantastic. Dogs are funny.", ["deep","dish","pizza"]),True)
   
if __name__=='__main__':
    unittest.main()