from PIL import Image, ImageOps

def main():
  
    size = (1240,720)
    with Image.open("Assets/20250221_155239.jpg","wb") as f:
        ImageOps.contain(f,size).save("F_contaion.jpg")
        # ImageOps.cover(f,size).save("F_cover.jpg")
        # ImageOps.fit(f,size).save("F_fit.jpg")
        # ImageOps.pad(f,size,color="#f00").save("F_pad.jpg")
        # ImageOps.scale(f,2).save("F_scale.jpg")

    f.show()
main()