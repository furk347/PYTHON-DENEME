import secrets
import string

def generate_strong_password():
    print("Şifrenizin güçlü olması için bazı bilgilere ihtiyacımız var.")
    while True:
        name = input("Adınız nedir? ").strip().capitalize()
        birth_year = input("Doğum yılınız nedir? ")
        favorite_color = input("En sevdiğiniz renk nedir? ").strip().capitalize()
        
        # Şifre uzunluğunu kullanıcıya sor
        while True:
            try:
                length = int(input("Şifre uzunluğunu girin: "))
                if length < 8:
                    print("Şifre en az 8 karakter uzunluğunda olmalıdır.")
                else:
                    break
            except ValueError:
                print("Geçersiz bir değer girdiniz. Lütfen bir tam sayı girin.")

        # Rastgele karakterler ekle
        additional_characters = '!@#$%^&*()-_=+'
        password_candidate = name + ''.join(secrets.choice(additional_characters) for _ in range(1)) + birth_year + ''.join(secrets.choice(additional_characters) for _ in range(1)) + favorite_color + ''.join(secrets.choice(additional_characters) for _ in range(1)) + ''.join(secrets.choice(additional_characters) for _ in range(1))

        # Şifre kriterlerini kontrol et
        if (any(c.islower() for c in password_candidate)
                and any(c.isupper() for c in password_candidate)
                and sum(c.isdigit() for c in password_candidate) >= 3
                and any(c in string.punctuation for c in password_candidate)):
            break
        else:
            print("Şifreniz güçlü değil, lütfen farklı bilgiler girin.")

    return password_candidate

# Güçlü bir şifre oluştur
generated_password = generate_strong_password()
print("Oluşturulan güçlü şifre:", generated_password)