import wx


class MainFrame(wx.Frame):
    """Primary application window with menu, status bar, and a simple demo panel."""

    def __init__(self, parent: wx.Window | None, title: str) -> None:
        super().__init__(parent, title=title, size=(640, 420))
        self.SetMinSize((480, 320))

        self._build_menu()
        self._build_content()
        self.CreateStatusBar()
        self.SetStatusText("Ready")

        self.Bind(wx.EVT_CLOSE, self._on_close)

    def _build_menu(self) -> None:
        menu_bar = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, "E&xit\tAlt+F4", "Close the application")
        menu_bar.Append(file_menu, "&File")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "&About…", "About this application")
        menu_bar.Append(help_menu, "&Help")

        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self._on_exit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self._on_about, id=wx.ID_ABOUT)

    def _build_content(self) -> None:
        panel = wx.Panel(self)
        root = wx.BoxSizer(wx.VERTICAL)

        intro = wx.StaticText(
            panel,
            label="This is a wxPython + uv template.\nUse the button below or the menus to explore.",
        )
        intro.Wrap(560)

        self._counter = 0
        self._label = wx.StaticText(panel, label="Button clicks: 0")

        btn = wx.Button(panel, label="Click me")
        btn.Bind(wx.EVT_BUTTON, self._on_click)

        root.Add(intro, 0, wx.ALL | wx.EXPAND, 16)
        root.Add(self._label, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 8)
        root.Add(btn, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 16)

        panel.SetSizer(root)

    def _on_click(self, _event: wx.CommandEvent) -> None:
        self._counter += 1
        self._label.SetLabel(f"Button clicks: {self._counter}")
        self.SetStatusText(f"Clicked {self._counter} time(s)")

    def _on_exit(self, _event: wx.CommandEvent) -> None:
        self.Close()

    def _on_about(self, _event: wx.CommandEvent) -> None:
        wx.MessageBox(
            "wxPython project template\n\n"
            "A starter desktop app using wxPython and uv.\n"
            "https://www.wxpython.org/",
            "About",
            wx.OK | wx.ICON_INFORMATION,
            self,
        )

    def _on_close(self, event: wx.CloseEvent) -> None:
        event.Skip()
