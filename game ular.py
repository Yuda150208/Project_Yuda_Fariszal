import pygame
import random

pygame.init()

# Ukuran layar
LEBAR = 600
TINGGI = 400

# Warna
PUTIH = (255, 255, 255)
HIJAU = (0, 255, 0)
MERAH = (255, 0, 0)
HITAM = (0, 0, 0)

layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Snake Game Python")

clock = pygame.time.Clock()
ukuran = 20

font = pygame.font.SysFont("Arial", 25)
font_besar = pygame.font.SysFont("Arial", 40)

def tampil_skor(skor):
    text = font.render(f"Skor: {skor}", True, PUTIH)
    layar.blit(text, [10, 10])

def game_over_screen():
    layar.fill(HITAM)

    teks1 = font_besar.render("GAME OVER", True, MERAH)
    teks2 = font.render("Tekan R = Main Lagi", True, PUTIH)
    teks3 = font.render("Tekan Q = Keluar", True, PUTIH)

    layar.blit(teks1, (LEBAR//2 - 120, TINGGI//2 - 60))
    layar.blit(teks2, (LEBAR//2 - 120, TINGGI//2))
    layar.blit(teks3, (LEBAR//2 - 120, TINGGI//2 + 30))

    pygame.display.update()

def game():

    while True:  # loop supaya bisa restart

        x = LEBAR // 2
        y = TINGGI // 2

        x_gerak = 0
        y_gerak = 0

        snake = []
        panjang = 1

        makanan_x = round(random.randrange(0, LEBAR - ukuran) / 20) * 20
        makanan_y = round(random.randrange(0, TINGGI - ukuran) / 20) * 20

        jalan = True

        while jalan:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_gerak = -ukuran
                        y_gerak = 0
                    elif event.key == pygame.K_RIGHT:
                        x_gerak = ukuran
                        y_gerak = 0
                    elif event.key == pygame.K_UP:
                        y_gerak = -ukuran
                        x_gerak = 0
                    elif event.key == pygame.K_DOWN:
                        y_gerak = ukuran
                        x_gerak = 0

            x += x_gerak
            y += y_gerak

            # Game over kalau keluar layar
            if x >= LEBAR or x < 0 or y >= TINGGI or y < 0:
                jalan = False

            layar.fill(HITAM)

            pygame.draw.rect(layar, MERAH, [makanan_x, makanan_y, ukuran, ukuran])

            kepala = [x, y]
            snake.append(kepala)

            if len(snake) > panjang:
                del snake[0]

            # tabrak diri sendiri
            for bagian in snake[:-1]:
                if bagian == kepala:
                    jalan = False

            for bagian in snake:
                pygame.draw.rect(layar, HIJAU, [bagian[0], bagian[1], ukuran, ukuran])

            # makan
            if x == makanan_x and y == makanan_y:
                makanan_x = round(random.randrange(0, LEBAR - ukuran) / 20) * 20
                makanan_y = round(random.randrange(0, TINGGI - ukuran) / 20) * 20
                panjang += 1

            tampil_skor(panjang - 1)

            pygame.display.update()
            clock.tick(10)

        # ===== GAME OVER MENU =====
        menunggu = True
        while menunggu:
            game_over_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        menunggu = False  # restart game
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return

game()