#!/usr/bin/env python
#
# File: $Id$
#
"""
Some exceptions need to be generally available to many modules so they are
kept in this module to avoid ciruclar dependencies.
"""

# system imports
#
#######################################################################
#
# We have some basic exceptions used during the processing of commands
# to determine how we respond in exceptional situations
#
class ProtocolException(Exception):
    def __init__(self, value = "protocol exception"):
        self.value = value
    def __str__(self):
        return self.value

class No(ProtocolException):
    def __init__(self, value = "no"):
        self.value = value
    def __str__(self):
        return self.value

class Bad(ProtocolException):
    def __init__(self, value = "bad"):
        self.value = value
    def __str__(self):
        return self.value

class MailboxInconsistencey(ProtocolException):
    """
    When processing commands on a mailbox it is possible to hit a
    state where what is on disk is not what we expected it to be.

    Frequently the base action in these cases is to punt (because we
    are usually in a place where we can not regain consistency and
    maintain state).

    The upper layer is expected to catch this, initiate actions to
    regain consistent state, and then likely try the command again.
    """
    def __init__(self, value = "mailbox inconsistencey", mbox = None):
        self.value = value
        self.mbox = mbox
    def __str__(self):
        return self.value
    

