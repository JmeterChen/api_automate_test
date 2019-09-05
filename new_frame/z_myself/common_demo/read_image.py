# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-04


from PIL import Image  # 需要加载PIL库
import urllib.request
import pytesseract
from collections import defaultdict
import os


sep = os.sep
# # # url = 'http://202.119.81.113:8080/verifycode.servlet'  # 验证码URL
# url = 'https://shop.fangdd.com/api/boai/boai/user/authCode/image?uuid=794165f0-cf16-11e9-a280-a5e127001ced'
# r = urllib.request.urlopen(url)
# # # print(type(r))
# #
# # # 这里是将验证码图片写入到本地文件
# with open('photo.png', 'wb') as f:
# 	f.write(r.read())
# # print("-------图片保存成功-----")


# 获取图片中像素点数量最多的像素
def get_threshold(image):
    pixel_dict = defaultdict(int)

    # 像素及该像素出现次数的字典
    rows, cols = image.size
    for i in range(rows):
        for j in range(cols):
            pixel = image.getpixel((i, j))
            pixel_dict[pixel] += 1

    count_max = max(pixel_dict.values())  # 获取像素出现出多的次数
    pixel_dict_reverse = {v: k for k, v in pixel_dict.items()}
    threshold = pixel_dict_reverse[count_max]  # 获取出现次数最多的像素点

    return threshold


# 按照阈值进行二值化处理
# threshold: 像素阈值
def get_bin_table(threshold):
    # 获取灰度转二值的映射table
    table = []
    for i in range(256):
        rate = 0.1  # 在threshold的适当范围内进行处理
        if threshold*(1-rate) <= i <= threshold*(1+rate):
            table.append(1)
        else:
            table.append(0)
    return table


# 去掉二值化处理后的图片中的噪声点
def cut_noise(image):

    rows, cols = image.size  # 图片的宽度和高度
    change_pos = []  # 记录噪声点位置

    # 遍历图片中的每个点，除掉边缘
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # pixel_set用来记录该店附近的黑色像素的数量
            pixel_set = []
            # 取该点的邻域为以该点为中心的九宫格
            for m in range(i-1, i+2):
                for n in range(j-1, j+2):
                    if image.getpixel((m, n)) != 1:  # 1为白色,0位黑色
                        pixel_set.append(image.getpixel((m, n)))

            # 如果该位置的九宫内的黑色数量小于等于4，则判断为噪声
            if len(pixel_set) <= 4:
                change_pos.append((i, j))

    # 对相应位置进行像素修改，将噪声处的像素置为1（白色）
    for pos in change_pos:
        image.putpixel(pos, 1)

    return image  # 返回修改后的图片


# 识别图片中的数字加字母
# 传入参数为图片路径，返回结果为：识别结果
def OCR_lmj(img_path):

    image = Image.open(img_path)  # 打开图片文件
    imgry = image.convert('L')  # 转化为灰度图

    # 获取图片中的出现次数最多的像素，即为该图片的背景
    max_pixel = get_threshold(imgry)

    # 将图片进行二值化处理
    table = get_bin_table(threshold=max_pixel)
    out = imgry.point(table, '1')

    # 去掉图片中的噪声（孤立点）
    out = cut_noise(out)

    # 识别图片中的数字和字母
    txt = pytesseract.image_to_string(out)

    # 去掉识别结果中的特殊字符
    exclude_char_list = ' .:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥“”'
    txt = ''.join([x for x in txt if x not in exclude_char_list])
    
    return txt


def main():
    # 识别指定文件目录下的图片
	# 图片存放目录figures
    root_path = os.path.abspath(os.path.join(__file__, f"..{sep}.."))  # 项目根路径下
    dir_path = root_path + f'{sep}images'
	
    correct_count = 0  # 图片总数
    total_count = 0  # 识别正确的图片数量
    #  遍历figures下的png,jpg文件
    for file in os.listdir(dir_path):
        if file.endswith('.png') or file.endswith('.jpg'):
            # print(file)
            photo_path = '%s/%s' % (dir_path, file)  # 图片路径
            answer = file.split('.')[0]  # 图片名称，即图片中的正确文字
            result = OCR_lmj(photo_path)  # 图片识别的文字结果
            print((answer, result))
            if result == answer:  # 如果识别结果正确，则total_count加1
                correct_count += 1
                
            total_count += 1
	
    print('Total count: %d, correct: %d.' % (total_count, correct_count))
    print("验证码识别正确率为: %.2f" % ((correct_count/total_count)*100) + "%")
	
    '''
	# 单张图片识别
	image_path = 'E://figures/code (1).jpg'
	OCR_lmj(image_path)
	'''

main()
# if __name__ == '__main__':
#     root_path = os.path.abspath(os.path.join(__file__, f"..{sep}.."))  # 项目根路径下
#     dir_path = root_path + f'{sep}images'
#     image_path = dir_path + f'{sep}AACV.png'
#     print(image_path)
#     print(OCR_lmj(image_path))






