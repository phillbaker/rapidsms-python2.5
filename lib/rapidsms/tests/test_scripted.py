from harness import MockApp
from scripted import TestScript

class EchoApp (MockApp):
    def handle (self, message):
        MockApp.handle(self, message)
        message.respond(message.peer + ": " + message.text)

class MockTestScript (TestScript):
    apps = (EchoApp,)

    def testRunScript (self):
        self.runScript("""
            2345678901 > echo helloworld?
            2345678901 < helloworld?
        """)
    
    def testAssertInteraction (self):
        self.assertInteraction("""
            8005551212 > echo someuser
            8005551212 < someuser
        """)
    
    def testEmptyMessagesFail (self):
        def emptyMessage():
            self.assertInteraction("""
                8005551212 > echo someuser
                8005551212 < 
            """)
        
        self.assertRaises(AssertionError, emptyMessage)
            
    
    def testDifferentPeerNumbers (self):
        def differentPeerNumbers():
            self.assertInteraction("""
                8005551212 > echo someuser
                1 < someuser
            """)
        
        self.assertRaises(AssertionError, differentPeerNumbers)
            
        try:
            differentPeerNumbers()
        except AssertionError, e:
            self.assertEquals("Expected to respond to 1, but message was sent to 8005551212.\nMessage: 'echo someuser'", e.message)
    
    def testSameMessages (self):
        self.assertInteraction("""
            8005551212 > echo someuser
            8005551212 > echo someuser
            8005551212 < someuser
        """)
    
    def testMultipleMessages (self):
        self.assertInteraction("""
            8005551212 > echo someuser
            8005551212 < someuser
            8005551212 > echo another
            8005551212 < another
        """)

