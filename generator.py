import secrets
import string

def generate_password(length=16):
    """Kriptografik jihatdan xavfsiz va murakkab parol yaratuvchi funksiya"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    try:
        user_input = input("Parol uzunligini kiriting (standart 16): ").strip()
        length = int(user_input) if user_input else 16
        
        if length < 8:
            print("Ogohlantirish: Xavfsizlik uchun kamida 8 ta belgi tavsiya etiladi.")
            
        print(f"Xavfsizlik uchun yangi parolingiz:\n{generate_password(length)}")
    except ValueError:
        print("Xato: Iltimos, faqat butun son kiriting.")
