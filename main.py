import time
import model
import controller
import view

while True:
    time.sleep(1/100)
    controller.events()
    view.weiv()