import random
import string

def generate_password(length=None):
    if length is None:
        length = random.randint(8, 32)
    
    if length < 8 or length > 32:
        raise ValueError("Длина пароля должна быть от 8 до 32 символов.")
    
    # Определяем символы для пароля
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Объединяем все символы
    all_characters = lowercase + uppercase + digits + special_characters
    
    # Убедимся, что в пароле будут символы всех категорий
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]
    
    # Заполняем оставшуюся длину пароля случайными символами
    password += random.choices(all_characters, k=length - 4)
    
    # Перемешиваем пароль для случайности
    random.shuffle(password)
    
    return ''.join(password)

# Пример использования
print(generate_password())
