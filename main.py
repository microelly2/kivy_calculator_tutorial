from kivy.app import App


class RechnerApp(App):
	pass

	def berechne(self,button,gui,app):
		print(" berechne wird ausgefuehrt")
		for x in [self,button,gui,app]:
			print(x)
		button.text='fertig berechnet'
		print("fertig.") 

	def button_pressed(self, button):
		print(button.text) 
		print(self.root.ids)
		if self.root.ids.outputLabel.text == 'Hallo':
			self.root.ids.outputLabel.text = button.text
		else:
			self.root.ids.outputLabel.text += button.text

	def berechne2(self):
			self.root.ids.outputLabel.text = str(eval(self.root.ids.outputLabel.text))

	def reset(self):
		self.root.ids.outputLabel.text = 'Hallo'

meineAnwendung=RechnerApp()
print(meineAnwendung)
meineAnwendung.run()


