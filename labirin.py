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

#Variabel untuk menjalankan logika game kotak labirin
waktu = 1000
y_level = 0

#game over
y_time_line = 290
x_time_line = [450,550,600]
x_pilih = 260
game_over = False

#play game
play = False

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

#fungsi untuk menampilkan teks ketika program dijalankan 
def drawText(ch,xpos,ypos):
    color = (69, 185, 6) #kode warna
    # color = (0, 0, 0)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2]) #kode warna
    line=0
    glRasterPos2f (xpos, ypos) #posisi teks
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  #membuat karakter/teks

#fungsi untuk menampilkan teks ketika program dijalankan           
def drawTextbold(ch,xpos,ypos):
    color = (69, 185, 6) #kode warna
    # color = (0, 0, 0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2]) #kode warna
    line=0
    glRasterPos2f (xpos, ypos) #posisi teks
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  #membuat karakter/teks

#fungsi untuk menampilkan skor ketika program dijalankan 
def drawTextNum(skor,xpos,ypos):
    color = (69, 185, 6) #kode warna
    # color = (0, 0, 0)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2]) #kode warna
    line=0
    glRasterPos2f (xpos, ypos) #posisi teks
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))#membuat karakter/teks

#fungsi utk menghitung level dan waktu dari labirin
def draw_level():
    global y_level,y_time_line,x_time_line
    if level == 3 :
        y_level = 100
        y_time_line = 390
    time_line(x_time_line[level-1],y_time_line)
    drawText("LEVEL KAMU : ",120,330+y_level)
    drawTextNum(level,250,330+y_level)
    drawText("WAKTU KAMU(S): ", 120,300+y_level)
    drawTextNum(cek_skor,270,300+y_level)

#membentuk labirin dengan menggunakan objek points
def labirin(pos,r,b,g):
    glPushMatrix() #utk menyimpan koordinat yang ada
    glPointSize(15) #utk mengatur ukuran titiknya
    glBegin(GL_POINTS) #utk memulai pembuatan objek titik
    glColor3ub(r,b,g) #kode warna pake rgb
    glVertex2f(pos[0],pos[1]) #titik koordinat
    glEnd() #utk mengakhiri objek yang dibuat
    glPopMatrix() #utk memanggil suatu fungsi yang telah disimpan glPushMatrix()

#Fungsi membuat labirin menggunkan perulangan for
def draw_labirin(levl,h_g):
    x,y = 120,50
    r,b,g = 66, 207, 160
    for row in levl[::-1]: #utk membuat row atau baris 
        for col in row: #utk membuat kolom dimana nanti col akan diseleksi
            if col == "W": #maka membentuk dinding labirin
                labirin((x, y),r,b,g)
                h_g.append([x,y])
                h_g.append([104,130])
            elif col == "F":  #maka membuat jalur finish
                labirin((x, y),0,0,0)
                hold_grid.append([x,y])
                finish.append([x,y])
            elif col == 'R': #maka membuat kotak yng akan dicari
                if cek_point == True:
                    # labirin((x, y), 0, 0, 0)
                    hold_grid.append([x,y])
                    point.append([x,y])
                else:
                    labirin((x, y),255, 255, 255)
                    hold_grid.append([x,y])
                    point.append([x,y])
            x += 16
        y += 16
        x = 120

#untuk membuat background ketika game yang sudah diselesaikan yang nantinya teks akan ditampilkan
def bg_level():
    glPushMatrix() #utk menyimpan koordinat yang ada
    glBegin(GL_QUADS) #utk memulai pembuatan objek titik
    glColor3ub(145,100,40) #kode warna pake rgb
    glVertex2f(250,280) #titik koordinat
    glVertex2f(500,280) #titik koordinat
    glVertex2f(500,330) #titik koordinat
    glVertex2f(250,330) #titik koordinat
    glEnd() #utk mengakhiri objek yang dibuat
    
    glLineWidth(3) #utk menentukan lebar garis yang akan digambar
    glBegin(GL_LINE_LOOP) #utk menampilkan garis loop
    glColor3ub(69, 185, 6) #kode warna pake rgb
    glVertex2f(250,280) #titik koordinat
    glVertex2f(500,280) #titik koordinat
    glVertex2f(500,330) #titik koordinat
    glVertex2f(250,330) #titik koordinat
    glEnd() #utk mengakhiri objek yang dibuat
    glPopMatrix() #utk memanggil suatu fungsi yang telah disimpan glPushMatrix()

#Fungsi untuk membuat karakter yang berupa objek point 
def karakter():
    glPushMatrix() #utk menyimpan koordinat yang ada
    glPointSize(10) #utk mengatur ukuran titiknya
    glBegin(GL_POINTS) #utk memulai pembuatan objek titik
    glColor3ub(255, 136, 0) #kode warna pake rgb
    glVertex2f(x_player1,y_player1) #titik koordinat
    glEnd()  #utk mengakhiri objek yang dibuat
    glPopMatrix() #utk memanggil suatu fungsi yang telah disimpan glPushMatrix()

