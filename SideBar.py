import flet as ft
from PIL.ImageOps import expand
from rich import padding


class SideBar(ft.Container):
  def __init__(self, compact=True, pg=ft.Page):

    super().__init__(bgcolor="#191325",
          width=76 if compact else 220
          ,content=self.buildContent(),max_width=220)
  def navItem(self, icon, label, link):
    return ft.Container(
         padding=10,
         content=ft.Row(
         spacing=12,
         controls=[
           ft.Icon(icon=icon,size=20, color="#faf6f6"),
           ft.Text(label, size=18, color="#faf6f6")
         ]
       )
    )
  def buildContent(self):
    menuItems=[(ft.Icons.DASHBOARD,"Dashboard","/"),
              (ft.Icons.LIST,"Detection","/"),
              (ft.Icons.ALARM,"Alert","/"),
              (ft.Icons.CAMERA_OUTDOOR,"Live Stream","/"),
              (ft.Icons.SETTINGS,"Setting","/"),
              (ft.Icons.LOGOUT,"Log Out","/"),]
    return ft.Column(
        controls=[
          ft.Container(
              # alignment=ft.MainAxisAlignment.CENTER,

            content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
              controls=[
                ft.Image(src="icon.svg", height=80, width=40),
                ft.Text("Sahand Detector" , size=22,weight=ft.FontWeight.BOLD, color="#EDEAE0")
              ]            )
          )
        ,
        *([self.navItem(icon, label, link) for (icon, label, link) in menuItems])
        ]
    )
