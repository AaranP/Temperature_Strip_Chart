import numpy as np
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math

xsize=150


# configure the serial portpi
ser = serial.Serial(
 port='/dev/cu.usbserial-D308HR8X',
 baudrate=115200,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_TWO,
 bytesize=serial.EIGHTBITS
)

ser.isOpen()
   
def data_gen():
    t = data_gen.t
    while True:
       t+=1
       strin = ser.readline()
       a= (strin.decode('utf-8'))
       val= float(a)
       yield t, val

def run(data):
    # update the data
    t,y = data
    if t>-1:
        xdata.append(t)
        ydata.append(y)
        if t>xsize: # Scroll to the left.
            ax.set_xlim(t-xsize, t)
        line.set_data(xdata, ydata)

    return line,

def on_close_figure(event):
    sys.exit(0)

data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=2)
ax.set_ylim(20, 35)
ax.set_xlim(0, xsize)
ax.set_xlabel("Time [S]")
ax.set_ylabel("Temperature [C]")
ax.grid()
xdata, ydata = [], []

# Important: Although blit=True makes graphing faster, we need blit=False to prevent
# spurious lines to appear when resizing the stripchart.
ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=50, repeat=False)
plt.show()
