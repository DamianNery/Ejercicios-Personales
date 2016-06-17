import pyglet

class Jugador():
    def __init__(self,window,imagenes):
        self.w=window
        self.i=imagenes
        self.up1_key=pyglet.window.key.A
        self.down1_key=pyglet.window.key.Z
        self.up2_key=pyglet.window.key.UP
        self.down2_key=pyglet.window.key.DOWN
        self.quit_key=pyglet.window.key.Q
        
    def on_key_press(self,symbol,modifiers):
        if symbol == self.up1_key:
            self.i.player1_spr.y += 25
        elif symbol == self.down1_key:
            self.i.player1_spr.y -= 25
        elif symbol == self.up2_key:
            self.i.player2_spr.y += 25
        elif symbol == self.down2_key:
            self.i.player2_spr.y -= 25
        elif symbol == self.quit_key:
            exit(0)

class Bola():
    def __init__(self,window,imagenes):
        self.w=window
        self.i=imagenes

        self.estado=0

        self.ckball=self.i.ball_spr
        self.ckp1=self.i.player1_spr
        self.ckp2=self.i.player2_spr

    def sentidos(self):
                        
        if self.ckball.y == self.w.height and self.estado==0: #01 INICIO
            self.estado=1
                
        elif self.ckball.x == self.w.width and self.estado==1: #12
            self.estado=2

        elif self.ckball.y == 0 and self.estado==2: #23
            self.estado=3

        elif self.ckball.x == 0 and self.estado==3: #34
            self.estado=4

        elif self.ckball.y == self.w.height and self.estado==4: #41
            self.estado=1
                        
        if self.ckball.y == self.w.height and self.estado==5: #01 INICIO
            self.estado=2

        elif self.ckball.x == 0 and self.estado==2: #14
            self.estado=1

        elif self.ckball.y == 0 and self.estado==1: #43
            self.estado=4

        elif self.ckball.x == self.w.width and self.estado==4: #32
            self.estado=3

        elif self.ckball.y == self.w.height and self.estado==3: #21
            self.estado=2

        if self.ckball.x == self.ckp2.x: #P2 derecha
            if self.ckball.y >= self.ckp2.y-self.ckp2.width//2:
                if self.ckball.y <= self.ckp2.y+self.ckp2.width//2:                    
                    if self.estado==1:
                        self.estado=2
                    elif self.estado==4:
                        self.estado=3
       
        if self.ckball.x == self.ckp1.x: #P1 izquierda
            if self.ckball.y >= self.ckp1.y-self.ckp1.width//2:
                if self.ckball.y <= self.ckp1.y+self.ckp1.width//2:
                    if self.estado==3:
                        self.estado=4
                    elif self.estado==2:
                        self.estado=1

    def estados(self):
        if self.estado==0:
            self.ckball.x += 1*10
            self.ckball.y += 1*10
        elif self.estado==1:
            self.ckball.x += 1*10
            self.ckball.y -= 1*10
        elif self.estado==2:
            self.ckball.x -= 1*10
            self.ckball.y -= 1*10
        elif self.estado==3:
            self.ckball.x -= 1*10
            self.ckball.y += 1*10
        elif self.estado==4:
            self.ckball.x += 1*10
            self.ckball.y += 1*10
        elif self.estado==5:
            self.ckball.x -= 1*10
            self.ckball.y += 1*10

    def puntos(self):
        self.w.score1.text='Player1: '+str(self.w.suma1)
        self.w.score2.text='Player2: '+str(self.w.suma2)
        if self.ckball.x<self.ckp1.x-20:
            self.w.suma2+=1
            self.ckball.x = 500
            self.ckball.y = 550
            self.estado=5
        if self.ckball.x>self.ckp2.x+20:
            self.w.suma1+=1
            self.ckball.x = 300
            self.ckball.y = 550
            self.estado=0
            
    def redraw(self):
        self.sentidos()
        self.estados()
        self.puntos()
        
class Imagenes():
    def __init__(self,window):
        self.w=window
        player = pyglet.image.load("barra.png")
        ball = pyglet.image.load("bola.png")
        
        player.anchor_x = player.width//2
        player.anchor_y = player.height//2
        ball.anchor_x = ball.width//2
        ball.anchor_y = ball.height//2
        
        self.player1_spr = pyglet.sprite.Sprite(player,x=100,y=300)
        self.player2_spr = pyglet.sprite.Sprite(player,x=700,y=300)
        self.ball_spr = pyglet.sprite.Sprite(ball,x=400,y=550)

        self.ball_spr.scale=0.25
        self.player1_spr.scale=0.25
        self.player2_spr.scale=0.25

        self.player1_spr.rotation=(90.0)
        self.player2_spr.rotation=(90.0)
        
    def redraw(self):
        self.player1_spr.draw()
        self.player2_spr.draw()
        self.ball_spr.draw()
        
class Window(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super(Window,self).__init__(width=800,height=600,*args,**kwargs)
        the_window=self
        self.imagenes=Imagenes(the_window)
        self.bola=Bola(the_window,self.imagenes)
        self.jugador=Jugador(the_window,self.imagenes)
        self.suma1=0
        self.suma2=0
        self.label = pyglet.text.Label('Pong en Pyglet',
                     font_name='Times New Roman',font_size=36,
                     x=self.width//2,y=550,anchor_x='center',anchor_y='center')
        self.score1 = pyglet.text.Label('Player1: '+str(self.suma1),
                     font_name='Times New Roman',font_size=20,
                     x=100,y=575,anchor_x='center',anchor_y='center')
        self.score2 = pyglet.text.Label('Player2: '+str(self.suma2),
                     font_name='Times New Roman',font_size=20,
                     x=700,y=575,anchor_x='center',anchor_y='center')
        pyglet.clock.schedule_interval(self.update, 1/15)

    def on_draw(self):
        self.label.draw()
        self.score1.draw()
        self.score2.draw()

    def on_key_press(self, symbol, modifiers):
        self.jugador.on_key_press(symbol, modifiers)
        
    def update(self,*args,**kwargs):
        self.clear()
        self.on_draw()
        self.imagenes.redraw()
        self.bola.redraw()

if __name__=="__main__":
    window=Window()
    pyglet.app.run()
