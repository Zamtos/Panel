from tkinter import *
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
import datetime
import ephem
import math
# from datetime import datetime, time, timedelta
from kivy.uix.behaviors import ButtonBehavior

# class Sample(GridLayout):
#     def __init__(self, **kwargs):
#         super(Sample, self).__init__(**kwargs)
#         self.cols = 3
#         self.button = Button(text='przycisk')
#         self.button.bind(state=self.callback)
#         self._clock_label = Label(text=str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#         self.add_widget(self._clock_label)
#         self.add_widget(Label(text='<- Zegar'))
#         self.add_widget(self.button)
#         Clock.schedule_interval(self.updateLabel, 0.5)
#
#     def updateLabel(self, dt):
#         self._clock_label.text = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
#         pass
#
#     def doNothing(self):
#         print('test')
#
#     def callback(self, instance, value):
#         print('The button <%s> state is <%s> ' % (instance, value))
#
# #class Menu():
# #    def __init__(self):
#
#
# class MyApp(App):
#
#    def build(self):
#         return Sample()
#
#
# if __name__ == '__main__':
#     MyApp().run()
#
#
#
# def Sun():
#     sun = ephem.Sun()
#     sun.compute()
#     print sun.ra, sun.dec
#
# mars = ephem.Earth()
# mars.compute()
# print(mars.ra, mars.dec)

import tkinter as tk

class CurrentTimeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="left")

        self.label = tk.Label(self, text=str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        self.label.pack(side="right")

        self.setTime()

    def setTime(self):
        self.label['text'] = str(datetime.datetime.now().strftime("Today is %d-%m-%Y %H:%M:%S"))
        root.after(1000, self.setTime)

    def say_hi(self):
        print("hi there, everyone!")

class ProgramFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="left")
        #
        self.label = tk.Label(self, text=str("R.A.: %s DEC.: %s" % (s.a_ra, s.a_dec)))
        self.label.pack(side="right")

        # self.setTime()
        self.dLocation()

    def dLocation(self):
        s = ephem.Sun()
        s.compute(epoch=ephem.now())
        o = ephem.Observer()
        o.lon, o.lat = '17.03333', '51.100000'  # Współrzędne Wrocławia
        o.date = ephem.now()  # 00:22:07 EDT 06:22:07 UT+1
        s.compute(o)
        hour_angle = o.sidereal_time() - sun.ra
        t = ephem.hours(hour_angle + ephem.hours('12:00')).norm  # .norm for 0..24
        rad = str(ephem.hours(hour_angle + ephem.hours('12:00')).norm)
        # print("R.A.: %s DEC.: %s" % (s.a_ra, s.a_dec))
        # print("HOUR ANGLE: %s SIDERAL TIME: %s" % (rad, o.sidereal_time()))
        # # print("HOUR ANGLE2: %s SIDERAL TIME: %s" % (t, o.sidereal_time()))
        # # print("HOUR ANGLE3: %s SIDERAL TIME: %s" % (hour_angle, o.sidereal_time()))
        # print("SUN Altitude: %s SUN Azimuth: %s" % (sun.alt, sun.az))
        self.label['text'] = str("R.A.: %s DEC.: %s" % (s.a_ra, s.a_dec))
        # self.label['text'] = str("HOUR ANGLE: %s SIDERAL TIME: %s" % (rad, o.sidereal_time()))
        root.after(1000, self.dLocation)

    # def setTime(self):
    #     self.label['text'] = str(datetime.datetime.now().strftime("Today is %d-%m-%Y %H:%M:%S"))
    #     root.after(1000, self.setTime)

    # def say_hi(self):
    #     print("hi there, everyone!")

