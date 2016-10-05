from visual import *

################################################################################

# Jhon Cory
# The original purpose of this program was to create a model of the solar system.
# However, I modified the program slightly to create something new!


################################################################################
################################################################################

# Create axes
x = box(pos=(0,0,0,), size=(10000,10,10), color=color.blue)
y = box(pos=(0,0,0,), size=(10,10000,10), color=color.blue)
z = box(pos=(0,0,0,), size=(10,10,10000), color=color.blue)

# Create planets
Sun = sphere(pos=(0,0,0), radius=696, color=color.yellow)
Mercury = sphere(pos=(2000,0,0), radius=25, color=color.orange)
Venus = sphere(pos=(3736,0,0), radius=61, color=color.yellow)
Earth = sphere(pos=(5168,0,0), radius=64, color=color.cyan)
Mars = sphere(pos=(7873,0,0), radius=34, color=color.red)
Extra2 = sphere(pos=(8000,0,0), radius=88, color=color.white)

# Initialize time variables
t = 0
dt = 0.05

# Leaving a trail
Mercury.trail = curve(color=Mercury.color)
Venus.trail = curve(color=Venus.color)
Earth.trail = curve(color=Earth.color)
Mars.trail = curve(color=Mars.color)
Extra2.trail = curve(color=Extra2.color)

# Cause movement
while t>-1:
    # Set rate of while loop
    rate(100)
    
    # Cause planets to move in ellipses
    Mercury.pos.x = 2000*cos(0.25*t)
    Mercury.pos.y = 1750*sin(0.23*t)
    Mercury.pos.z = 1500*sin(0.25*t)
    
    Venus.pos.x = 3736*cos(0.42*t)
    Venus.pos.y = 1839*sin(0.46*t)
    Venus.pos.z = 2300*sin(0.42*t)

    Earth.pos.x = 5168*cos(0.28*t)
    Earth.pos.y = 4399*sin(0.38*t)
    Earth.pos.z = 3500*sin(0.28*t)
    
    Mars.pos.x = 7873*cos(0.2*t)
    Mars.pos.y = 3023*sin(0.2347*t)
    Mars.pos.z = 5000*sin(0.2*t)

    Extra2.pos.x = 5500*cos(0.40*t)
    Extra2.pos.y = 6000*sin(0.50*t)
    Extra2.pos.z = 5500*sin(0.40*t)

    # Updating trail curves
    Mercury.trail.append(pos=Mercury.pos)
    Venus.trail.append(pos=Venus.pos)
    Earth.trail.append(pos=Earth.pos)
    Mars.trail.append(pos=Mars.pos)
    Extra2.trail.append(pos=Extra2.pos)
    
    # Update time value
    t = t + dt



