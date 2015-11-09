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

	def gengraph(self,button):
		print("Wir zeichnen einen Graphen") 
		from graph import Graph, MeshLinePlot
		from math import *
		graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
		x_ticks_major=25, y_ticks_major=1,
		y_grid_label=True, x_grid_label=True, padding=5,
		x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)

		plot = MeshLinePlot(color=[1, 0, 0, 1])
		plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
		graph.add_plot(plot)

		plot2= MeshLinePlot(color=[1, 1, 0, 1])
		plot2.points = [(x, 0.02*x -1.0) for x in range(0, 101)]
		graph.add_plot(plot2)

		print (graph)
		button.parent.add_widget(graph)

meineAnwendung=RechnerApp()
print(meineAnwendung)
meineAnwendung.run()


