from harness import EchoApp
from scripted import TestScript

class MockTestScript (TestScript):
    apps = (EchoApp,)

    testScript = """
        8005551212 > hello
        8005551212 < 8005551212: hello
    """
    testScript2 = """
        1234567890 > echo this!
        1234567890 < 1234567890: echo this!
    """
    
    def testClosure (self):
        self.assertEquals(type(self.testScript.func_defaults), tuple)
        self.assertEquals(type(self.testScript.func_defaults[0]), list)
        self.assertNotEquals(self.testScript.func_defaults,
                             self.testScript2.func_defaults)

    def testRunScript (self):
        self.runScript("""
            2345678901 > echo?
            2345678901 < 2345678901: echo?
        """)
    
    def testAssertInteraction(self):
        self.assertInteraction("""
            8005551212 > echo someuser
            8005551212 < someuser
        """)
    