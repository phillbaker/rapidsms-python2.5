
import unittest
from rapidsms.tests.scripted import TestScript
#from  rapidsms.tests.harness import MockApp#TODO something is causing these tests to hang. Is it the lack of apps=''? Is it because there is no App for registration? Why isn't there a bug filed for this
#is there a bug in the harness/etc for using a non-app handler?
#why does it not hang/block when tests fail? why does it only mess up with everything else works?
#looks like it's really assertInteration that's the problem

class TestRegister(TestScript):

    def testRegister(self):
        self.assertInteraction("""
          8005551212 > register as someuser
          8005551212 < Thank you for registering, as someuser!
        """)

    def testLang(self):
        self.assertInteraction("""
          8005551212 > lang english
          8005551212 < You must JOIN or IDENTIFY yourself before you can set your language preference.
          8005551212 > register as someuser
          8005551212 < Thank you for registering, as someuser!
          8005551212 > lang english
          8005551212 < I will speak to you in English.
          8005551212 > lang klingon
          8005551212 < Sorry, I don't speak "klingon".
        """)

    def testHelp(self):
        self.assertInteraction("""
          8005551212 > lang
          8005551212 < To set your language, send LANGUAGE <CODE>
          8005551212 > register
          8005551212 < To register, send JOIN <NAME>
        """)
