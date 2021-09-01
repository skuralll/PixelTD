class UIManager:

    uis = {}

    @staticmethod
    def update():
        for ui in UIManager.uis.values():
            ui.update()

    @staticmethod
    def draw():
        for ui in UIManager.uis.values():
            ui.draw()

    @staticmethod
    def addUI(ui):
        UIManager.uis[ui.UI_ID] = ui

    @staticmethod
    def delUI(uiid):
        del UIManager.uis[uiid]
