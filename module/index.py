from mod1 import title
from time import sleep
import random
print(__name__)
bulb = title.Bulb(random.choice([True,False]))
print(bulb.lightState())