#Fungsi untuk kecepatan waktu
def time_line(x,y):
    glPushMatrix() #utk menyimpan koordinat yang ada
    glLineWidth(5) #utk menentukan lebar garis yang akan digambar
    glBegin(GL_LINES) #utk menghubungkan antar titik menjadi sebuah garis
    glColor3ub(255,0,0) #kode warna pake rgb
    glVertex2f(120,y) #titik koordinat
    glVertex2f(x,y) #titik koordinat
    glEnd() #utk mengakhiri objek yang dibuat
    glPopMatrix() #utk memanggil suatu fungsi yang telah disimpan glPushMatrix()

#Fungsi pilih
def pilih(x,y): 
    glPushMatrix() #utk menyimpan koordinat yang ada
    glPointSize(5) #utk mengatur ukuran titiknya
    glBegin(GL_POINTS) #utk memulai pembuatan objek titik
    glVertex2f(x,y)  #titik koordinat
    glEnd() #utk mengakhiri objek yang dibuat
    glPopMatrix() #utk memanggil suatu fungsi yang telah disimpan glPushMatrix()

# LOGIK
#Fungsi input keyboard
def input_keyboard(key,x,y):
    global x_player1, y_player1, level, cek_point, x_pilih, x_time_line

    #Fungsi untuk mengubah posisi kotak       
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
                    x_player1 = 120 #posisi utk player 120 dan 130
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
                    x_player1 = 120  #posisi utk player 120 dan 130
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
                    x_player1 = 120 #posisi utk player 120 dan 130
                    y_player1 = 130
                x_player1 += 0
        except:
            x_pilih = 410
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
                    x_player1 = 120 #posisi utk player 120 dan 130
                    y_player1 = 130
                x_player1 += 0
        except:
            x_pilih = 260
            x_player1 -= 16

#Fungsi input keyplayer            
def key_player(key,x,y):
    global game_over, level, x_time_line,play
    # Untuk mengubah posisi kotak
    if ord(key) == ord(b'\r'):
        if x_pilih == 260:
            game_over = False
            play = False
            level = 1
            x_time_line= [450,550,600]
        elif x_pilih == 410:
            game_over = "End"

#Fungsi input mouse
def input_mouse(key,state,x,y):
    global play
    if key == GLUT_LEFT_BUTTON:
        # print("x",x,"y",y)
        if (x>190 and x < 382) and (y>170 and y<218):
            play = True
          
#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 500) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
#Fungsi menampilkan objek
def showScreen():
    global lvl, finis
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate() #fungsi looping
    if play == True:
        if level < 4 and game_over == False:
            draw_labirin(lvl[level-1],hold_grid)
            karakter()
            draw_level()
            
        elif game_over == True:  
            drawTextbold("G A M E   O V E R", 280,300)
            drawText("INGIN MELANJUTKAN PERMAINAN?", 250,250)
            drawText("Y E S         N O", 275,230)
            pilih(x_pilih,235) # x=260 dan x=410
            
        else:
            finis = True
            drawText("F I N I S H   ", 200,300)
            drawText("W A K T U (s): ", 200,250)
            drawTextNum(skor,350,250) #skor akhir yang akan dicetak ketika game berakhir
    else:
        bg_level()
        drawTextbold("P L A Y    G A M E", 280,300)
           
    glutSwapBuffers() #utk membersihkan layar, double buffering

#Fungsi untuk konfigurasi objek
def init():
    # glClearColor(2,1,0, 2.0)
    # glClearColor(1,4,7, 5.0)
    glClearColor(0,0,0, 0) # utk memilih warna yang digunakan untuk membersihkan latar dalam mode RGBA
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
    
# fungsi utk menghitung skor
def timer(value):
    # cek skor : skor sementara untuk penghitungan skor player ketika menelusuri labirin
    # skor : skor akhir yang akan dicetak ketika game berakhir
    # waktu : waktu yang telah dimainkan dalam permainan
    # time_line : garis kecepakatan waktu
    # game_over : ketika game gagal dimainkan
    global cek_skor, waktu, skor, x_time_line, game_over 
    if play == True:
        if game_over == False:
            if (finis == True) or (x_time_line[level-1] == 120):
                skor = cek_skor
                game_over = True
            else:
                x_time_line[level-1] -= 10
                cek_skor += 1
    glutTimerFunc(waktu,timer,0)

#Fungsi yang dipanggil ketika program dieksekusi
def main ():   
    glutInit() #inisialisasi glut
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA) #utk mengatur display supaya berwarna
    glutInitWindowSize(600, 500) #utk mengatur ukuran window
    glutInitWindowPosition(100,100) #utk mengatur letak window
    glutCreateWindow("KOTAK LABIRIN") #utk memberi nama pada window
    glutDisplayFunc(showScreen) #utk fungsi callback
    glutIdleFunc(showScreen) #utk fungsi callback
    glutSpecialFunc(input_keyboard) # utk mengaktifkan tombol-tombol khusus pada keyboard
    glutKeyboardFunc(key_player) #utk fungsi panggilan balik keyboard 
    glutMouseFunc(input_mouse)  #utk fungsi panggilan balik mouse
    timer(0)
    init() #memanggil fungsi init
    glutMainLoop() #fungsi yang akan memulai keseluruhan program

main() #memanggil fungsi main