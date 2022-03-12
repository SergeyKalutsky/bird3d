from ursina import *
from random import uniform

if __name__ == '__main__':
    app = Ursina()
go = False

class Plane(Entity):
    def __init__(self, origin, speed):
        super().__init__(model='assets/plane2', origin=origin, collider='box')
        self.texture = 'plane/Diffuse'
        self.rotation_y = 180
        self.rotation_x += 7
        self.speed = speed
        self.elapsed_time = 0

    def update(self):
        self.elapsed_time += time.dt
        global go
        if not go:
            if self.elapsed_time >= 5:
                self.speed += 1
                self.elapsed_time = 0
                print(self.speed)
            self.z -= self.speed
            if bird.x > self.x:
                self.x += 0.2
            else:
                self.x -= 0.2
            if bird.y > self.y:
                self.y += 0.2
            else:
                self.y -= 0.2
            if self.z <= -150:
                score.text = str(int(score.text) + 1)
                self.z = 100
                self.x = uniform(-6, 6)
                self.y = uniform(-20, 20)



class Bird(Entity):
    def __init__(self):
        super().__init__(model='assets/HUMBIRD', origin=(0, 0.05, -0.5),
                         parent=camera, scale=16, collider='box')
        self.texture = 'HUMBIRD.JPG'
        self.texture = 'HUMBIRD.TIF'

    def update(self):
        global go
        info = self.intersects()
        if info.hit:
            go = True
            Text(text='GAME OVER', y=0, x=0, scale=1.5,
             origin=(0, 0), background=True)
            for game_object in game_objects:
                 game_object.enabled = False
        if not go:
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


game_objects = []
bird = Bird()
game_objects.append(bird)
for i in range(10):
    game_objects.append(Plane(origin=(uniform(-6, 6), uniform(-20, 20), 50), speed=1))

score = Text(text='0', y=.43, x=-.75, scale=1.5,
             origin=(0, 0), background=True)
game_objects.append(score)
game_objects.append(Sky(texture='surroundings/wp2894323.jpg'))


if __name__ == '__main__':
    app.run()
