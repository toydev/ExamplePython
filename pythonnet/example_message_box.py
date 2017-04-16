#!/usr/bin/env python

import clr
clr.AddReference(r"wpf\PresentationFramework")
from System.Windows import MessageBox

MessageBox.Show("Hello World")
