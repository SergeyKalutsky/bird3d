from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
cam = EditorCamera()
# cam.gravity = 0
Sky()

class Plane(Entity):
    def __init__(self):
        super().__init__(model='assets/plane2')
        self.texture = 'plane/Diffuse'

    def update(self):
        pass


class Bird(Entity):
    def __init__(self):
        super().__init__(model='assets/HUMBIRD', origin=(0,0.05,-0.5), parent=camera)

        self.texture = 'HUMBIRD.JPG'
        self.texture = 'HUMBIRD.TIF'

    def update(self):
        self.y -= 0.001
        if held_keys['d']:
            self.x += time.dt/100
            self.rotation_z += 0.2
            camera.rotation_y += 10 * time.dt
        if held_keys['a']:
            self.x -= time.dt/100
            self.rotation_z -= 0.2
            camera.rotation_y -= 10 * time.dt
        if held_keys['w']:
            self.z += time.dt
            camera.z += time.dt 
        if held_keys['s']:
            self.z -= time.dt
            camera.z -= time.dt 
        if held_keys['space']:
            self.y += time.dt/2


sphere = Entity(model="sphere", color=color.yellow, position=(10, 5, 5))
bird = Bird()
plane = Plane()


app.run()
