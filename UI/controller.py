import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selected_aeroportoA = None
        self._selected_aeroportoP = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        minimo = self._view.txtInCompagnie.value
        try:
            minimo = int(minimo)
        except ValueError:
            self._view.txt_result.create_alert("Inserisci un valore numerico nel campo: '# compagnie minimo'")
            self._view.update_page()
            return
        grafo = self._model.buildGraph(minimo)
        if grafo:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente"))
            self._view.txt_result.controls.append(ft.Text(f"{self._model.printGraphDetails()}"))
            self.fillDDAeroportoPartenza()
            self._view._btnConnessi.disabled = False
            self.fillDDAeroportoArrivo()
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Errore nella creazione del grafo"))
            self._view.update_page()
            return

    def handleConnessi(self, e):
        origine = self._selected_aeroportoP
        if origine is None:
            self._view.txt_result.controls.append(ft.Text("Seleziona un aeroporto di partenza!"))
        else:
            vicini = self._model.getVicini(origine)
            self._view.txt_result.controls.append(ft.Text(f"Ecco i vicini di {origine}:"))
            for v in vicini:
                self._view.txt_result.controls.append(ft.Text(f"{v[1]} - {v[0]}"))
        self._view.update_page()

    def handleCercaItinerario(self, e):
        pass

    def fillDDAeroportoPartenza(self):
        nodi = self._model.getNodes()
        for n in nodi:
            self._view.ddAeroportoP.options.append(ft.dropdown.Option(text=n.AIRPORT, data=n, on_click=self.readDDAeroportoPartenza))
        self._view.update_page()

    def readDDAeroportoPartenza(self, e):
        if e.control.data is None:
            self._selected_aeroportoP = None
        else:
            self._selected_aeroportoP = e.control.data
        print(self._selected_aeroportoP)

    def fillDDAeroportoArrivo(self):
        nodi = self._model.getNodes()
        for n in nodi:
            self._view.ddAeroportoD.options.append(ft.dropdown.Option(text=n.AIRPORT, data=n, on_click=self.readDDAeroportoArrivo))
        self._view.update_page()

    def readDDAeroportoArrivo(self, e):
        if e.control.data is None:
            self._selected_aeroportoA = None
        else:
            self._selected_aeroportoA = e.control.data
