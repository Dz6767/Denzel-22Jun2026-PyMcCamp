# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
mobs.kill(mobs.target(NEAREST_PLAYER))
# fuction to make the agent come to player
def Teleport ():
    agent.teleport_to_player()


player.on_chat("come",Teleport)
def front(step):
    agent.move(FORWARD,step)
def back(step):
    agent.move(BACK,step)
def left(step):
     agent.move(LEFT,step)
def right(step):
     agent.move(RIGHT,step)
player.on_chat("front",front)
player.on_chat("back",back)
player.on_chat("left",left)
player.on_chat("right",right)
def boom():
    agent.collect_all()

player.on_chat("boom",boom)
def up(step):
    agent.move(UP,step)
def down(step):
    agent.move(DOWN,step)
player.on_chat("up",up)
player.on_chat("down",down)
def turnr():
    agent.turn_right
def turnl():
    agent.turn_left

player.on_chat("turnr",turnr)
player.on_chat("turnl",turnl)
player.on_chat("hahaha",difficult)

def difficult():
    gameplay.set_difficulty(EASY)


def gogogo():
    agent.move(FORWARD,4)
    agent.move(LEFT,4)
    agent.move(FORWARD,3)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,3)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)

player.on_chat("GOGOGO",gogogo)




def on_on_chat():
    agent.set_item(DIAMOND_AXE, 1, 1)
    agent.drop(FORWARD, 1, 1)
player.on_chat("g", on_on_chat)









def tree(step):
    for i in range (step):
        agent.destroy(FORWARD)
        agent.move(UP,1)
    agent.move(DOWN,step)
    agent.collect_all()

player.on_chat("chop", tree)



def mine(step):
    for i in range (step):
        agent.destroy(FORWARD)
        agent.move(FORWARD,1)
    agent.move(BACK,step)
    agent.collect_all()

player.on_chat("mine", mine)