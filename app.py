"""This module initialises and runs the stats tests app.

The app is initialised using the App class which links together a
frontend (GUI) and backend (Server). This is done by calling link functions
in the GUI and Server modules.
"""

from gui import GUI
from server import Server


class App:
    """An app that combines a frontend (GUI) and backend (server)."""

    def __init__(self):
        """Initialise the GUI and sever, and links them."""
        self.gui = GUI()
        self.server = Server()
        self.link_parts()

    def link_parts(self):
        self.server.link_with_gui(self.gui)
        self.gui.link_with_server(self.server)


def main():
    app = App()
    app.gui.run()


if __name__ == "__main__":
    main()