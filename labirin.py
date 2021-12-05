#import library
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# LOGIK

# Koordinat x dan y untuk posisi kotak
x_player1 = 120
y_player1 = 130
# hold_player = [[x_player1,y_player1]]

waktu = 1000

level = 1
cek_skor = 1
skor = 0
hold_grid = []
# finish = [[344,50],[600,146],[600,162]]
finish = []
finis = False
point = []
cek_point = False

# Labirin
level1 = [
    "WWWWWWWWWWWWWWWWWWWWWWW",
    "W                     W",
    "W            WWWWWW   W",
    "W  W   WWWW       W   W",
    "W  W   W        WWWW  W",
    "W  WWWWW  WWWW        W",
    "W   W  W     W   W    W",
    "W   W  W     W  WWWW  W",
    "W   W  WWW  WW  W  W  W",
    "S        W   W  W  W  W",
    "WWWWWW   W   WWWW  W  W",
    "W    W   W R W        W",
    "W    W   WWWWW  WWW   W",
    "W        W        W   W",
    "WWWWWWWWWWWWWWFFWWWWWWW"
]

level2 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W     W        W        W  W  W",
    "W  W  W  WWWW  WWWWWWW  W  W  W",
    "W  W  W     W        W  W     W",
    "W  WWWWWWWWWW  W  WWWW  W  W  W",
    "W              W        W  W  W",
    "W  WW  WWWWWWWWW  WWWWWWW  W  W",
    "W  W   W       W  W        W  W",
    "W  WWWWW   W   W  W  WWWWWWW  F",
    "S          W   W  W  W  W  WWWW",
    "WWWWW  W   W   W  W  W  W  W  W",
    "W      W   W   W     W  W  W  W",
    "W  WWWWWWWWW   WWWWWWW  W  W  W",
    "W          W               R  W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

