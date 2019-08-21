#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import datetime
import logging as log
from configparser import ConfigParser
from driver_program import processResourceAlignment
#from Driver_Program import processResourceAlignment_Test
import sys
def main():
    # ------------------------------------------------------------------------------------------------------------------
    # Start the program
     if sys.argv[1]=='train':
        start_exec_time = datetime.datetime.now()
        # ------------------------------------------------------------------------------------------------------------------
        # Fetch the properties and configurations
        prop = ConfigParser()
        prop.read(r"/home/SubramaniamS/Knovation-ELA/Incremental_resources/properties.ini")
        # ------------------------------------------------------------------------------------------------------------------
        #  Setup Logging mechanism
        for handler in log.root.handlers[:]:
            log.root.removeHandler(handler)
        log.basicConfig(filename=prop.get("Logging", "log_filepath")+"Knovation" + str(start_exec_time).split()[0] +".log",filemode = 'w',level=prop.get("Logging", "log_level"))
    #    log.basicConfig(filename=prop.get("Logging", "log_filepath")+'knovation',level="INFO")
    
        log.info(
            "-------------------------------------" + str(start_exec_time) + "-----------------------------------------")
        log.info("Initializing the process...")
        # -----------------------------------------------------------------------------------------------------------------
        # Fetch the properties and configurations
        log.info("Checking for configurations...")
        subject = (prop.get("Default", 'subject')).encode('UTF8')
        log.info(subject)
        log.info("Configurations loaded successfully...")
        # -----------------------------------------------------------------------------------------------------------------------
        
        processResourceAlignment(prop,log)
        end_exec_time = datetime.datetime.now()
    
        execution_response_time = end_exec_time - start_exec_time
        log.info("Execution time of the entire program is " + str(execution_response_time.total_seconds()))
        log.shutdown()
     elif sys.argv[1]=='test':
        start_exec_time = datetime.datetime.now()
        # ------------------------------------------------------------------------------------------------------------------
        # Fetch the properties and configurations
        prop = ConfigParser()
        prop.read(r"/home/SubramaniamS/Knovation-ELA/Incremental_resources/properties.ini")
        # ------------------------------------------------------------------------------------------------------------------
        #  Setup Logging mechanism
        for handler in log.root.handlers[:]:
            log.root.removeHandler(handler)
        log.basicConfig(filename=prop.get("Logging", "log_filepath")+"Knovation_test" + str(start_exec_time).split()[0] +".log",filemode = 'w',level=prop.get("Logging", "log_level"))
    #    log.basicConfig(filename=prop.get("Logging", "log_filepath")+'knovation',level="INFO")
    
        log.info(
            "-------------------------------------" + str(start_exec_time) + "-----------------------------------------")
        log.info("Initializing the process...")
        # -----------------------------------------------------------------------------------------------------------------
        # Fetch the properties and configurations
        log.info("Checking for configurations...")
        subject = (prop.get("Default", 'subject')).encode('UTF8')
        log.info(subject)
        log.info("Configurations loaded successfully...")
        # -----------------------------------------------------------------------------------------------------------------------
        
        processResourceAlignment(prop,log)
        end_exec_time = datetime.datetime.now()
    
        execution_response_time = end_exec_time - start_exec_time
        log.info("Execution time of the entire program is " + str(execution_response_time.total_seconds()))
        log.shutdown()

     
if __name__ == '__main__':
    main()
     
    
    
    

