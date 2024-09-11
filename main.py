# مكتبة pygame مفتوحة المصدر
# في جميع أنحاء هذا الملف
import sys
import pygame  # استيراد مكتبة pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT  # استيراد الثوابت المحددة من ملف constants
from player import Player  # استيراد اللاعب من ملف player
from asteroid import Asteroid  # استيراد الكويكب من ملف asteroid
from asteroidfield import AsteroidField # استيراد حقل الكويكبات من ملف asteroidfield
from shot import Shot  # استيراد الرصاصة من ملف shot


# الدالة الرئيسية
def main():
    """
    دالة لبدء لعبة asteroids.
    """
    pygame.init()  # تهيئة مكتبة pygame
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )  # إعداد شاشة العرض بحجم العرض والارتفاع المحددين
    # كائن لتتبع الوقت
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # إنشاء لاعب في وسط الشاشة
    new_asteroid = AsteroidField()
    dt = 0  # الوقت المنقضي منذ آخر تحديث
    player.update(dt)  # Access the player object
    print("Starting asteroids!")  # طباعة رسالة بدء اللعبة
    print(f"Screen width: {SCREEN_WIDTH}")  # طباعة عرض الشاشة
    print(f"Screen height: {SCREEN_HEIGHT}")  # طباعة ارتفاع الشاشة

    while True:  # حلقة لا نهائية
        for event in pygame.event.get():  # التحقق من جميع الأحداث
            if event.type == pygame.QUIT:  # إذا كان نوع الحدث هو الخروج
                pygame.quit()
                return
        # اذا المستخدمخرج من اللعبة يخرج
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over!")
                sys.exit()

        screen.fill((0, 0, 0))  # ملء الشاشة باللون الأسود
        for obj in drawable:
            obj.draw(screen)

            
        pygame.display.flip()  # تحديث الشاشة لعرض التغييرات
        dt = clock.tick(60) / 1000.0  # حساب الوقت المنقضي منذ آخر تحديث
        


if __name__ == "__main__":
    main()
