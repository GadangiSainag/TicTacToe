import pygame
empty_space=70

run= True
game=[['-','-','-'],
	  ['-','-','-'],
	  ['-','-','-']]


screen = width, height= 404, 404+int(empty_space)
#box =128x128
pygame.init()
window = pygame.display.set_mode(screen)
pygame.display.set_caption("TIC TAC TOE")
#icon
icon= pygame.image.load('game.png')
pygame.display.set_icon(icon)
#diciding the player
temp=0
player=''

#player1 aka CROSS
mouse_x=0
mouse_y=0
cross=pygame.image.load('cross.png')
empty=pygame.image.load('empty.jpg')
circle= pygame.image.load('ovel.png')
#box1,box2,box3
#box4,box5,box6
#box7,box8,box9
box1=(0,empty_space)
box2=(138,empty_space)
box3=(276,empty_space)
box4=(0,empty_space+128+10)
box5=(138,empty_space+128+10)
box6=(276,empty_space+128+10)
box7=(0,empty_space+128+10+128+10)
box8=(138,empty_space+128+10+128+10)
box9=(276,empty_space+128+10+128+10)

boxes={ box1:'-',
	    box2:'-',
	    box3:'-',
	    box4:'-',
	    box5:'-',
	    box6:'-',
	    box7:'-',
	    box8:'-',
	    box9:'-'}

#TO SHOW THE IMAGES ON THE SCREEN
images = {box1 : empty,
	      box2 : empty,
	      box3 : empty,
	      box4 : empty,
	      box5 : empty,
	      box6 : empty,
	      box7 : empty,
	      box8 : empty,
	      box9 : empty  }
text=pygame.font.Font('freesansbold.ttf', 16)
over_font= pygame.font.Font('freesansbold.ttf', 63)
def  decide_player(box):
	global temp, playe
	if temp%2==0:
		player='one'
		testt= text.render("GAME OVER", True , (255,255,255))
		window.blit(testt, (20,40))
		if boxes[box]!= 'x'and boxes[box]!='o':
			boxes[box]='x'
			images[box]=cross
		else:
			temp+=1
		
	elif temp%2==1:
		player='two'
		if boxes[box]!= 'x'and boxes[box]!='o':
			boxes[box]='o'
			images[box]= circle
		else:
			temp+=1
	temp+=1
	return temp,player


def gameBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9):
	global cross, empty
	window.blit(images[box1], box1)
	window.blit(images[box2], box2)
	window.blit(images[box3], box3)
	window.blit(images[box4], box4)
	window.blit(images[box5], box5)
	window.blit(images[box6], box6)
	window.blit(images[box7], box7)
	window.blit(images[box8], box8)
	window.blit(images[box9], box9)	

def winner():
	global boxes,game,text
	if game[0][0]==game[0][1]==game[0][2]=='x' or game[1][0]==game[1][1]==game[1][2]=='x' or game[2][0]==game[2][1]==game[2][2]=='x' or \
	game[0][0]==game[1][0]==game[2][0]=='x' or game[0][1]==game[1][1]==game[2][1]=='x' or game[0][2]==game[1][2]==game[2][2]=='x' or \
	game[0][0]==game[1][1]==game[2][2]=='x' or game[0][2]==game[1][1]==game[2][0]=='x'  :
		winner=text.render("PLAYER 1 WON THE MATCH", True ,(0,255,0))
		window.blit(winner, (70,50))
		over_text= over_font.render("GAME OVER", True , (0,0,0))
		window.blit(over_text, (20,240))
		pygame.time.delay(500)
		pygame.display.update()
		pygame.quit()
	elif game[0][0]==game[0][1]==game[0][2]=='o' or game[1][0]==game[1][1]==game[1][2]=='o' or game[2][0]==game[2][1]==game[2][2]=='o' or \
	game[0][0]==game[1][0]==game[2][0]=='o' or game[0][1]==game[1][1]==game[2][1]=='o' or game[0][2]==game[1][2]==game[2][2]=='o' or \
	game[0][0]==game[1][1]==game[2][2]=='o' or game[0][2]==game[1][1]==game[2][0]=='o':
		winner=text.render("PLAYER 2 WON THE MATCH", True ,(0,255,0))
		window.blit(winner, (70,50))
		over_text= over_font.render("GAME OVER", True , (0,0,0))
		window.blit(over_text, (20,240))
		pygame.time.delay(500)
		pygame.display.update()
		pygame.quit()

	elif game[0][0]!='-' and game[0][1]!='-' and game[0][2]!='-' and game[1][0]!='-' and game[1][1]!='-' and game[1][2]!='-' and \
	 game[2][0]!='-' and game[2][1]!='-' and game[2][2]!='-':

		winner=text.render("NOBODY WON tHE MATCH", True ,(0,255,0))
		window.blit(winner, (80,50))
		over_text= over_font.render("GAME OVER", True , (0,0,0))
		window.blit(over_text, (20,240))
		pygame.time.delay(500)
		pygame.display.update()
		pygame.quit()

	#
	
