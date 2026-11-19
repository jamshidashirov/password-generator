# Bu mening GitHubdagi birinchi loyiham va kodim    
import random
import string

def generate_password(length=30):
    """Murakkab va ishonchli parol yaratuvchi funksiya"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("Xavfsizlik uchun yangi parolingiz:")
    print(generate_password())
#Kod ishlayapti 
