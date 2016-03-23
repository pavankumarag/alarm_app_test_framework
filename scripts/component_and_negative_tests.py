import unittest,os,re,time 
from application.Alarms_implementation import *
import logging,argparse
from lib.logmod import configure_log


class TestApplication(unittest.TestCase):
    def setUp(self):
        logger.info("-----START------")
        logger.info("We are in setup, creating alarm obj")
        self.alarm_added = 0
        self.a = Alarm()
        pass
    
    def test_1_component_add(self):
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = "hello"
        logger.info("=====Component test for ADD feature; check add feature behavior when string repeat passed=====")
        
        a.add(title,fire_time,repeat) 
        self.alarm_added =  self.alarm_added +1  
        
        if self.alarm_added == a.count():
            logger.info("PASS : Add function adds one alarm")
        else:
            logger.info("FAIL : Add function adds one alarm")
            
        logger.info("Data sent; title ->'%s' fire_time -> '%s' repeat ->'%r'" %(title,fire_time,repeat))
        logger.info("Data added %r " %a.alarms[0])
        
        if True == a.alarms[0]['repeat']:
            logger.info("PASS : Data integrity test for repeat %r %r" %(repeat, a.alarms[0]['repeat']))
        else:
            logger.info("FAIL : Data integrity test for repeat")
        
        self.assertEquals(title, a.alarms[0]['title'], "FAIL : Data intergrity test for title")
        self.assertEquals(fire_time, a.alarms[0]['fire_time'], "FAIL : Data intergrity test for fire_time") 
        self.assertEquals(True, a.alarms[0]['repeat'], "FAIL : Data intergrity test for repeat")
    
    def test_2_component_add(self):
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = True
        logger.info("=====Component test for ADD feature; Passing insufficient argument when \"add\" takes 3=====")
        try:
            a.add(title) 
        except:
             logger.error("TypeError: Passed only 1 argument , whereas add needs atleast 2 arguments to be passed") 
        
        try:
            a.add() 
        except:
             logger.error("TypeError: No argument passed , whereas add needs atleast 2 arguments to be passed")
             
        try:
            a.add(title,fire_time,repeat,fire_time) 
        except:
             logger.error("TypeError: More than 3 arguments passed , whereas add needs atmost 3 arguments to be passed")
             
        if a.count() == 0:
            logger.info("PASS : Add function failed to add alarm due to insufficient arguments as expected")
        else:
            logger.info("FAIL : Add function adds one alarm,where its not expected")
            
        self.assertEquals(0, a.count(), "FAIL : Add function adds one alarm,where its not expected")
    
    
    def test_3_component_update(self):
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        logger.info("=====Component test for UPDATE feature; check update feature behavior when string repeat passed=====")
        
        a.add(title,fire_time,repeat) 
        self.alarm_added =  self.alarm_added +1 
        repeat="hello" 
        a.update(0,title,fire_time,repeat)
        
        if self.alarm_added == a.count():
            logger.info("PASS : Add function adds one alarm")
        else:
            logger.info("FAIL : Add function fails to add alarm")
            
        logger.info("Data sent for update; title ->'%s' fire_time -> '%s' repeat ->'%r'" %(title,fire_time,repeat))
        logger.info("Data updated %r " %a.alarms[0])
        
        self.assertEquals(title, a.alarms[0]['title'], "FAIL : Data intergrity test for title")
        self.assertEquals(fire_time, a.alarms[0]['fire_time'], "FAIL : Data intergrity test for fire_time") 
        self.assertEquals(True, a.alarms[0]['repeat'], "FAIL : Data intergrity test for repeat")
        
    def test_4_component_update(self):
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = True
        logger.info("=====Component test for UPDATE feature; Passing insufficient argument when \"add\" takes 3=====")
        a.add(title,fire_time,repeat) 
        self.alarm_added =  self.alarm_added +1
        
        title1 = title +" updated"
        a.update(0,title1) 
        if title1 == a.alarms[0]['title']:
            logger.info("PASS : Updates an alarm when only title is passed")
        else:
            logger.info("FAIL : Failed to update an alarm when only title is passed")
    
        try:
            a.update() 
        except:
             logger.error("TypeError: No argument passed , whereas add needs atleast 2 arguments to be passed")
             
        try:
            a.update(0,title,fire_time,repeat,fire_time) 
        except:
             logger.error("TypeError: More than 4 arguments passed , whereas add needs atmost 4 arguments to be passed")
        
        #try:
        logger.info("Passing non existent id to update")
        a.update(-1,title,fire_time,repeat)
        self.alarm_added =  self.alarm_added +1
        if self.alarm_added == a.count():
            logger.info("PASS : UPDATE function adds one alarm when non-existant ID is passed")
        else:
            logger.info("FAIL : UPDATE function failed to add an alarm when non-existant ID is passed")
            
        self.assertEquals(self.alarm_added, a.count(), "FAIL : Update function failed to add an alarm non existant ID is passed")
        
    def test_5_component_get(self):
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = True
        logger.info("=====Component test for GET feature; 'get' negative id and larger id=====")
        a.add(title,fire_time,repeat) 
        self.alarm_added =  self.alarm_added +1
        try:
            a.get(-1)
        except:
            logger.error("Alarm not found when executed a.get(-1)")
        for i in range(1000):
            title1 = title + " %d"%i
            a.add(title1,fire_time,repeat)
            self.alarm_added = self.alarm_added + 1    
        
        alarm_output = a.get(1000)
        if len(alarm_output) > 0:
            logger.info("PASS: a.get(1000) gets an alarm %r" %alarm_output)
        self.assertEquals(self.alarm_added, a.count(), "FAIL : Alarm count is not same as alarms added")
        
    def test_5_component_remove(self):
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = True
        logger.info("=====Component test for REMOVE feature; 'remove' negative id and larger id=====")
        a.add(title,fire_time,repeat) 
        self.alarm_added =  self.alarm_added +1
        try:
            a.remove(-1)
        except:
            logger.error("Exception:Alarm not found when executed a.remove(-1)")
        for i in range(1000):
            title1 = title + " %d"%i
            a.add(title1,fire_time,repeat)
            self.alarm_added = self.alarm_added + 1    
        
        a.remove(1000)
        self.alarm_added =  self.alarm_added - 1
        if self.alarm_added == a.count():
            logger.info("PASS : Remove function removes an alarm when executed with larger value, a.remove(1000)")
        else:
            logger.info("FAIL : Failed to remove when executed a.remove(1000)")
        self.assertEquals(self.alarm_added, a.count(), "FAIL : Alarm count is not same as alarms added")   
        
    def tearDown(self):
        logger.debug(self.a.alarms)
        logger.info("We are in tear down, clearing all the alarms")
        self.a.clear()
        logger.debug(self.a.alarms)
        pass
    
if __name__ == "__main__":
    filename = "results/%s.log_%d" %(os.path.basename(__file__).split('.')[0],int(time.time()))    
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="to display debug logs",action="store_true")
    args = parser.parse_args()
    if args.verbose:
        logger = configure_log(logging.DEBUG, __name__,filename)
        logger.info("debug mode turned on")
    else:
        logger = configure_log(logging.INFO, __name__,filename)
    unittest.main(verbosity=5)
