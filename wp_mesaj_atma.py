import webbrowser
import pyautogui
import time
import keyboard

def send_whatsapp_messages(phone_number, message, repeat, delay_ms, language):
    # WhatsApp Web'i aç
    webbrowser.open(f'https://web.whatsapp.com/send?phone={phone_number}')
    time.sleep(5)  # WhatsApp Web'in yüklenmesi için bekleyin

    if language == "turkish":
        # Türkçe klavye düzenini seç
        keyboard.press_and_release('alt+shift')  # Türkçe klavyeye geçiş
    elif language == "arabic":
        # Arapça klavye düzenini seç
        keyboard.press_and_release('alt+shift')  # Arapça klavyeye geçiş

    for _ in range(repeat):
        # Mesajı yaz ve Enter tuşuna basarak gönder
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(delay_ms / 1000.0)  # Mesajlar arasında milisaniyeler bekle

    # Eski klavye düzenine geri dön
    keyboard.press_and_release('alt+shift')  # Eski klavyeye dönüş

# Telefon numarası ve mesaj bilgileri
phone_number = ""  # Alıcının telefon numarası
message = ""  # Gönderilecek mesaj
repeat = 1000  # Mesajın kaç kez gönderileceği
delay_ms = 100  # Milisaniye cinsinden bekleme süresi (örneğin, 100 ms = 0.1 saniye)
language = "turkish"  # Dil seçimi 

send_whatsapp_messages(phone_number, message, repeat, delay_ms, language)
