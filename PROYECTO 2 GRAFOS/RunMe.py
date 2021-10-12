from gl import Raytracer, V3
from obj import *
from figures import *

# Dimensiones 1024x512
width = 1024
height = 512

# Mats
wood = Material(diffuse = (0.6,0.2,0.2), spec = 64)
stone = Material(diffuse = (0.4,0.4,0.4), spec = 64)

gold = Material(diffuse = (1, 0.8, 0 ),spec = 32, matType = REFLECTIVE)
mirror = Material(spec = 128, matType = REFLECTIVE)

water = Material(spec = 64, ior = 1.33, matType = TRANSPARENT)
glass = Material(spec = 64, ior = 1.5, matType = TRANSPARENT)
diamond = Material(spec = 64, ior = 2.417, matType = TRANSPARENT)

tierra = Material(texture = Texture('tierra.bmp'))
cafe = Material(texture = Texture('cafe.bmp'))


# ENVMAP y Pantalla
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('hill1.bmp')

# uces
rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))

#Esferas
rtx.scene.append(Sphere(V3(0,3,-8),0.6, tierra) )
rtx.scene.append(Sphere(V3(0,1,-8), 0.6, cafe) )
rtx.scene.append(Sphere(V3(0,-1,-8), 0.6, glass) )
rtx.scene.append(Sphere(V3(0,-3,-8), 0.6, gold) )
rtx.scene.append(Sphere(V3(-2,0,-8), 0.6, stone) )


#CUBOS
rtx.scene.append(AABB(V3(-6,3,-8), V3(1,1,1),wood))
rtx.scene.append(AABB(V3(-6,1,-8), V3(1,1,1),mirror))
rtx.scene.append(AABB(V3(-6,-1,-8), V3(1,1,1),cafe))
rtx.scene.append(AABB(V3(-6,-3,-8), V3(1,1,1),diamond))
rtx.scene.append(AABB(V3(-8,0,-8), V3(1,1,1),stone))


#HoverBoard
rtx.scene.append(AABB(V3(6,3,-8.1), V3(1.7,0.6,0.6),gold))
rtx.scene.append(Sphere(V3(4.8,3,-8),0.5, gold) )
rtx.scene.append(Sphere(V3(7.1,3,-8),0.5, gold) )

rtx.scene.append(AABB(V3(6,1,-8.1), V3(1.7,0.6,0.6),stone))
rtx.scene.append(Sphere(V3(4.8,1,-8),0.5, stone) )
rtx.scene.append(Sphere(V3(7.1,1,-8),0.5, stone) )

rtx.scene.append(AABB(V3(6,-1,-8.1), V3(1.7,0.6,0.6),wood))
rtx.scene.append(Sphere(V3(4.8,-1,-8),0.5, wood) )
rtx.scene.append(Sphere(V3(7.1,-1,-8),0.5, wood) )

rtx.scene.append(AABB(V3(6,-3,-8.1), V3(1.7,0.6,0.6),cafe))
rtx.scene.append(Sphere(V3(4.8,-3,-8),0.5, cafe) )
rtx.scene.append(Sphere(V3(7.1,-3,-8),0.5, cafe) )

rtx.scene.append(AABB(V3(4,0,-8.1), V3(1.7,0.6,0.6),cafe))
rtx.scene.append(Sphere(V3(2.8,0,-8),0.5, cafe) )
rtx.scene.append(Sphere(V3(5.1,0,-8),0.5, cafe) )

# Imprimir
rtx.glRender()
rtx.glFinish('salida.bmp')



