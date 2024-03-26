meme_dict = {
    "LOL": "Komik bir şeye verilen cevap",
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}

while True:
    words = list(meme_dict.keys())[:5]  # Sözlükten rastgele 5 kelime alınır
    print("Aşağıdaki kelimelerden birinin anlamını isteyin:")
    for word in words:
        print("-", word)
    
    user_input = input("Bir kelime yazın veya çıkmak için 'exit' yazın: ").strip().upper()
    
    if user_input == 'EXIT':
        print("Programdan çıkılıyor...")
        break
    elif user_input in meme_dict:
        print(meme_dict[user_input])
    else:
        print("Bu kelimeyi sözlükte bulamadım. Lütfen listedeki kelimelerden birini girin.")
