from pgui.Layout import Layout

from bs4 import BeautifulSoup

class PgUI:
    def __init__(self, pg):
        self.pg = pg
        self.layouts = []

    def addLayout(self, layout: Layout):
        self.layouts.append(layout)

    def draw(self):
        for layout in self.layouts:
            layout.draw()