import qrcode

url = "https://lemon-flower-04f666310.3.azurestaticapps.net"
nome_arquivo = "qr_code.png"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

imagem_qr = qr.make_image(fill='black', back_color='white')
imagem_qr.save(nome_arquivo)

print("QR Code gerado com sucesso!")
