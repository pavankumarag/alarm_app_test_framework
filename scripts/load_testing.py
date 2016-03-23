import unittest,os,re,time,argparse  
from application.Alarms_implementation import *
import logging
from lib.logmod import configure_log


class TestApplication(unittest.TestCase):
    def setUp(self):
        logger.info("-----START------")
        logger.info("We are in setup, creating alarm obj")
        self.alarm_added = 0
        self.a = Alarm()
        pass
    
    def test_1_add(self):
        logger.info("Load testing the add functionality of alarm application")
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        for i in range(1000):
            title1 = title + " %d"%i
            a.add(title1,fire_time,repeat)
            self.alarm_added = self.alarm_added + 1
            
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully loaded alarams  %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully loaded alarams %d %d alarms" %(self.alarm_added,a.count()))
        self.assertEquals(self.alarm_added, a.count(), "FAIL to load the alarms %d" %self.alarm_added)
        
    def test_2_update(self):
        logger.info("Load testing the update functionality of  alarm application")
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        for i in range(1000):
            title1 = title + " %d"%i
            a.add(title1,fire_time,repeat)
            self.alarm_added = self.alarm_added + 1
            
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully loaded alarams  %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully loaded alarams %d %d alarms" %(self.alarm_added,a.count()))
        title = title + " another"
        
        for i in range(1000):
            title1 = title + "_%d"%i
            a.update(i,title1,fire_time,repeat)
        
        self.assertEquals(self.alarm_added, a.count(), "FAIL to load the alarms %d" %self.alarm_added)
            
    def test_2_remove(self):
        logger.info("Load testing the remove functionality of  alarm application")
        a = self.a
        title = "New alarm test"
        fire_time = "Tue Mar 22 00:59:30 IST 2016"
        repeat = False
        for i in range(1000):
            title1 = title + " %d"%i
            a.add(title1,fire_time,repeat)
            self.alarm_added = self.alarm_added + 1
            
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully loaded alarams  %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully loaded alarams %d %d alarms" %(self.alarm_added,a.count()))
        title = title + " another"
        for i in range(1000):
            a.remove(i)
            self.alarm_added = self.alarm_added - 1
        if self.alarm_added == a.count():
            logger.info("PASS : Successfully removed alarams  %d %d alarms" %(self.alarm_added,a.count()))
        else:
            logger.info("FAIL : Successfully removed alarams %d %d alarms" %(self.alarm_added,a.count()))
        self.assertEquals(self.alarm_added, a.count(), "FAIL to load the alarms %d" %self.alarm_added)
        
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
