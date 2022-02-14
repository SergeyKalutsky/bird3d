from sklearn.preprocessing import scale
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
cam = EditorCamera()
# cam.gravity = 0
Sky()

class Plane(Entity):
    def __init__(self):
        super().__init__(model='assets/plane', scale=0.001)
        self.texture = '11803_Airplane_body_diff.jpg'
        self.texture = '11803_Airplane_wing_big_L_diff.jpg'
        self.texture = '11803_Airplane_wing_big_R_diff.jpg'
        self.texture = '11803_Airplane_wing_big_R_diff.jpg'


class Bird(Entity):
    def __init__(self):
        super().__init__(model='assets/HUMBIRD', origin=(0,0.05,-0.5), parent=camera)

        self.texture = 'HUMBIRD.JPG'
        self.texture = 'HUMBIRD.TIF'

    def update(self):
        self.y -= 0.001
        if held_keys['d']:
            self.x += time.dt/10
            camera.rotation_y += 10 * time.dt
        if held_keys['a']:
            self.x -= time.dt/10
            camera.rotation_y -= 10 * time.dt
        if held_keys['w']:
            self.z += time.dt
        if held_keys['s']:
            self.z -= time.dt
        if held_keys['space']:
            self.y += time.dt/2


sphere = Entity(model="sphere", color=color.yellow, position=(10, 5, 5))
bird = Bird()
plane = Plane()


app.run()
