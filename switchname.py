#!/bin/python

import pexpect
import pdb
import sys, re
class FCoE_Helper():

	def ConnectToSwitch(self, ip, sw_name):
		self.sw = pexpect.spawn('ssh admin@'+ip)
		r = self.sw.expect([pexpect.TIMEOUT, '[P/p]assword:','(yes/no)'])
		#pdb.set_trace()
		if r == 0 :
			print "Not able to reach the switch"
		elif r == 2 :
			self.sw.sendline("yes")
			r1 = self.sw.expect([pexpect.TIMEOUT, '[P/p]assword:'])
			if r1 == 0 :
				print "Not able to reach the switch after giving yes"


		self.sw.sendline('nbv_12345')
		
		self.sw.expect([pexpect.TIMEOUT, '#'])
		self.sw.sendline('terminal length 0')
		self.sw.expect([pexpect.TIMEOUT, '#'])
		self.sw.sendline('conf')
		self.sw.expect([pexpect.TIMEOUT, '#'])
		
		self.sw.sendline('switchname '+ sw_name)
		self.sw.expect([pexpect.TIMEOUT, '#'])
		
fh = FCoE_Helper()
fh.ConnectToSwitch(ip=<IP>, sw_name = 'MDSNG')
