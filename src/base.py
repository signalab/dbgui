#!/usr/bin/env/ python
# http://www.pygtk.org/pygtk2tutorial/sec-SteppingThroughHelloWorld.html


import pygtk
pygtk.require('2.0')
import gtk


class Base(object):
    """docstring for Base."""
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect ("delete_event", self.close_signal)
        self.window.connect ("destroy", self.destroy)
        self.window.set_border_width (15)

        self.hello_button = gtk.Button ("Hello World!")
        self.hello_button.connect ("clicked", self.hello, None)

        self.hello_button.connect_object ("clicked", gtk.Widget.destroy, self.window)
        self.window.connect ("focus_in_event", self.enter_event)

        self.window.add (self.hello_button)
        self.hello_button.show ()
        self.window.show ()

    def hello(self, widget, data=None):
        print "Hello World!"

    def close_signal(self, widget, event, data=None):
        # If true is returned, the main window will not be destroyed
        return False

    def enter_event(self, widget, event, data=None):
        print "Hello!"

    def destroy(self, widget, data=None):
        gtk.main_quit ()

    # Main
    def main(self):
        gtk.main()



print __name__
if __name__ == "__main__":
    base = Base()
    base.main()
