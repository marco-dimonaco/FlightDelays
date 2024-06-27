import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._btnAnalizza = None
        self.txtInCompagnie = None
        self._txtDescrizioneCompagnie = None
        self._btnConnessi = None
        self.ddAeroportoP = None
        self._txtDescrizioneAPart = None
        self.ddAeroportoD = None
        self._txtDescrizioneADest = None
        self._btnCercaItinerario = None
        self.txtInTratte = None
        self._txtDescrizioneTratte = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 02-07-2018 TURNO C", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 1
        self._txtDescrizioneCompagnie = ft.Text("# compagnie minimo", width=200)
        self.txtInCompagnie = ft.TextField(width=300)
        self._btnAnalizza = ft.ElevatedButton(text="Analizza aeroporti", on_click=self._controller.handleAnalizza)
        row1 = ft.Row([self._txtDescrizioneCompagnie, self.txtInCompagnie, self._btnAnalizza],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW 2
        self._txtDescrizioneAPart = ft.Text("Aeroporto di partenza", width=200)
        self.ddAeroportoP = ft.Dropdown(label="Aeroporto di Partenza", width=300, on_change=self._controller.readDDAeroportoPartenza)
        self._btnConnessi = ft.ElevatedButton(text="Aeroporti connessi", on_click=self._controller.handleConnessi,
                                              disabled=True)
        row2 = ft.Row([self._txtDescrizioneAPart, self.ddAeroportoP, self._btnConnessi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW 3
        self._txtDescrizioneADest = ft.Text("Aeroporto di destinazione", width=200)
        self.ddAeroportoD = ft.Dropdown(label="Aeroporto di Destinazione", width=300, on_change=self._controller.readDDAeroportoArrivo)
        row3 = ft.Row([self._txtDescrizioneADest, self.ddAeroportoD],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW 4
        self._txtDescrizioneTratte = ft.Text("Numero di tratte massimo", width=200)
        self.txtInTratte = ft.TextField(width=300)
        self._btnCercaItinerario = ft.ElevatedButton(text="Cerca itinerario", on_click=self._controller.handleCercaItinerario)
        row4 = ft.Row([self._txtDescrizioneTratte, self.txtInTratte, self._btnCercaItinerario],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()