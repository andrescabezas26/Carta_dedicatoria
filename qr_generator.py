import qrcode

url = "https://andrescabezas26.github.io/Carta_dedicatoria/"

img = qrcode.make(url)
img.save("codigo_qr.png")