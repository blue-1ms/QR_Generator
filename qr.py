# import qrcode lib
import qrcode
 
# link to convert
data = input("link to convert: ")
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
qr.make(fit = True)

# colour of qrcode
img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
 
# save file as, .png attribute after name
img.save(input('inputname: '))
