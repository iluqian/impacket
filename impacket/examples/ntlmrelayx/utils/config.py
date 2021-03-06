#!/usr/bin/env python
# Copyright (c) 2013-2016 CORE Security Technologies
#
# This software is provided under under a slightly modified version
# of the Apache Software License. See the accompanying LICENSE file
# for more information.
#
# Config utilities
#
# Author:
#  Dirk-jan Mollema / Fox-IT (https://www.fox-it.com)
#
# Description:
#     Configuration class which holds the config specified on the
# command line, this can be passed to the tools' servers and clients
class NTLMRelayxConfig:
    def __init__(self):

        self.daemon = True

        # Set the value of the interface ip address
        self.interfaceIp = None

        self.domainIp = None
        self.machineAccount = None
        self.machineHashes = None
        self.target = None
        self.mode = None
        self.redirecthost = None
        self.outputFile = None
        self.attacks = None
        self.lootdir = None
        self.randomtargets = False
        self.encoding = None
        self.ipv6 = False

        #WPAD options
        self.serve_wpad = False
        self.wpad_host = None
        self.wpad_auth_num = 0
        self.smb2support = False

        #SMB options
        self.exeFile = None
        self.command = None
        self.interactive = False
        self.runSocks = False

        #LDAP options
        self.dumpdomain = True
        self.addda = True

        #MSSQL options
        self.queries = []

    def setInterfaceIp(self, ip):
        self.interfaceIp = ip

    def setRunSocks(self, socks):
        self.runSocks = socks

    def setOutputFile(self,outputFile):
        self.outputFile = outputFile

    def setTargets(self, target):
        self.target = target

    def setExeFile(self, filename):
        self.exeFile = filename

    def setCommand(self, command):
        self.command = command

    def setEncoding(self, encoding):
        self.encoding = encoding

    def setMode(self,mode):
        self.mode = mode

    def setAttacks(self,attacks):
        self.attacks = attacks

    def setLootdir(self,lootdir):
        self.lootdir = lootdir

    def setRedirectHost(self,redirecthost):
        self.redirecthost = redirecthost

    def setDomainAccount( self, machineAccount,  machineHashes, domainIp):
        self.machineAccount = machineAccount
        self.machineHashes = machineHashes
        self.domainIp = domainIp

    def setRandomTargets(self,randomtargets):
        self.randomtargets = randomtargets

    def setLDAPOptions(self,dumpdomain,addda):
        self.dumpdomain = dumpdomain
        self.addda = addda

    def setMSSQLOptions(self,queries):
        self.queries = queries

    def setInteractive(self,interactive):
        self.interactive = interactive

    def setIMAPOptions(self,keyword,mailbox,dump_all,dump_max):
        self.keyword = keyword
        self.mailbox = mailbox
        self.dump_all = dump_all
        self.dump_max = dump_max

    def setIPv6(self, use_ipv6):
        self.ipv6 = use_ipv6

    def setWpadOptions(self, wpad_host, wpad_auth_num):
        if wpad_host != None:
            self.serve_wpad = True
        self.wpad_host = wpad_host
        self.wpad_auth_num = wpad_auth_num
