from PIL import Image
im = Image.open('original.png')
w,h = im.size

size_list = [40,40*2,50,50*2,60,60*2,60*3,72,72*2,76,76*2,29,29*2,29*3,57,57*2]
size_name = ["icon-40","icon-40@2x","icon-50","icon-50@2x","icon-60","icon-60@2x","icon-60@3x","icon-72","icon-72@2x","icon-76","icon-76@2x","icon-small","icon-small@2x","icon-small@3x","icon.png","icon@2x"]

i = 0
for ss in size_list:
  size = size_list[i]
  im_after = im.resize((size,size))
  im_after.save(size_name[i]+".png")
  print("size_list : " + str(size_list[i]), end="")
  print(" / ", end="")
  print("size_name : " + size_name[i])
  i = i+1


