import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))#tamanho da tela
done = False#se acabou o game
clock = pygame.time.Clock()#tempo do jogo, padrao 

class jogador(object):#cria classe jogador
    def __init__(self):
        self.color = (0, 128, 255)#cor do jogador
    def update(self,x,y):
        pygame.draw.rect(screen, self.color, pygame.Rect(x, y, 60, 60))#altera a posicao com os valores novos de x e y
        
class Inimigo(object):
    def __init__(self,x,y):
        self.color = (255, 128, 0)
        self.x=x#pos original do inimigo
        self.y=y
        self.speed=1
    def correAtras(self,x,y):


        if(x>self.x):# se a posicao x do jogador for maior que o self(desse inimigo) ele vai aumenta esse x, indo para a direcao dele
            self.x=self.x+self.speed
        else:
            self.x=self.x-self.speed
        if(y>self.y):
            self.y=self.y+self.speed
        else:
            self.y=self.y-self.speed

        if(x==self.x and y==self.y):
            global done#para pegar a var global
            done = True#fecha o game pois acabou


        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, 40, 40))
        


if __name__ == '__main__':
    player = jogador()#instancia o jogador
    x = 30#posicoes originais do jogador
    y = 30#esses x e y dentro da main sao do jogador, inclusive quando sao passados pro inimigo correr atras

    #instancia inimigos
    #os parametros sao as posicoes originais dos inimigos
    inimigo1 = Inimigo(-400,100)
    inimigo2 = Inimigo(-100,200)
    inimigo1 = Inimigo(-200,100)
    inimigo2 = Inimigo(100,200)
    inimigo1 = Inimigo(400,100)
    inimigo2 = Inimigo(100,200)
    inimigo2 = Inimigo(100,-500)
    inimigo2 = Inimigo(100,200)
    
    
    
    while not done:#equnato o jogo n acabou

        for event in pygame.event.get():#pra sair do game
            if event.type == pygame.QUIT: done = True
                
        pressed = pygame.key.get_pressed()#pra cada seta ele joga um valor pra x ou y, cordennadas
        if pressed[pygame.K_UP]: y -= 4
        if pressed[pygame.K_DOWN]: y += 4
        if pressed[pygame.K_LEFT]: x -= 4
        if pressed[pygame.K_RIGHT]: x += 4

        screen.fill((0, 0, 0))
            

        player.update(x,y)#chama update toda vez
        inimigo1.correAtras(x,y)
        inimigo2.correAtras(x,y)

        pygame.display.flip() #para mudar o frame
        clock.tick(60)