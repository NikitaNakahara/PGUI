from pgui.View import View

class Layout:
    def __init__(self):
        self.views = []

    def addView(self, view: View):
        self.views.append(view)

    def draw(self):
        for view in self.views:
            view.draw()

    