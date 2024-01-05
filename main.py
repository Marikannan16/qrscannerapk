from kivymd.app import MDApp
from kivy.lang import Builder
from pyzbar.pyzbar import ZBarSymbol
from kivymd.uix.snackbar import Snackbar
import pyttsx3




KV = """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
MDBoxLayout:
	orientation:'vertical'
	ZBarCam:
		id:zbarcam
		code_types:ZBarSymbol.QRCODE.value,ZBarSymbol.EAN13.value
		on_symbols:app.on_symbols(*args)

"""

class Myapp(MDApp):
	def build(self):
		self.root = Builder.load_string(KV)

	def on_symbols(self,instance,symbols):
		if not symbols == "":
			for symbol in symbols:
				da=symbol.data.decode()
				print("YOu Qr is : ",da)
				Snackbar(
				text="You Qr is : {}".format(symbol.data.decode()),
				md_bg_color="green",
				font_size=25

				).open()
				engine=pyttsx3.init()
				voices=engine.getProperty('voices')
				for voice in voices:
					engine.setProperty('voice',voice.id)
					engine.say(da)
					engine.runAndWait()	

if __name__ == "__main__":
	Myapp().run()