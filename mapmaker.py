''' !dependencies!

sudo apt-get install python3-tk
sudo apt-get install python3-pil.imagetk (or pip install pillow)
pip3 instal lxml

'''

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import xmlput
import obj, objectList
import popups
from copy import deepcopy

activeObjects = []
locationRatio = 50/(60*5)

class Window(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self,parent)
        #tk.Tk.iconbitmap(self, default = '@/home/long/Desktop/WMWMapCreator/assets/logo.xbm')
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=90*5, height=120*5)
        self.initialize()
        self.title('WMW Map Creator')
        self.geometry('%dx%d' % (760 , 610) )

        
    def initialize(self):
        self.grid()
    
        self.canvas.grid(row=0, column=1, rowspan = 999)
        self.openIMG('blank.png')
        
        self.canvas.tag_bind('object', '<ButtonPress-1>', self.on_press)
        self.canvas.tag_bind('bg', '<ButtonPress-1>', self.destroyTweaks)
        self.canvas.tag_bind('object', '<ButtonRelease-1>', self.on_obj_release)
        self.canvas.tag_bind('object', '<B1-Motion>', self.on_obj_motion)
        #self.bind('<Motion>', self.xy)
        
        # this data is used to keep track of an item being dragged
        self._drag_data = {'x': 0, 'y': 0, 'item': None}

        
        # button
        buttonBox = ttk.LabelFrame(self, text='Toolbox')
        buttonBox.grid(row=1, column=0, rowspan = 99, sticky = 'N')
        ttk.Button(buttonBox, text='Add', command = addObj).pack()
        ttk.Button(buttonBox, text='Copy', command = popups.commingsoon).pack()
        ttk.Button(buttonBox, text='Paste', command = popups.commingsoon).pack()
        ttk.Button(buttonBox, text='MultiSeclect', command = popups.commingsoon).pack()
        ttk.Button(buttonBox, text='Seclect All', command = popups.commingsoon).pack()
        ttk.Button(buttonBox, text='Undo', command = popups.commingsoon).pack()
        ttk.Button(buttonBox, text='Redo', command = popups.commingsoon).pack()
        
        # obj prop tweak
        ttk.Label(self, text='OBJECT PROPERTIES').grid(row=0, column=3)
        #ttk.Button(self, text='Apply', command = popups.applyCommingsoon).grid(row=99, column=3)
        
        # menu bar
        bar = tk.Menu(self)
        
        self.config(menu=bar)
        
        fileMenu = tk.Menu(bar)
        
        fileMenu.add_command(label= 'Open', command = openfile)
        fileMenu.add_command(label= 'Export XML', command = export)
        fileMenu.add_command(label= 'Close Img', command = lambda: self.openIMG('assets/WMWmap.png'))
        fileMenu.add_separator()
        fileMenu.add_command(label= 'Exit', command = self.client_exit)
        bar.add_cascade(label= 'File', menu=fileMenu)
        
        edit = tk.Menu(bar)
        edit.add_command(label= 'Copy', command = popups.commingsoon)
        edit.add_command(label= 'Paste', command = popups.commingsoon)
        #bar.add_cascade(label= 'Edit', menu=edit)
        
        help = tk.Menu(bar)
        help.add_command(label= 'View help.txt')
        help.add_command(label= 'About', command = popups.about_dialog)
        bar.add_cascade(label= 'Help', menu=help)
        
        
        self.tweakList = []
        
        self.spriteList = [] # this has 100% colleration with 'activeObjects' list
        self.imgref = []
        
        self.snapshots = []
        self.objSpawned = 0
        
    def spawn_tweak(self, laObj , canvas):
        i=1
        for prop, value in laObj.props.items():
            if prop == 'name':
                description = 'Reference'
                lb = ttk.LabelFrame(self, text=description)
                lb.grid(row=i, column=3)
                self.tweakList.append(lb)
                ttk.Label(lb, text='Name').grid(row=0, column=0, sticky = 'W')
                ent = ttk.Entry(lb)
                ent.insert('end', value)
                ent.grid(row=1, column=0)
            
            elif prop == 'location':
                description =  'Location'
                lb = ttk.LabelFrame(self, text=description)
                lb.grid(row=i, column=3)
                self.tweakList.append(lb)
                
                ttk.Label(lb, text='X: ').grid(row=0, column=0)
                ent = ttk.Entry(lb, width=10)
                ent.grid(row=0, column=1)
                ent.insert('end', value[0])
                ttk.Label(lb, text='Y: ').grid(row=1, column=0)
                ent = ttk.Entry(lb, width=10)
                ent.grid(row=1, column=1)
                ent.insert('end', value[1])
                
            elif prop == 'angle':
                description =  'Angle'
                lb = ttk.LabelFrame(self, text=description)
                lb.grid(row=i, column=3)
                self.tweakList.append(lb)
                
                angleKnob = tk.Scale(lb, from_=0, to=360, orient='horizontal', length=175, sliderlength=15, command=lambda x:self.rotate(laObj,canvas,angle=x) )
                angleKnob.set(value)
                angleKnob.grid(row=0, column=0)
            
            elif prop == 'intput':
                lb = ttk.LabelFrame(self)
                lb.grid(row=i, column=3)
                self.tweakList.append(lb)
                
                
            else:
                i -=1
                
            i+=1
        
        lb = ttk.LabelFrame(self)
        lb.grid(row=i, column=3)
        self.tweakList.append(lb)
        #ttk.Button(lb, text='Appply', command = ).pack()
        ttk.Button(lb, text='Remove', command = lambda:self.rmObject(laObj) ).pack()
        ttk.Button(lb, text='Duplicate', command = lambda:self.duplicate(laObj) ).pack()
            
    def destroyTweaks(self, meh=None):
        for w in self.tweakList:
            w.destroy()
            
    def client_exit(self):
        exit()
        
    def xy(self, event):
        xm,ym = event.x-300 , event.y-225
        xy_data = 'x=%d  y=%d' % (xm, ym)
        
        lab = ttk.Label(self , text = xy_data)
        lab.grid(row=0, column=0)
        
    
    def openIMG(self, imgfile):
        self.bugfix = imgfile
    
        mapim = Image.open(imgfile)
        mapim = mapim.resize((mapim.size[0]*5,mapim.size[1]*5))
        self.render = ImageTk.PhotoImage(mapim)
        ping = self.canvas.create_image(90*5/2, 120*5/2  , image=self.render, tags='bg')
        self.canvas.tag_lower(ping)
        self.title('%s - WMW Map Creator' %(imgfile))
        
    def rotate(self, leObj,canvas, angle):
        leObj.props['angle'] = angle
        index = activeObjects.index(leObj)
        rotated = Image.open(leObj.props['texture']).rotate(int(angle))
        render = ImageTk.PhotoImage(rotated)
        self.imgref[ index ] = render
        self.canvas.itemconfig(canvas, image = self.imgref[ index ])
        
    def rmObject(self, leObj):
        ind = activeObjects.index(leObj)
        activeObjects.pop(ind)
        self.spriteList.pop(ind)
        self.imgref.pop(ind)
        
    def duplicate(self, leObj):
        ind = activeObjects.index(leObj)
        activeObjects.append( deepcopy(activeObjects[ind]) )
        try:
            activeObjects[ len(activeObjects)-1 ].props["name"]+="-copy"
        except:
            pass

        self.imgref.append( self.imgref[ind] )
        a = self.canvas.create_image(90*5/2, 120*5/2  , image=self.imgref[ len(self.imgref)-1 ], tags='object')
        self.spriteList.append( a )
        
        
    def _create_sprite(self, imgfile):
        img = Image.open(imgfile)
        render = ImageTk.PhotoImage(img)
        self.imgref.append( render )
        a = self.canvas.create_image(90*5/2, 120*5/2  , image=self.imgref[ len(self.imgref)-1 ], tags='object')
        self.spriteList.append(a)        

    def on_press(self, event):
        self._drag_data['item'] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data['x'] = event.x
        self._drag_data['y'] = event.y
        
        self.destroyTweaks()
        self.spawn_tweak( activeObjects[  self.spriteList.index( self._drag_data['item'] )  ] ,canvas=self._drag_data['item'] )
        

    def on_obj_release(self, event):
        xy = self.canvas.coords( self._drag_data['item'] )
        x = "{0:.6f}".format( (xy[0] - 90*5/2)*locationRatio )
        y = "{0:.6f}".format( (xy[1] - 120*5/2)*locationRatio *-1 )
        # a random bug sometimes occur where user can move baccground canvas
        try:
            activeObjects[  self.spriteList.index( self._drag_data['item'] )  ].props['location'] = (x , y)
        except:
            self.openIMG(self.bugfix)
        
        self.destroyTweaks()
        self.spawn_tweak( activeObjects[  self.spriteList.index( self._drag_data['item'] )  ] ,canvas=self._drag_data['item'] )
        
        # reset the drag information
        self._drag_data['item'] = None
        self._drag_data['x'] = 0
        self._drag_data['y'] = 0

    def on_obj_motion(self, event):
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data['x']
        delta_y = event.y - self._drag_data['y']
        # move the object the appropriate amount
        self.canvas.move(self._drag_data['item'], delta_x, delta_y)
        # record the new position
        self._drag_data['x'] = event.x
        self._drag_data['y'] = event.y
    
