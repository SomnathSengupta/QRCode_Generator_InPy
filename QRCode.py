import qrcode  as qr
print("Welcome to Your Personalized QR Code Generator!!!")
url = input("Enter the url: ")
img = qr.make(url)
name = input("Enter the file name to saved: ")
img.save(name + ".png")