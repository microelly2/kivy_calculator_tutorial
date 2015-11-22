from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.internet import reactor, protocol
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MeinProtokoll(protocol.Protocol):
	def connectionMade(self):
		self.factory.app.on_connection(self.transport)

	def dataReceived(self, data):
		self.factory.app.zeige_antwort(data)



class MeineClientFactory(protocol.ClientFactory):
	protocol = MeinProtokoll

	def __init__(self, app):
		self.app = app

	def clientConnectionLost(self, conn, reason):
		self.app.zeige_antwort("Verbindung verloren")
		self.app.zeige_antwort(str(reason))

	def clientConnectionFailed(self, conn, reason):
		self.app.zeige_antwort("Verbindung fehlgeschlagen")
		print ("Verbindung fehlgeschlagen")
		print(reason)


class MeinClientApp(App):
	connection = None

	def connect_to_server(self,host='127.0.0.1',port=5678):
		reactor.connectTCP(host,port, MeineClientFactory(self))

	def on_connection(self, connection):
		self.zeige_antwort("Verbindung ist aufgebaut!")
		self.connection = connection

	def sende_frage(self, *args):
		frage = str(self.root.textbox.text)
		if frage and self.connection:
			print ("Sende Frage :" + frage)
			self.root.label.text += frage + " ... \n"
			self.connection.write(frage)
		else:
			print ("keine Frage gestellt oder keine Verbindung vorhanden")

	def zeige_antwort(self, antwort):
		print ("Antwort :" + antwort)
		self.root.label.text += antwort + "\n"

if __name__ == '__main__':

	app=MeinClientApp()
	app.connect_to_server()
	app.run()

