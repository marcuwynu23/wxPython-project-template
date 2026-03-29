import wx

from wx_python_project_template.main_window import MainFrame


def run() -> int:
    """Start the application (convenience wrapper)."""
    return main()


def main() -> int:
    """Create the wx application, show the main window, and run the event loop."""
    app = wx.App(False)
    frame = MainFrame(None, title="wxPython project template")
    frame.Show()
    app.MainLoop()
    return 0
