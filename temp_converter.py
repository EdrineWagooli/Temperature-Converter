import flet as ft



# App structure and setup
def main(page: ft.Page):
    page.title = "Temperature Converter"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 500
    page.window_height = 600
    page.window_resizable = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # GUI field
    celsius_input = ft.TextField(label="Celsius °C",
                           keyboard_type=ft.KeyboardType.NUMBER,
                           color=ft.Colors.GREEN,
                           border_color=ft.Colors.BLUE_500,border_radius=14,
                           focused_border_color=ft.Colors.BLUE_500,
                           on_change=lambda e: convert_to_celsius(e.control.value)
                           )

    fahrenheit_input = ft.TextField(label="Fahrenheit °F",
                              keyboard_type=ft.KeyboardType.NUMBER,
                              color=ft.Colors.GREEN,
                              border_color=ft.Colors.BLUE_500,border_radius=14,
                              focused_border_color=ft.Colors.BLUE_700,
                              on_change=lambda e: convert_to_fahrenheit(e.control.value)  )

    kelvin_input = ft.TextField(label="Kelvin °K",
                          keyboard_type=ft.KeyboardType.NUMBER,
                          color=ft.Colors.GREEN,
                          border_color=ft.Colors.BLUE_500, border_radius=14,
                          focused_border_color=ft.Colors.BLUE_700,
                          on_change=lambda e: convert_to_kelvin(e.control.value)
                            )

    #App functionality
    def convert_to_celsius(value):
        if value and value.strip():
            try:
                celsius = float(value)
                fahrenheit = (celsius * 9 / 5)+ 32
                kelvin = celsius + 273.15

                fahrenheit_input.value = f"{fahrenheit:,.2f}"
                kelvin_input.value = f"{kelvin:,.2f}"
                page.update()
            except ValueError:
                fahrenheit_input.value = f"Math Error"
                kelvin_input.value = f"Math Error"


    def convert_to_fahrenheit(value):
        if value and value.strip():
            try:
                fahrenheit= float(value)
                celsius = (fahrenheit - 32) * 5 / 9
                kelvin = celsius + 273.15

                celsius_input.value = f"{celsius:,.2f}"
                kelvin_input.value = f"{kelvin:,.2f}"
                page.update()
            except ValueError:
                celsius_input.value = f"Math Error"
                kelvin_input.value = f"Math Error"


    def convert_to_kelvin(value):
        if value and value.strip():
            try:
                kelvin= float(value)
                celsius = kelvin - 273.15
                fahrenheit = (celsius * 9 / 5) + 32


                celsius_input.value = f"{celsius:,.2f}"
                fahrenheit_input.value = f"{fahrenheit:,.2f}"
                page.update()
            except ValueError:
                celsius_input.value = f"Math Error"
                fahrenheit_input.value = f" Math Error"


    def clear_all(e):
        celsius_input.value = ""
        fahrenheit_input.value = ""
        kelvin_input.value = ""
        page.update()


    #main UI --> containers

    page.add(
        ft.Column([
            ft.Text("Temperature Converter",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.BLUE_700,
                    ),
            ft.Divider(height=20),
            celsius_input,
            ft.Divider(color=ft.Colors.WHITE),
            fahrenheit_input,
            ft.Divider(color=ft.Colors.WHITE),
            kelvin_input,
            ft.Divider(color=ft.Colors.WHITE),

            ft.Button('Clear All', icon=ft.Icons.CLEAR,
                      on_click=clear_all,
                      style=ft.ButtonStyle(
                          bgcolor=ft.Colors.RED_400,
                          color=ft.Colors.WHITE,
                      )),
            ft.Divider(),
            ft.Container(
                content=ft.Column([
                 ft.Text("CONVERSION FORMULAS: ", weight=ft.FontWeight.BOLD,),
                    ft.Text("Celsius to Fahrenheit:  F = (C * 9/5) + 32"),
                    ft.Text("Fahrenheit to Celsius:  C = (C - 32) * 5/9"),
                    ft.Text("Celsius to Kelvin:      K = C + 273.15"),
                ],spacing=5
                ),
                padding=15,
                bgcolor=ft.Colors.GREY_400,
                border_radius = 10,
            )

        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=0,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),




    )


# Run the App
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP_WEB)
