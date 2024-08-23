# مكتبة pygame مفتوحة المصدر
# في جميع أنحاء هذا الملف
import pygame  # استيراد مكتبة pygame
from constants import *  # استيراد جميع الثوابت من ملف constants

# الدالة الرئيسية
def main():
    """
    دالة لبدء لعبة asteroids.
    """
    pygame.init()  # تهيئة مكتبة pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # إعداد شاشة العرض بحجم العرض والارتفاع المحددين
    clock = pygame.time.Clock()
    print(clock)
    dt = 0  # متغير لتخزين الوقت المنقضي منذ آخر تحديث	
    print(f"Starting asteroids!")  # طباعة رسالة بدء اللعبة
    print(f"Screen width: {SCREEN_WIDTH}")  # طباعة عرض الشاشة
    print(f"Screen height: {SCREEN_HEIGHT}")  # طباعة ارتفاع الشاشة
    while True:  # حلقة لا نهائية
        for event in pygame.event.get():  # التحقق من جميع الأحداث
            if event.type == pygame.QUIT:  # إذا كان نوع الحدث هو الخروج
                return  # إنهاء الدالة والخروج من اللعبة
        screen.fill((0, 0, 0))  # ملء الشاشة باللون الأسود
        pygame.display.flip()  # تحديث الشاشة لعرض التغييرات
        dt = clock.tick(60) / 1000.0  # حساب الوقت المنقضي منذ آخر تحديث


if __name__ == "__main__":  # إذا كان هذا الملف هو الملف الرئيسي الذي يتم تشغيله
    main()  # استدعاء الدالة الرئيسية