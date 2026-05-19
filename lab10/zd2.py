from PIL import Image
cards={
    "Новый год": "ng.jpg",
    "День рождеия":"dr.jpg",
    "8 марта": "download.jpg"
}
a = input("К какому празднику вам нужна открытка?")
if a in cards:
    file= cards[a]
    Imageshow= Image.open(file)
    Imageshow.show()