def definations():
	global empty_space, height, width
	pygame.draw.rect(window, (0,0,0), (128,empty_space,10, height ))
	pygame.draw.rect(window, (0,0,0), (128 +128+10,empty_space,10, height ))
	pygame.draw.rect(window, (0,0,0), (0,empty_space+128,width, 10))
	pygame.draw.rect(window, (0,0,0), (0,empty_space+128+10+128,width, 10))
	pygame.draw.rect(window, (153,255,255), (0,0 ,width,empty_space))
	#text goes here

clock=pygame.time.Clock()

while run:
	clock.tick(30)
	game[0][0],game[1][0],game[2][0]=boxes[box1],boxes[box2],boxes[box3]
	game[0][1],game[1][1],game[2][1]=boxes[box4],boxes[box5],boxes[box6]
	game[0][2],game[1][2],game[2][2]=boxes[box7],boxes[box8],boxes[box9]
	pygame.display.update()
	#decide_player(temp,player)
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			run=False

	click= pygame.mouse.get_pressed()
	if click[0]:
		mouse_x= pygame.mouse.get_pos()[0]
		mouse_y= pygame.mouse.get_pos()[1]
	if 1<mouse_x <128 and empty_space <mouse_y< empty_space+128:
		decide_player(box1)
		
	if 138< mouse_x<266 and empty_space <mouse_y <empty_space+128:
		decide_player(box2)	
		
	if 276< mouse_x<404 and empty_space<mouse_y <empty_space+128:
		decide_player(box3)	
		
	if 1<mouse_x <128 and empty_space+128+10<mouse_y <empty_space+128+128+10:
		decide_player(box4)	
		
	if 138< mouse_x<266 and empty_space+128+10<mouse_y <empty_space+128+128+10:
		decide_player(box5)	
		
	if 276< mouse_x<404 and empty_space+128+10<mouse_y <empty_space+128+128+10:
		decide_player(box6)	
		
	if 1<mouse_x <128 and empty_space+128+10+128+10<mouse_y <empty_space+128+128+128+10+10:
		decide_player(box7)	
		
	if 138< mouse_x<266 and empty_space+128+10+128+10<mouse_y <empty_space+128+128+128+10+10:
		decide_player(box8)	
		
	if 276< mouse_x<404 and empty_space+128+10+128+10<mouse_y <empty_space+128+128+128+10+10:
		decide_player(box9)	
		
	window.fill((255,255,255))
	#gameboard here
	
	gameBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
	definations()
	if temp%2==0:
		
		player_text= text.render("Player 1 --", True , (204,0,0))
		window.blit(player_text, (20,20))
	else:
		player_text= text.render("Player 2 --", True , (51,51,255))
		window.blit(player_text, (20,20))
	winner()
	pygame.time.delay(100)
	mouse_x=0
	mouse_y=0




pygame.quit()