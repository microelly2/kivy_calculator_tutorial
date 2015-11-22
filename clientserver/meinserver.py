# -*- coding: utf8 -*-
from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.internet import reactor
from twisted.internet import protocol

from kivy.app import App


class MeinProtokoll(protocol.Protocol):
    def dataReceived(self, data):
        response = self.factory.app.bearbeite_anfrage(data)
	print "Frage:"
	print(data)
	print "Antwort:"
	print(response)
        if response:
            self.transport.write(response)


class MeinServerFactory(protocol.Factory):
    protocol = MeinProtokoll

    def __init__(self, app):
        self.app = app


class MeinServerApp(App):

    def bearbeite_anfrage(self, frage):

	frage=frage.rstrip()
        self.root.label.text += "Frage:  %s\n" % frage

        if frage == "3*4":
            antwort = "12"
        elif frage == "12/3":
            antwort = "4"
	else:
	   antwort = "kann ich nicht beantworten" 

        self.root.label.text += "Antwort: %s\n" % antwort

        return antwort+"\nNächste Aufgabe:"



if __name__ == '__main__':

	app=MeinServerApp()
	reactor.listenTCP(5678, MeinServerFactory(app))
	app.run()
