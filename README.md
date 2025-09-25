# 🚀 Équipe NSI Prem P03 - 2025/2026

Voici la team avec nos pseudos GitHub :

| Prénom  | Pseudo GitHub    |
|---------|------------------|
| Thimothe | `thimothe.chps`  |
| Haron    | `HaronElmz`      |
| Victor   | `frst_304`       |

import pygame
import random
import math

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Particle:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 4)
        self.size = random.randint(2, 5)
        self.life = 100

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1

    def draw(self, screen):
        alpha = max(0, min(255, self.life * 2))
        surface = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (255, 255, 255, alpha), (self.size, self.size), self.size)
        screen.blit(surface, (self.x - self.size, self.y - self.size))

particles = []

# Boucle principale
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Générer des particules
    if len(particles) < 300:
        particles.append(Particle())

    # Mettre à jour et dessiner les particules
    for p in particles[:]:
        p.move()
        p.draw(screen)
        if p.life <= 0:
            particles.remove(p)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
