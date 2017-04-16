#!/usr/bin/env python

import clr
clr.AddReference(r"wpf\PresentationFramework")
from System.Drawing import Icon, SystemIcons
from System.Windows import Application
from System.Windows.Forms import ContextMenu, NotifyIcon
from System.Threading import Thread, ThreadStart, ApartmentState

icon = NotifyIcon()

def application_main():
    global icon

    icon = NotifyIcon()
    icon.Text = "Hello World"
    icon.Icon = Icon(SystemIcons.Application, 40, 40);
    icon.Visible = True

    Application().Run()

try:
    thread = Thread(ThreadStart(application_main))
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()

    input()
finally:
    if icon is not None: icon.Dispose()
    if thread is not None: thread.Interrupt()
