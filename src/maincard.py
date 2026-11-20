import flet as ft
from flet import controls


class MainCard(ft.Container ):

 def __init__(self,):
  super().__init__(content=self.buildContent())

 def card(self, count, description):
  return ft.Card(
   col={
       ft.ResponsiveRowBreakpoint.LG:3,
       ft.ResponsiveRowBreakpoint.MD:4,
       ft.ResponsiveRowBreakpoint.XS:12,
   },
   content=ft.Container(
    padding=15,
    content=ft.Column(
     controls=[
            ft.Text(description, size=18),
            ft.Text(str(count), size=24, weight=ft.FontWeight.BOLD),
       ]
     ),
    ),
  )



 def buildContent(self):
  items=[(4,"Total Camera"),
         (3, "Active Camera"),
         (4,"Alerts Today"),
         (124,"Total Detection"),
  ]
  return ft.ResponsiveRow(controls=[
   *([self.card(count, label) for count, label in items])])
