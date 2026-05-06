from PIL import Image
from numpy.ma.core import resize

def wm(img, wm_path, out, pos='br', op=128, s=0.15):
    i=Image.open(img).convert('RGBA')
    w=Image.open(wm_path).convert('RGBA')

    new_width = int(i.width * s)
    new_height = int(w.height * new_width / w.width)

    w = w.resize((new_width, new_height))
    w.putalpha(w.split()[3].point(lambda p:p*op//255))

    if pos == 'br':
        x, y=(i.width-w.width-20,i.height-w.height-20)
    else: x, y = 20, 20

    i.paste(w, (x,y), w)
    i.convert('RGB').save(out)
wm("1.jpg","2.jpg", 'result.jpg')