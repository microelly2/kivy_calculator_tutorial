from kivy.app import App


class RechnerApp(App):
	pass

	def berechne(self,button,gui,app):
		print(" berechne wird ausgefuehrt")
		for x in [self,button,gui,app]:
			print(x)
		button.text='fertig berechnet'
		print("fertig.") 

meineAnwendung=RechnerApp()
print(meineAnwendung)
meineAnwendung.run()

