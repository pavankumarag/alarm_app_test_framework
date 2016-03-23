import unittest,os,re,time 
from application.Alarms_implementation import *
import logging
from lib.logmod import configure_log
import sys,argparse




class TestApplication(unittest.TestCase):
    def setUp(self):
        logger.info("-----START------")
        logger.info("We are in setup, creating alarm obj")
        self.alarm_added = 0
        self.a = Alarm()
        pass
    
    def test_1_add(self):
        #a = Alarm()
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        logger.info("=====Functional test for ADD feature=====")
        
        a.add(title,fire_time,repeat) 
        self.alarm_added =  self.alarm_added +1  
        if title == a.alarms[0]['title']:
            logger.info("PASS : Data integrity test for title")
        else:
            logger.info("FAIL : Data integrity test for title")
        if fire_time == a.alarms[0]['fire_time']:
            logger.info("PASS : Data integrity test for fire_time")
        else:
             logger.info("FAIL : Data integrity test for fire_time")
        if repeat == a.alarms[0]['repeat']:
            logger.info("PASS : Data integrity test for repeat")
        else:
            logger.info("FAIL : Data integrity test for repeat")
           
        title1 = title + "another"
        a.add(title1,fire_time,repeat)
        self.alarm_added =  self.alarm_added +1  
        if title1 == a.alarms[1]['title']:
            logger.info("PASS : Data integrity test for title")
        else:
            logger.info("FAIL : Data integrity test for title")
        
        if self.alarm_added == a.count():
            logger.info("PASS : Add function adds one alarm")
        else:
            logger.info("FAIL : Add function adds one alarm")

        self.assertEquals(title, a.alarms[0]['title'], "FAIL : Data intergrity test for title")
        self.assertEquals(fire_time, a.alarms[0]['fire_time'], "FAIL : Data intergrity test for fire_time") 
        self.assertEquals(repeat, a.alarms[0]['repeat'], "FAIL : Data intergrity test for repeat")
        self.assertEquals(title1, a.alarms[1]['title'], "FAIL : Data intergrity test for title")
    
    def test_2_update(self):
        logger.info("=====Functional test for UPDATE feature=====")
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        title = title + " update" 
        fire_time = "Tue Mar 23 00:59:30 IST 2016"
        repeat = True
        a.update(0,title,fire_time,repeat)
        if title == a.alarms[0]['title']:
            logger.info("PASS : Update Data integrity test for title")
        else:
            logger.info("FAIL : Update Data integrity test for title")
        if fire_time == a.alarms[0]['fire_time']:
            logger.info("PASS : Update Data integrity test for fire_time")
        else:
             logger.info("FAIL : Update Data integrity test for fire_time")
        if repeat == a.alarms[0]['repeat']:
            logger.info("PASS : Update Data integrity test for repeat")
        else:
            logger.info("FAIL : Update Data integrity test for repeat")
        
        if self.alarm_added == a.count():
            logger.info("PASS : Update function just updates an alarm and not addition")
        else:
            logger.info("FAIL : Update function just updates an alarm and not addition")
                
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        title1 = title + " And another"
        a.update(1,title1,fire_time,repeat)
        if self.alarm_added == a.count():
            logger.info("PASS : Update function just updates an alarm and not addition")
        else:
            logger.info("FAIL : Update function just updates an alarm and not addition")
        if title1 == a.alarms[1]['title']:
            logger.info("PASS : Update Data integrity test for title")
        else:
            logger.info("FAIL : Update Data integrity test for title")
        
        self.assertEquals(title, a.alarms[0]['title'], "FAIL : Update Data intergrity test for title")
        self.assertEquals(fire_time, a.alarms[0]['fire_time'], "FAIL : Update Data intergrity test for fire_time") 
        self.assertEquals(repeat, a.alarms[0]['repeat'], "FAIL : Update Data intergrity test for repeat")
        self.assertEquals(title1, a.alarms[1]['title'], "FAIL : Update Data intergrity test for title")    
        
        #logger.info(a.alarms)
    
    def test_3_remove(self):
        logger.info("=====Functional test for UPDATE feature======")
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        title = title + " another"
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        
        a.remove(0)
        self.alarm_added = self.alarm_added - 1
        if self.alarm_added == a.count():
            logger.info("PASS : Remove function successfully deletes an alarm")
        else:
            logger.info("FAIL : Remove function successfully deletes an alarm")
            
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        #logger.info(a.alarms)
        a.remove(2)
        self.alarm_added = self.alarm_added - 1
        if self.alarm_added == a.count():
            logger.info("PASS : Remove function successfully deletes an alarm")
        else:
            logger.info("FAIL : Remove function successfully deletes an alarm")   
        
        self.assertEquals(title, a.alarms[1]['title'], "FAIL : Update Data intergrity test for title")
        self.assertEquals(fire_time, a.alarms[1]['fire_time'], "FAIL : Update Data intergrity test for fire_time") 
        self.assertEquals(repeat, a.alarms[1]['repeat'], "FAIL : Update Data intergrity test for repeat")
        
        
    def test_4_clear(self):
        logger.info("=====Functional test for CLEAR feature=====")
        a =self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        
        title1 = "New alarm test"
        a.add(title1,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1  
        
        repeat = True
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully added %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully added %d %d alarms" %(self.alarm_added,a.count()))
        
        a.clear()
        self.alarm_added = 0
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully cleared all alarms; %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully cleared all alarms; %d %d alarms" %(self.alarm_added,a.count()))
        self.assertEquals(self.alarm_added, a.count(), "FAIL to clear the alarms")
        
        
    def test_5_count(self):
        logger.info("=====Functional test for COUNT feature=====")
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully count is reflected after addition %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully count is reflected after addition %d %d alarms" %(self.alarm_added,a.count()))
            
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully count is reflected after addition %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully count is reflected after addition %d %d alarms" %(self.alarm_added,a.count()))   
            
        a.remove(1)
        self.alarm_added = self.alarm_added - 1
        
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully count is reflected after deletion of alarm  %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully count is reflected after deletion of alarm %d %d alarms " %(self.alarm_added,a.count()))  
        self.assertEquals(self.alarm_added, a.count(), "FAIL to clear the alarms")
        
            
        
    def test_6_get(self):
        logger.info("=====Functional test for GET feature=====")
        a=self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        
        title1 = title + " another"
        a.add(title1,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        
        alarm_output = a.get(0)
        #logger.info(alarm_output)
        if title == alarm_output['title']:
            logger.info("PASS : GET feature functional test for title")
        else:
            logger.info("FAIL : GET feature functional test for title")
        if fire_time == alarm_output['fire_time']:
            logger.info("PASS : GET feature functional test for fire_time")
        else:
             logger.info("FAIL : GET feature functional test for fire_time")
        if repeat == alarm_output['repeat']:
            logger.info("PASS : GET feature functional test for repeat")
        else:
            logger.info("FAIL : GET feature functional test for repeat")
            
        a.update(0,title1,fire_time,repeat)
        alarm_output = a.get(0)
        if title1 == alarm_output['title']:
            logger.info("PASS : GET feature functional test for title")
        else:
            logger.info("FAIL : GET feature functional test for title")
        alarm_output1 = a.get(1)    
        
        self.assertEquals(title1, alarm_output['title'], "FAIL : GET test for title")
        self.assertEquals(fire_time, alarm_output['fire_time'], "FAIL : GET test for fire_time") 
        self.assertEquals(repeat, alarm_output['repeat'], "FAIL : GET test for repeat")
        self.assertEquals(title1, alarm_output['title'], "FAIL : GET test for title")
        
    def test_7_get_nonexistantdata(self):
        logger.info("=====Testing GET functionality for non existant ID=====")
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        try:
            alarm_output = a.get(1)
        except AlarmNotFound:
            logger.error("Alarm not found for the given ID")
            
    
    def test_7_remove_nonexistantdata(self):
        logger.info("=====Testing REMOVE functionality for non existant ID=====")
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        a.add(title,fire_time,repeat)
        self.alarm_added = self.alarm_added + 1
        try:
            a.remove(1)
        except AlarmNotFound:
            logger.error("Alarm not found for the given ID")
            
                       
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
    