# class GridLayout(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#
#         self.label1 = Label(self, text="Location:")
#         self.label1.pack()
#         self.label2 = Label(root, text="Longitude:")
#
#         self.label1.grid(row=0, sticky=E)
#         self.label2.grid(row=1, sticky=E)
#
#         self.entry1 = Entry(root)
#         self.entry2 = Entry(root)
#
#         self.entry1.grid = (row=0, column=1)
#         self.entry2.grid = (row=1, column=1)


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the main menu
        self.menu = Menu(self)
        self.createMenu(self.menu)
        master.config(menu=self.menu)

        self.pack()
        self.create_widgets()

    def createMenu(self, menu):
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New", command=New)
        subMenu.add_command(label="Load", command=doNothing)
        subMenu.add_command(label="Start for Default Location", command=dLocation)
        subMenu.add_separator()
        subMenu.add_command(label="Quit Program", command=self.menuQuit)

        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="View Local Parameters", command=doNothing)
        editMenu.add_command(label="Enter Panel Location Coordinates", command=doNothing)
        editMenu.add_command(label="Start for Default Location", command=doNothing)
        editMenu.add_command(label="Start for New Location", command=doNothing)

    def create_widgets(self):
        # self.root = Tk()
        # self.root.title('Panel')
        self.winfo_toplevel().title("SOLAR PANEL Program")
        # this adds something to the frame, otherwise the default
        # size of the window will be very small
        # label = Entry(self)
        # label.pack(side="top", fill="x")
        # self.gridlayout = GridLayout(self)
        # self.gridlayout.pack(side="top")
        # self.default = ProgramFrame(self)
        # self.default(side="left")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="right")

        self.current_time = CurrentTimeFrame(self)
        self.current_time.pack(side="left")


    ### Akcje w menusach

    def menuQuit(self):
        quit()

def dLocation():
    s = ephem.Sun()
    s.compute(epoch=ephem.now())
    print("R.A.: %s DEC.: %s" % (s.a_ra, s.a_dec))
    o = ephem.Observer()
    o.lon, o.lat = '17.03333', '51.100000' # Współrzędne Wrocławia
    o.date = ephem.now()  # 00:22:07 EDT 06:22:07 UT+1
    s.compute(o)
    hour_angle = o.sidereal_time() - sun.ra
    t = ephem.hours(hour_angle + ephem.hours('12:00')).norm  # .norm for 0..24
    rad = str(ephem.hours(hour_angle + ephem.hours('12:00')).norm)
    print("HOUR ANGLE: %s SIDERAL TIME: %s" % (rad, o.sidereal_time()))
    # print("HOUR ANGLE2: %s SIDERAL TIME: %s" % (t, o.sidereal_time()))
    # print("HOUR ANGLE3: %s SIDERAL TIME: %s" % (hour_angle, o.sidereal_time()))
    print("SUN Altitude: %s SUN Azimuth: %s" % (sun.alt, sun.az))
    root.after(1000, dLocation)

def New():
    print('New')


def doNothing():
    print('test')






sun = ephem.Sun()
sun.compute()
print(sun.ra, sun.dec)

s = ephem.Sun()
s.compute(epoch=ephem.now())
print("%s %s" % (s.a_ra, s.a_dec))

s.compute('2017/12/4', epoch='2017/12/4')
print("%s %s" % (s.a_ra, s.a_dec))


# def hour_angle(hUTC, dayofyear, year, longitude):
#     """ Sun hour angle
#
#     Args:
#         hUTC: fractional hour (UTC time)
#         dayofyear (int):
#         year (int):
#         longitude (float): the location longitude (degrees, east positive)
#
#
#     Returns:
#         (float) the hour angle (hour)
#
#     Details:
#         World Meteorological Organization (2006).Guide to meteorological
#         instruments and methods of observation. Geneva, Switzerland.
#     """
#     jd = julian_date(hUTC, dayofyear, year)
#     n = jd - 2451545
#     gmst = numpy.mod(6.697375 + 0.0657098242 * n + hUTC, 24)
#     lmst = numpy.mod(gmst + longitude / 15., 24)
#     ra = right_ascension(hUTC, dayofyear, year)
#     ha = numpy.mod(lmst - ra / 15. + 12, 24) - 12
#     return ha


