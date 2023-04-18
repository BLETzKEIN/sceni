import time
import model
import controller,controller2
import view,view2

while True:
    time.sleep(1 / 100)
    if model.scena == "rect":
        controller.events()
        view.weiv()
    else:
        controller2.events()
        view2.weiv()
