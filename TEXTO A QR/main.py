import flet as ft
import qrcode
import os

def main(page: ft.Page):
    
    def btn_click(event):
        qr_code = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr_code.add_data(text.value)
        image_name = name.value + ".png"
        image_qr = qr_code.make_image(fill_color="black",
                                      back_color="white")
        image_qr.save(image_name)

        image_col.controls.append(ft.Image(src=image_name,
                                           width=400,
                                           height=400,
                                           fit=ft.ImageFit.CONTAIN,
                                           ))
        page.update()

    text = ft.TextField(label="texto a convertir")
    name = ft.TextField(label="Nombre imagen QR")
    button = ft.ElevatedButton("Generar")
    image_col = ft.Column(expand=1, wrap=False, scroll='AUTO')
    
    logo_path = os.path.join(os.path.dirname(__file__), "MyLogo.png")
    logo_image = ft.Image(src=logo_path, 
                          width=100, 
                          height=100, 
                          fit=ft.ImageFit.CONTAIN)

    button.on_click = btn_click

    page.add(text,
             name,
             button,
             image_col,
             logo_image)

ft.app(target=main)