def addObj():
    def add(Obj):
        created = obj.addObject(Obj, app.objSpawned )
        app.objSpawned+=1
        app._create_sprite( created.props['texture'] )
        activeObjects.append(created)
        popup.destroy()
    
    popup = tk.Tk()
    popup.wm_title('Add Object')
    ttk.Button(popup, text="Swampy's Ducky", command = lambda: add(objectList.Ducky) ).pack()
    ttk.Button(popup, text="Cranky's Ducky", command = lambda: add(objectList.CrankyDucky) ).pack()
    ttk.Button(popup, text="Allie's Ducky", command = lambda: add(objectList.AllieDucky) ).pack()
    ttk.Button(popup, text='Goal', command = lambda: add(objectList.BrokenPipe) ).pack()
    ttk.Button(popup, text='Pipe', command = lambda: add(objectList.Pipe) ).pack()
    ttk.Button(popup, text='Pipe Elbow', command = lambda: add(objectList.PipeElbow) ).pack()
    ttk.Button(popup, text='Long Pipe', command = lambda: add(objectList.PipeLong) ).pack()
    ttk.Button(popup, text='Pipe Elbow 2', command = lambda: add(objectList.PipeElbow2) ).pack()
    ttk.Button(popup, text='Spout', command = lambda: add(objectList.Spout) ).pack()
    ttk.Button(popup, text='Drain', command = lambda: add(objectList.Drain) ).pack()
    ttk.Button(popup, text='Bomb', command = lambda: add(objectList.Bomb) ).pack()
    ttk.Button(popup, text="Swampy's Room", command = lambda: add(objectList.Room) ).pack()
    
    popup.mainloop()
    

def openfile():
    def fetch():
        p = '/home/longn/Desktop/WMWMapCreator/test.png'#path.get()
        if p.strip().lower()[-3:] == 'png':
            app.openIMG(p)
            popup.destroy()
        
    popup = tk.Tk()
    popup.wm_title('Open file')
    path = ttk.Entry(popup, width=75)
    path.grid(row=0, column=1)
    ttk.Label(popup, text='Path to file:').grid(row=0, column=0)
    ttk.Button(popup, text='Open', command = fetch).grid(row=0, column=3)
    ttk.Label(popup, text='Parse in directory to Map image PNG file or Object mapping XML file').grid(row=2, column=0, columnspan = 3)
    popup.mainloop()
    
def export():
    popup = tk.Tk()
    popup.wm_title('Export file')
    ttk.Label(popup, text="Where do you want to put your work? Extension should be .xml").pack()
    ttk.Label(popup, text="Eg.: first_dig.xlm").pack()
    dire = ttk.Entry(popup, width=75)
    dire.pack()
    ttk.Button(popup, text="Export", command = lambda: xmlput.finalBuild(activeObjects, path=dire.get() ) ).pack()
    

if __name__ == '__main__':
    app = Window(None)
    app.mainloop()
