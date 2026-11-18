import flet as ft
from SideBar import SideBar
from datetime import datetime

def main(page: ft.Page):
  # page.theme=ft.ThemeMode.LIGHT,
  today = datetime.now().strftime("%d/%m/%y, %H%M%S")


  page.add(
    ft.SafeArea(
      expand=True,
      content=ft.Row(
        spacing=10,
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=[
          SideBar(compact=False,),

          ft.Container(
            expand=True,
            height=page.height,
            width=page.width,
            content=ft.Column(
              controls=[
                ft.Container(
                  padding=ft.Padding.all(10),
                  bgcolor="#1a152e",
                  border=ft.Border(bottom=ft.BorderSide(1, color="#c0c0c0")),

                  content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing = 20,
                    controls=[
                      ft.Icon(icon=ft.Icons.MENU, size=36, color="#a09e9e"),
                      ft.Text("Detction AI Sestem", size=28, weight=ft.FontWeight.BOLD),
                      ft.Button(
                        content=ft.Row(
                          controls=[
                            ft.Icon(icon=ft.Icons.REFRESH_OUTLINED),
                            ft.Text("system online"),
                          ]
                        )
                      ),
                      ft.Text(today),
                      ft.Button(
                        content=
                        ft.Text("Refresh data"),
                      )
                    ]
                  ))

              ]
            ))
        ])
    )
  )


if __name__ == "__main__":
  ft.run(main=main)