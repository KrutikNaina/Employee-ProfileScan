import qrcode

def generate_qr(eid):
    qr = qrcode.make(eid)
    qr.save(f"media/qrcodes/{eid}.png")
