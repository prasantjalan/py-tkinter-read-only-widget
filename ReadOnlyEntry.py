
from Tkinter import Frame, Entry, Tk, Scrollbar, Text
from Tkconstants import *
# for demo
from Tkinter import Button, LabelFrame


class ReadOnlyEntry(Frame):
    def __init__(self, master, withFocus = True):
        '''
        withFocus -> enabled
            User can set the widget to focus, but the widget will not update
            while it has user focus (even programatically it cannot be updated)

        withFocus -> disabled
            User cannot set focus on the Entry widget. The moment it gets focus,
            focus is shifted to a dummy Frame.
            Widget can be updated programatically anytime.

        Note: in both cases the widget is readonly
        '''
        Frame.__init__(self, master)
        self.master = master
        self.withFocus = withFocus

        self.hasFocus = False
        vcmd = (self.master.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.readOnlyEntry = Entry(self, justify=CENTER, validate="all", validatecommand=vcmd, width=50)
        self.readOnlyEntry.grid(row=0, column=0)
        self.dummyFrame = Frame(self)
        self.dummyFrame.grid(row=0, column=1)

    def onValidate(self, d, i, P, s, S, v, V, W):
        """
        If withFocus is True, then do not accept keyboard inputs
        If withFocus is False, set focus to the dummy Frame that is not visible
        """
        if self.withFocus == True:
            if V == "focusin":
                self.hasFocus = True
            elif V == "focusout":
                self.hasFocus = False

            if self.hasFocus == False and V == "key":
                    return True
            else:
                return False
        else:
            if V == "focusin":
                self.dummyFrame.focus_set()
            return True


    def configure(self, **kwargs):
        self.readOnlyEntry.configure(**kwargs)

    def config(self, **kwargs):
        self.configure(**kwargs)

    def get(self):
        return self.readOnlyEntry.get()

    def set(self, text):
        self.readOnlyEntry.delete(0, END)
        self.readOnlyEntry.insert(0, text)

class ReadOnlyEntryDemo(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)

        self.entryFrame = LabelFrame(self, text="Enter Text and press Button : ")
        self.entryFrame.grid(row=0, column=0, pady=10)
        self.userInputEntry = Entry(self.entryFrame, width=50)
        self.userInputEntry.grid(row=0, column=0)
        self.setButton = Button(self.entryFrame, text="Set Text", command=self.setText)
        self.setButton.grid(row=1, column=0)

        self.withFocusFrame = LabelFrame(self, text="Readonly Widget: With Focus example (Try typing in this widget)")
        self.withFocusFrame.grid(row=1, column=0, pady=10)
        self.readOnlyFocus = ReadOnlyEntry(self.withFocusFrame, withFocus=True)
        self.readOnlyFocus.grid(row=0, column=0)

        self.withoutFocusFrame = LabelFrame(self, text="Readonly Widget: Without Focus example (Try typing in this widget)")
        self.withoutFocusFrame.grid(row=2, column=0, pady=10)
        self.readOnlyNoFocus = ReadOnlyEntry(self.withoutFocusFrame, withFocus=False)
        self.readOnlyNoFocus.grid(row=0, column=0)


    def setText(self):
        self.readOnlyFocus.set(self.userInputEntry.get())
        self.readOnlyNoFocus.set(self.userInputEntry.get())

if __name__ == "__main__":
    root = Tk()
    root.title("Read Only Entry Demo")
    ro = ReadOnlyEntryDemo(root)
    ro.grid(row=0, column=0)
    root.mainloop()
