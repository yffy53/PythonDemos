import cv2
import os
import numpy as np
from PIL import Image


def pic_compress_png(image_path, new_image_path):
    files = os.listdir(image_path)  # 获取当前目录下所有文件名
    files = np.sort(files)  # 按名称排序
    for f in files:
        print(f)
        #确保此处路径准确
        imgpath = image_path + '/' + f  # 路径＋文件名
        img = cv2.imread(imgpath)  # 读取图片
        if img is None:
            print("img = None")
            return None
        dirpath = new_image_path  # 压缩后储存路径
        file_name, file_extend = os.path.splitext(f)  # 将文件的名，后缀进行分割
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.png')  # 文件最终保存的路径及名字（名字和压缩前一致）
        print(os.path.join(dirpath, ".png"))  # 打印压缩缓存文件路径
        size = 70  # 输入你想要resize的高
        # 获取原始图像宽高
        height, width = img.shape[:2]
        # 等比例缩放尺度
        scale = height / size
        # 等比例缩放宽度
        width_size = int(width / scale)
        # resize
        shrink = cv2.resize(img, (width_size, size))
        cv2.imwrite(os.path.join(dirpath, ".png"), shrink, [cv2.IMWRITE_PNG_COMPRESSION, 1])  #对图像进行压缩
        # cv2.IMWRITE_PNG_COMPRESSION 压缩品质 0-10，数字越小压缩比越小
        img1 = Image.open(os.path.join(dirpath, ".png"))  # 打开压缩后的缓冲文件
        img1.save(dst, quality=70)  # 二次压缩，并保存位原始文件的文件名
        os.remove(os.path.join(dirpath, ".png"))  # 删除缓存文件


# 按下绿色按钮以运行脚本
if __name__ == '__main__':
    image_path = r'Cards'  #原始文件路径
    new_image_path = r'Cards'  #压缩后文件保存路径
    pic_compress_png(image_path, new_image_path)
    print("压缩成功")
