from PIL import Image
import os

pic_list = ['.png', '.jpg']


#若寫成 for file in os.listdir('.')代表同階層資料夾裡面的檔案
#在與python檔案當同位置建立兩個資料夾orig & result
for file in os.listdir('orig'):
    for i in pic_list:
        if file.endswith(i):
            image_file = Image.open(os.path.join('orig', file)) #讀取在orig裡面的檔案，或是可寫成 Image.open('orig/' + file)
            image_file = image_file.convert('L') #讓圖片變成黑白
            image_file.save(os.path.join('result', file[:-4] + '_grey.png'))