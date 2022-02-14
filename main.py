from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
# cam = EditorCamera()
# cam.gravity = 0
Sky()


class Bird(Entity):
    def __init__(self):
        super().__init__(model='assets/HUMBIRD', origin=(0,0,-1), parent=camera)

        self.texture = 'HUMBIRD.JPG'
        self.texture = 'HUMBIRD.TIF'

    def update(self):
        print(self.x, self.y, self.z)
        if held_keys['d']:
            self.x += time.dt
            camera.rotation_y += 10 * time.dt
        if held_keys['a']:
            self.x -= time.dt
            camera.rotation_y -= 10 * time.dt
        if held_keys['w']:
            self.z += time.dt
        if held_keys['s']:
            self.z -= time.dt
        if held_keys['space']:
            self.y += time.dt


sphere = Entity(model="sphere", color=color.yellow, position=(10, 5, 5))
bird = Bird()


app.run()
