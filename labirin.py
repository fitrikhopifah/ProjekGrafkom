#import library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# LOGIK
# Koordinat x dan y untuk posisi kotak
x_player1 = 120
y_player1 = 130
# hold_player = [[x_player1,y_player1]]

y = 0
kecepatan = 10

hold_grid = []
hold_grid2 = []

# Labirin
level1 = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "W                    W",
    "W           WWWWWW   W",
    "W     WWWW       W   W",
    "W     W        WWWW  W",
    "W  WWWW  WWWW        W",
    "W     W     W   W    W",
    "W     W     W  WWWW  W",
    "W     WWW  WW  W  W  W",
    "W       W   W  W  W  W",
    "WWWWW   W   WWWW  W  W",
    "W   W      WW        W",
    "W   W   WWWW   WWW   W",
    "W       W    E   W   W",
    "WWWWWWWWWWWWWWWWWWWWWW",
]

level = [
  "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
  "W     W        W        W  W  W",
  "W  W  W  WWWW  WWWWWWW  W  W  W",
  "W  W  W     W        W  W     W",
  "W  WWWWWWWWWW  W  WWWW  W  W  W",
  "W              W        W  W  W",
  "W  WW  WWWWWWWWW  WWWWWWW  W  W",
  "W  W   W       W  W        W  W",
  "W  WWWWW   W   W  W  WWWW  W  F",
  "S          W   W  W  W  W  WWWW",
  "WWWWW  W   W   W  W  W  W  W  W",
  "W      W   W   W     W  W  W  W",
  "W  WWWWWWWWW   WWWWWWW  W  W  W",
  "W          W            W     W",
  "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

def labirin(pos,r,b,g):
    glPushMatrix()
    glPointSize(15) #utk mengatur ukuran titiknya
    glBegin(GL_POINTS) #utk memulai pembuatan objek titik
    glColor3ub(r,b,g) #kode warna pake rgb
    glVertex2f(pos[0],pos[1]) #titik koordinat
    glEnd() #utk mengakhiri objek yang dibuat
    glPopMatrix()

def draw_labirin():
    x,y = 120,50
    r,b,g = 66, 207, 160
    for row in level[::-1]:
        for col in row:
            if col == "W":
                labirin((x, y),r,b,g)
                hold_grid.append([x,y])
                hold_grid.append([104,130])
            elif col == "F":
                labirin((x, y),255, 255, 255)
                hold_grid.append([x,y])
            x += 16
        y += 16
        x = 120

def bg_level():
    glPushMatrix()
    glBegin(GL_QUADS) #utk memulai pembuatan objek titik
    glColor3ub(0,0,0) #kode warna pake rgb
    glVertex2f(111,43) #titik koordinat
    glVertex2f(610,43)
    glVertex2f(610,282)
    glVertex2f(111,282)
    glEnd() #utk mengakhiri objek yang dibuat
    glPopMatrix()

def karakter():
    glPushMatrix()
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(255, 136, 0)
    glVertex2f(x_player1,y_player1)
    glEnd()
    glPopMatrix()

# LOGIK
def input_keyboard(key,x,y):
    global x_player1, y_player1
    # Untuk mengubah posisi grid_indeks0 =[]
    grid_x = []
    grid_y = []
    for i in hold_grid:
        grid_x.append(i[0])
        grid_y.append(i[1])
        
    if key == GLUT_KEY_UP: # sama seperti glut_key_up
        try:
            if hold_grid.index([x_player1,y_player1+16]) :
                y_player1 += 0
        except:
            y_player1 += 16
        print("Tombol Atas ditekan ", "x : ", x_player1, " y : ", y_player1)
    elif key == GLUT_KEY_DOWN:
        try:
            if hold_grid.index([x_player1,y_player1-16]) :
                y_player1 += 0
        except:
            y_player1 -= 16
        print("Tombol Bawah ditekan ", "x : ", x_player1, " y : ", y_player1)
    elif key == GLUT_KEY_RIGHT:
        try:
            if hold_grid.index([x_player1+16,y_player1]) :
                x_player1 += 0
        except:
            x_player1 += 16
        print("Tombol Kanan ditekan ", "x : ", x_player1, " y : ", y_player1)
    elif key == GLUT_KEY_LEFT:
        try:
            if hold_grid.index([x_player1-16,y_player1]) :
                x_player1 += 0
        except:
            x_player1 -= 16
        print("Tombol Kiri ditekan ", "x : ", x_player1, " y : ", y_player1)

#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 500) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate()
    bg_level()
    draw_labirin()
    karakter()
    glutSwapBuffers() #utk membersihkan layar, double buffering

def init():
    glClearColor(2,1,0, 2.0)
    # glClearColor(1,4,7, 5.0)
    # glClearColor(0,0,0, 0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
    
def timer(value):
    global y,kecepatan
    y -= kecepatan
    if y < value :
        #y= 10 tingkatan awal
        #y= 50 tingkatan akhir
        y = 50
    glutTimerFunc(kecepatan,timer,0)
    
def main ():   
    glutInit() #inisialisasi glut
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA) #utk mengatur display supaya berwarna
    glutInitWindowSize(600, 500) #utk mengatur ukuran window
    glutInitWindowPosition(100,100) #utk mengatur letak window
    glutCreateWindow("LABIRIN GA TUH GES") #utk memberi nama pada window
    glutDisplayFunc(showScreen) #utk fungsi callback
    glutIdleFunc(showScreen) #utk fungsi callback
    glutSpecialFunc(input_keyboard)
    # timer(0)
    init()
    glutMainLoop() #fungsi yang akan memulai keseluruhan program

main()