level3= [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W              W     W  W     W",
    "WWWWWWW  WWWW  W  WWWW  W  W  W",
    "W     W     W           W  W  W",
    "WWWW  W  WWWWWWW  WWWWWWWWWW  W",
    "W        W  W  W     W        W",
    "WWWWWWW  W  W  W  W  WWWW  W  W",
    "W  W  W  W  W  W  W     W  W  W",
    "W  W     W  W  W  WWWW  W  WWWW",
    "W  W  W  W     W  W  W     W  W",
    "W  W  W  WWWW  WWWW  WWWW  W  W",
    "W  W  W           W           W",
    "W  WWWWWWW  W  WWWWWWWWWWWWW  W",
    "W     W     W  W R W W  W  W  F",
    "W  WWWWWWW  WWWW   W W  W  WWWW",
    "S  W  W  W     W              W",
    "W  W  W  W  WWWWWWWWWWWWWWWW  W",
    "W                    W        W",
    "WWWWWWW  W  W  WWWW  WWWWWWW  W",
    "W        W  W  W              W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

lvl = [level1,level2,level3]

def drawText(ch,xpos,ypos):
    color = (69, 185, 6)
    # color = (0, 0, 0)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  

def drawTextNum(skor,xpos,ypos):
    color = (69, 185, 6)
    # color = (0, 0, 0)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

def draw_level():
    y_level = 0
    if level == 3:
        y_level += 60
    drawText("LEVEL KAMU : ",120,330+y_level)
    drawTextNum(level,250,330+y_level)

def labirin(pos,r,b,g):
    glPushMatrix()
    glPointSize(15) #utk mengatur ukuran titiknya
    glBegin(GL_POINTS) #utk memulai pembuatan objek titik
    glColor3ub(r,b,g) #kode warna pake rgb
    glVertex2f(pos[0],pos[1]) #titik koordinat
    glEnd() #utk mengakhiri objek yang dibuat
    glPopMatrix()

def draw_labirin(lvl,h_g):
    x,y = 120,50
    r,b,g = 66, 207, 160
    for row in lvl[::-1]:
        for col in row:
            if col == "W":
                labirin((x, y),r,b,g)
                h_g.append([x,y])
                h_g.append([104,130])
            elif col == "F":
                labirin((x, y),0,0,0)
                hold_grid.append([x,y])
                finish.append([x,y])
            elif col == 'R':
                if cek_point == True:
                    labirin((x, y), 0, 0, 0)
                    hold_grid.append([x,y])
                    point.append([x,y])
                else:
                    labirin((x, y),255, 255, 255)
                    hold_grid.append([x,y])
                    point.append([x,y])
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
    global x_player1, y_player1, level, cek_point
        
    if key == GLUT_KEY_UP:
        try:
            if hold_grid.index([x_player1,y_player1+16]) :
                if [x_player1,y_player1+16] == point[0] :
                    cek_point = True
                    y_player1 += 16
                if [x_player1,y_player1+16] == finish[0] and cek_point == True:
                    level +=1
                    cek_point = False
                    hold_grid.clear()
                    finish.clear()
                    x_player1 = 120
                    y_player1 = 130
                y_player1 += 0
        except:
            y_player1 += 16
            
    elif key == GLUT_KEY_DOWN:
        try:
            if hold_grid.index([x_player1,y_player1-16]) :
                if [x_player1,y_player1-16] == point[0] :
                    cek_point = True
                    y_player1 -= 16
                if [x_player1,y_player1-16] == finish[0] and cek_point == True:
                    level +=1
                    cek_point = False
                    point.clear()
                    hold_grid.clear()
                    finish.clear()
                    x_player1 = 120
                    y_player1 = 130
                y_player1 -= 0
        except:
            y_player1 -= 16
            
    elif key == GLUT_KEY_RIGHT:
        try:
            if hold_grid.index([x_player1+16,y_player1]) :
                if [x_player1+16,y_player1] == point[0] :
                    cek_point = True
                    x_player1 += 16
                if [x_player1+16,y_player1] == finish[0] :
                    level +=1
                    cek_point = False
                    point.clear()
                    hold_grid.clear()
                    finish.clear()
                    x_player1 = 120
                    y_player1 = 130
                x_player1 += 0
        except:
            x_player1 += 16
            
    elif key == GLUT_KEY_LEFT:
        try:
            if hold_grid.index([x_player1-16,y_player1]) :
                if [x_player1-16,y_player1] == point[0] :
                    cek_point = True
                    x_player1 -= 16
                if [x_player1-16,y_player1] == finish[0] :
                    level +=1
                    cek_point = False
                    point.clear()
                    hold_grid.clear()
                    finish.clear()
                    x_player1 = 120
                    y_player1 = 130
                x_player1 += 0
        except:
            x_player1 -= 16

#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 500) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    global lvl, finis
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate()
    if level < 4:
        draw_labirin(lvl[level-1],hold_grid)
        karakter()
        draw_level()
    else:
        bg_level()
        finis = True
        drawText("F I N I S H   ", 200,300)
        drawText("DENGAN WAKTU (s): ", 200,250)
        drawTextNum(skor,350,250)
    glutSwapBuffers() #utk membersihkan layar, double buffering

def init():
    # glClearColor(2,1,0, 2.0)
    # glClearColor(1,4,7, 5.0)
    glClearColor(0,0,0, 0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
    
def timer(value):
    global cek_skor, waktu, skor
    if finis == True :
        skor = cek_skor
    else:
        cek_skor += 1
    glutTimerFunc(waktu,timer,0)
    
def main ():   
    glutInit() #inisialisasi glut
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA) #utk mengatur display supaya berwarna
    glutInitWindowSize(600, 500) #utk mengatur ukuran window
    glutInitWindowPosition(100,100) #utk mengatur letak window
    glutCreateWindow("KOTAK LABIRIN") #utk memberi nama pada window
    glutDisplayFunc(showScreen) #utk fungsi callback
    glutIdleFunc(showScreen) #utk fungsi callback
    glutSpecialFunc(input_keyboard)
    timer(0)
    init()
    glutMainLoop() #fungsi yang akan memulai keseluruhan program

main()
print(hold_grid)