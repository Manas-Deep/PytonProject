import pyglet

# Create a window
window = pyglet.window.Window(width=800, height=600, caption='Pyglet Example')

@window.event
def on_draw():
    window.clear()  # Clear the screen (fill with the default color)
    
    # You can draw additional graphics or images here
    # For example, you could draw a white rectangle in the center of the window
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ('v2i', (300, 200, 500, 200, 500, 400, 300, 400)),  # Vertex coordinates
        ('c3B', (255, 255, 255) * 4)  # RGB color values (white)
    )

# Start the application
pyglet.app.run()
