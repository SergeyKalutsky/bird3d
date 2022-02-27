from ursina import *
from random import uniform

app = Ursina()
# cam = EditorCamera()
Sky()

class Plane(Entity):
    def __init__(self, origin, speed):
        super().__init__(model='assets/plane2', origin=origin, collider='box')
        self.texture = 'plane/Diffuse'
        self.rotation_y = 180
        self.rotation_x += 7
        self.speed = speed

    def update(self):
        self.z -= self.speed
        if self.z <= -150:
            score.text = str(int(score.text) + 1)
            self.z = 100
            self.x = uniform(-6, 6)
            self.y = uniform(-20, 20)
        info = self.intersects()
        print(info.hit)


class Bird(Entity):
    def __init__(self):
        super().__init__(model='assets/HUMBIRD', origin=(0,0.05,-0.5), parent=camera, scale = 16, collider='box')
        self.texture = 'HUMBIRD.JPG'
        self.texture = 'HUMBIRD.TIF'

    def update(self):
        if held_keys['d']:
            self.x += time.dt
            self.rotation_z += 1
            camera.rotation_y += 10 * time.dt
        if held_keys['a']:
            self.x -= time.dt
            self.rotation_z -= 1
            camera.rotation_y -= 10 * time.dt
        if held_keys['w']:
            self.z += time.dt
            camera.z += time.dt
        if held_keys['s']:
            self.z -= time.dt
            camera.z -= time.dt
        if held_keys['space']:
            self.y += 0.1
            camera.y += 0.1
        self.y -= 0.02
        camera.y -= 0.02


#sphere = Entity(model="sphere", color=color.yellow, position=(10, 5, 5))
bird = Bird()
for i in range(5):
   Plane(origin=(uniform(-6, 6), uniform(-20, 20)), speed=uniform(0.10,2))

score = Text(text='0', y=.43, x=-.75, scale=1.5, origin=(0, 0), background=True)

app.run()
from ursina import *
from random import uniform

app = Ursina()
# cam = EditorCamera()
Sky()

class Plane(Entity):
    def __init__(self, origin, speed):
        super().__init__(model='assets/plane2', origin=origin, collider='box')
        self.texture = 'plane/Diffuse'
        self.rotation_y = 180
        self.rotation_x += 7
        self.speed = speed

    def update(self):
        self.z -= self.speed
        if self.z <= -150:
            score.text = str(int(score.text) + 1)
            self.z = 100
            self.x = uniform(-6, 6)
            self.y = uniform(-20, 20)
        info = self.intersects()
        print(info.hit)


class Bird(Entity):
    def __init__(self):
        super().__init__(model='assets/HUMBIRD', origin=(0,0.05,-0.5), parent=camera, scale = 16, collider='box')
        self.texture = 'HUMBIRD.JPG'
        self.texture = 'HUMBIRD.TIF'

    def update(self):
        if held_keys['d']:
            self.x += time.dt
            self.rotation_z += 1
            camera.rotation_y += 10 * time.dt
        if held_keys['a']:
            self.x -= time.dt
            self.rotation_z -= 1
            camera.rotation_y -= 10 * time.dt
        if held_keys['w']:
            self.z += time.dt
            camera.z += time.dt
        if held_keys['s']:
            self.z -= time.dt
            camera.z -= time.dt
        if held_keys['space']:
            self.y += 0.1
            camera.y += 0.1
        self.y -= 0.02
        camera.y -= 0.02


#sphere = Entity(model="sphere", color=color.yellow, position=(10, 5, 5))
bird = Bird()
for i in range(5):
   Plane(origin=(uniform(-6, 6), uniform(-20, 20)), speed=uniform(0.10,2))

score = Text(text='0', y=.43, x=-.75, scale=1.5, origin=(0, 0), background=True)

app.run()