o = ephem.Observer()
o.lon, o.lat = '17.03333', '51.100000'
o.date = '2017/12/4 05:22:07'  # 00:22:07 EDT 06:22:07 UT+1 !!!!czas ma być podany w UT!!!!
sun = ephem.Sun()
sun.compute(o)
hour_angle = o.sidereal_time() - sun.ra
rad = str(ephem.hours(hour_angle + ephem.hours('24:00')).norm)
print("kat godzinny i czas gwiazdowy %s %s" % (rad, o.sidereal_time()))
print("kat godzinny %s " % (hour_angle))

fifteen_degrees = ephem.degrees(math.pi / 12.)
print('%s %s' % (s.dec, ephem.degrees(s.dec + fifteen_degrees)))
print('kat godzinny? %s %s' % (s.ra, ephem.hours(s.ra + fifteen_degrees)))

# def solarTime(utc_dt, lat, lon):
#     """Compute local solar time for given (lat, lon)
#     """
#     import ephem
#     o = ephem.Observer()
#     o.date = utc_dt
#     o.lat = str(lat)
#     o.lon = str(lon)
#     sun = ephem.Sun()
#     sun.compute(o)
#     hour_angle = o.sidereal_time() - sun.ra
#     rad = str(ephem.hours(hour_angle + ephem.hours('12:00')).norm)
#     t = datetime.strptime(rad, '%H:%M:%S.%f')
#     solar_dt = datetime.combine(utc_dt.date(), t.time())
#     return solar_dt

# j = ephem.Jupiter()
# j.compute(epoch=ephem.now())   # so both date and epoch are now
# print("%s %s" % (j.a_ra, j.a_dec))
#
# j.compute('2003/3/25', epoch='2003/3/25')
# print("%s %s" % (j.a_ra, j.a_dec))


gatech = ephem.Observer()
gatech.lon, gatech.lat = '-84.39733', '33.775867'
gatech.date = '1984/5/30 16:22:56'  # 12:22:56 EDT
sun, moon = ephem.Sun(), ephem.Moon()
sun.compute(gatech)
moon.compute(gatech)
print("%s %s" % (sun.alt, sun.az))
print("%s %s" % (moon.alt, moon.az))

gatech = ephem.Observer()
gatech.lon, gatech.lat = '17.03333', '51.100000'
gatech.date = '2017/12/4 05:22:07'  # 00:22:07 EDT 06:22:07 UT+1
sun, moon = ephem.Sun(), ephem.Moon()
sun.compute(gatech)
moon.compute(gatech)
print("altitude i azymut dla s 2017 %s %s" % (sun.alt, sun.az))
print("%s %s" % (moon.alt, moon.az))

print(ephem.separation((sun.az, sun.alt), (moon.az, moon.alt)))
print("%.8f %.8f %.11f" % (sun.size, moon.size, sun.size - moon.size))

gatech.date = '1984/5/31 00:00'   # 20:00 EDT
sun.compute(gatech)
for i in range(8):
     old_az, old_alt = sun.az, sun.alt
     gatech.date += ephem.minute * 5.
     sun.compute(gatech)
     sep = ephem.separation((old_az, old_alt), (sun.az, sun.alt))
     print("%s %s %s" % (gatech.date, sun.alt, sep))
print(gatech.next_setting(sun))
print("%s %s" % (sun.alt, sun.az))


root = Tk()
app = Application(master=root)
app.mainloop()

# menu = Menu(root)
# root.config(menu=menu)
#
# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New", command=doNothing)
# subMenu.add_command(label="Load", command=doNothing)
# subMenu.add_command(label="Start for Default Location", command=doNothing)
# subMenu.add_separator()
# subMenu.add_command(label="Quit Program", command=Quit)
#
# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="View Local Parameters", command=doNothing)
# editMenu.add_command(label="Enter Panel Location Coordinates", command=doNothing)
# editMenu.add_command(label="Start for Default Location", command=doNothing)
# editMenu.add_command(label="Start for New Location", command=doNothing)
#
# root.mainloop()
