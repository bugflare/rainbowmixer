import flet as ft

def main(page):
    page.title = "rainbow Mixer"
    page.padding = 20
    
    red = ft.Slider(min=0, max=255, value=255, label="Red")
    green = ft.Slider(min=0, max=255, value=255, label="Green")
    blue = ft.Slider(min=0, max=255, value=255, label="Blue")
    
    color_text = ft.Text("RGB: 255, 255, 255", size=20)
    
    def slider_moved(e):
        r = int(red.value)
        g = int(green.value)
        b = int(blue.value)
        
        page.bgcolor = f"#{r:02x}{g:02x}{b:02x}"
        
        color_text.value = f"RGB: {r}, {g}, {b}"
        page.update()
    
    red.on_change = slider_moved
    green.on_change = slider_moved
    blue.on_change = slider_moved
    
    page.add(
        ft.Text("Mix the colors", size=24),
        red,
        green,
        blue,
        color_text
    )
    
    page.bgcolor = "#ffffff"
    page.update()

ft.app(target=main)