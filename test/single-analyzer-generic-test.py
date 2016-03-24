#!/usr/bin/python
# Filename: single-analyzer-test.py

"""
A test suite for single analyzer

Author: Yuanjie Li
"""

import sys
import logging
import unittest

from mobile_insight.monitor import QmdlReplayer
from mobile_insight.analyzer import Analyzer
import mobile_insight.analyzer


def test_replayer_generator(analyzer_name, log_path):
    """
    Generate a test for a specific operator

    :param analyzer_name: the analyzer to be tested
    :log_path: the path of a mobileinsight log
    """

    def test(self):

        #Single analyzer test only
    	Analyzer.reset()

        src = QmdlReplayer()
        src.set_input_path(log_path)

        #Indirectly call analyzer via include_analyzer
        test_analyzer = Analyzer()
        test_analyzer.include_analyzer(analyzer_name,[])
        test_analyzer.set_source(src)

        #Disable all MobileInsight logs
        logging.getLogger('mobileinsight_logger').setLevel(logging.CRITICAL)

        src.run()

    return test

class SingleAnalyzerTest(unittest.TestCase):
    """
    A fixture (container) to hold automatically generated tests
    """
    pass

if __name__ == "__main__":

    operator_logs={"att" : "./test-logs/ATT.mi2log",
                   "tmobile" : "./test-logs/tmobile.mi2log",
                   "verizon" : "./test-logs/verizon.mi2log",
                   "sprint" : "./test-logs/sprint.mi2log",
                   "cmcc" : "./test-logs/CMCC.mi2log",
                   "att-iphone" : "./test-logs/ATT-iphone.mi2log"}


    analyzers=["UmtsNasAnalyzer"]
    # analyzers = mobile_insight.analyzer.__all__
    # forbidden_list=["HandoffLoopAnalyzer","Analyzer","LogAnalyzer","ProfileHierarchy","Profile","StateMachine","GuiAnalyzer"]
    # analyzers = [x for x in analyzers if x not in forbidden_list]


    for analyzer_name in analyzers:
        for operator in operator_logs:
            test_name = 'test_%s_%s' % (operator, analyzer_name)
            print "Add test: ",test_name
            test = test_replayer_generator(analyzer_name, operator_logs[operator])
            setattr(SingleAnalyzerTest, test_name, test)

    unittest.main()
