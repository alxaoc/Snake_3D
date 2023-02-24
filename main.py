from ursina import *

app = Ursina()
window.color = color.black

Light(type='ambient', color=(0.5, 0.5, 0.5, 1))
Light(type='directional', color=(0.5, 0.5, 0.5, 1), direction=(1, 1, 1, 1))
cube = Entity(model="cube", rotatioon=(-15, 0, 0), positio=(0, 0, 0), scale=4, color=color.orange)

app.run()
