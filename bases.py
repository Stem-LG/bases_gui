#import the base convert function
from converter import convert
#init gtk application
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#load ui file
builder = Gtk.Builder()
builder.add_from_file("bases.glade")

#get objects from ui file
window = builder.get_object("window1")
entry = builder.get_object("entry")
result = builder.get_object("result")
button1 = builder.get_object("btn1")
combo1 = builder.get_object("combo1")
combo2 = builder.get_object("combo2")

#button click action
def btn1_clicked(self):
    #convert and show result
    result.set_text(convert(entry.get_text(),combo1.get_active(),combo2.get_active()))
    

#set button1 onclick event
button1.connect("clicked", btn1_clicked)

#show window
window.show_all()

#exit when window is closed
window.connect("destroy", Gtk.main_quit)

#start gtk main loop
Gtk.main()
