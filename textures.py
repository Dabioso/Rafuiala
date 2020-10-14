from engine import pygame


def Player_Textures(character):
    if character == "Pirate":
        standing_textures = [pygame.image.load('textures\\characters\\pirate\\idle_000.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\idle_111.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\idle_222.png').convert_alpha(),
                            pygame.image.load('textures\\characters\\pirate\\idle_333.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\idle_444.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\idle_555.png').convert_alpha(),
                            pygame.image.load('textures\\characters\\pirate\\idle_666.png').convert_alpha()]
        jump_textures = [pygame.image.load('textures\\characters\\pirate\\jump_000.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\jump_111.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\jump_222.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\pirate\\jump_333.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\jump_444.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\jump_555.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\pirate\\jump_666.png').convert_alpha()]
        run_textures = [pygame.image.load('textures\\characters\\pirate\\run_000.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\run_111.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\run_222.png').convert_alpha(),
                        pygame.image.load('textures\\characters\\pirate\\run_333.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\run_444.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\run_555.png').convert_alpha(),
                        pygame.image.load('textures\\characters\\pirate\\run_666.png').convert_alpha()]
        walk_textures = [pygame.image.load('textures\\characters\\pirate\\walk_000.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\walk_111.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\walk_222.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\pirate\\walk_333.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\walk_444.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\walk_555.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\pirate\\walk_666.png').convert_alpha()]
        attack_textures = [pygame.image.load('textures\\characters\\pirate\\attack_000.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\attack_111.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\attack_222.png').convert_alpha(),
                           pygame.image.load('textures\\characters\\pirate\\attack_333.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\attack_444.png').convert_alpha(), pygame.image.load('textures\\characters\\pirate\\attack_555.png').convert_alpha(),
                           pygame.image.load('textures\\characters\\pirate\\attack_666.png').convert_alpha()]

    elif character == "Knight":
        standing_textures = [pygame.image.load('textures\\characters\\knight\\idle_00.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\idle_11.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\idle_22.png').convert_alpha(),
                            pygame.image.load('textures\\characters\\knight\\idle_33.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\idle_44.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\idle_55.png').convert_alpha(),
                            pygame.image.load('textures\\characters\\knight\\idle_66.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\idle_77.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\idle_88.png').convert_alpha(),
                            pygame.image.load('textures\\characters\\knight\\idle_99.png').convert_alpha()]
        jump_textures = [pygame.image.load('textures\\characters\\knight\\jump_00.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\jump_11.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\jump_22.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\knight\\jump_33.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\jump_44.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\jump_55.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\knight\\jump_66.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\jump_77.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\jump_88.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\knight\\jump_99.png').convert_alpha()]
        run_textures = [pygame.image.load('textures\\characters\\knight\\run_00.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\run_11.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\run_22.png').convert_alpha(),
                        pygame.image.load('textures\\characters\\knight\\run_33.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\run_44.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\run_55.png').convert_alpha(),
                        pygame.image.load('textures\\characters\\knight\\run_66.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\run_77.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\run_88.png').convert_alpha(),
                        pygame.image.load('textures\\characters\\knight\\run_99.png').convert_alpha()]
        walk_textures = [pygame.image.load('textures\\characters\\knight\\walk_00.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\walk_11.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\walk_22.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\knight\\walk_33.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\walk_44.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\walk_55.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\knight\\walk_66.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\walk_77.png').convert_alpha(), pygame.image.load('textures\\characters\\knight\\walk_88.png').convert_alpha(),
                         pygame.image.load('textures\\characters\\knight\\walk_99.png').convert_alpha()]
        attack_textures = []
    
    return standing_textures, jump_textures, run_textures, walk_textures, attack_textures

