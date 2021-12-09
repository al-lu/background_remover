from PIL import Image
import os
import os.path

os.getcwd()

directory = 'images/no_sound/'

# iterate over files in
# that directory
i = 0
for filename in os.listdir(directory):

    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        img = Image.open('{filen}'.format(filen=f))
        rgba = img.convert("RGBA")
        datas = rgba.getdata()

        newData = []
        for item in datas:
            # finding yellow colour
            if item[0] in range(40, 100) and item[1] in range(115, 165) and item[2] in range(120, 190):
                # replacing it with a transparent value
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        rgba.putdata(newData)
        rgba.save(
            "images/no_background/{}".format(f), "PNG", optimize=True)
        i += 1

    else:
        break

print("Done")
