import engine


gameRunning = True
while gameRunning:
    engine.fps.tick(60)

    for event in engine.pygame.event.get():
        if event.type == engine.pygame.QUIT:
            engine.pygame.quit()
            gameRunning = False
            quit()
    engine.pirate.movement()
    engine.knight.movement()
    engine.redrawGameScreen()

engine.pygame.quit()
