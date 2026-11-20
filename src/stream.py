import flet as ft
from PIL.ImageOps import expand


class MainStream:

      def __init__(self, *args, **kwargs):
        self.play=True
        self.pause=False
        self.image=ft.Image(
          src="Computervision_banner.jpg",fit=ft.BoxFit.FILL)
      def live(self):
        return ft.Column(
        controls=[
          ft.Row(
            controls=[
              ft.Text("live Camera-1")
            ]
          ),
          ft.Row(controls=[
            self.image
          ]
                 )
        ]
        )
      def buildUi(self):
        return ft.Container(
          col={
            ft.ResponsiveRowBreakpoint.LG:9,
            ft.ResponsiveRowBreakpoint.MD:10},
          content=ft.Row(
          expand=True,
          controls=[
          ft.Container(
            col={
              ft.ResponsiveRowBreakpoint.LG:3,
              ft.ResponsiveRowBreakpoint.MD:2},

            padding=10,
            bgcolor="#414040",
            border_radius=15,
            expand=True,
            content=self.live(),
          ),
        ft.Container(

          expand=True,
                     content=ft.Column(
                       controls=[
                         ft.Text(
                           "Alert Logs", size=24, weight=ft.FontWeight.BOLD
                         )
                       ]
                     )),

        ]))

