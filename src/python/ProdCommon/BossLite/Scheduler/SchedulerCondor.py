#!/usr/bin/env python
"""
_SchedulerCondor_
Scheduler class for vanilla Condor scheduler
"""

__revision__ = "$Id: SchedulerCondor.py,v 1.20 2009/12/15 15:01:43 ewv Exp $"
__version__ = "$Revision: 1.20 $"

import os

from SchedulerCondorCommon import SchedulerCondorCommon
from ProdCommon.BossLite.DbObjects.Job import Job
from ProdCommon.BossLite.DbObjects.Task import Task
from ProdCommon.BossLite.DbObjects.RunningJob import RunningJob

class SchedulerCondor(SchedulerCondorCommon) :
    """
    basic class to handle lsf jobs
    """
    def __init__( self, **args ):
        # call super class init method
        super(SchedulerCondor, self).__init__(**args)


    def jobDescription ( self, obj, requirements='', config='', service = '' ):
        """
        retrieve scheduler specific job description
        return it as a string
        """


    def findExecHost(self, requirements=''):
        return self.hostname


    def specificBulkJdl(self, job, requirements=''):
        # FIXME: This is very similar to SchedulerCondorCommon's version,
        # should be consolidated.
        """
        build a job jdl
        """
        rootName = os.path.splitext(job['standardError'])[0]

        jdl  = 'Universe  = vanilla\n'
        jdl += 'environment = CONDOR_ID=$(Cluster).$(Process)\n'
        jdl += 'log     = %s.log\n' % rootName # Same root as stderr

        if self.userRequirements:
            jdl += 'requirements = %s\n' % self.userRequirements

        x509 = self.x509Proxy()
        if x509:
            jdl += 'x509userproxy = %s\n' % x509

        return jdl


