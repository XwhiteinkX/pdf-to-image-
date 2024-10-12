import fitz  # PyMuPDF
import os

# 取用绝对路径
def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

# 指定待转换pdf路径
directory = r"C:\Users\林夕\Downloads\pdf2image\pdf"
files = get_all_files(directory)

for file in files:
    pdf_path = file

    # 定义图片保存的路径（与PDF文件同名的文件夹）
    save_path = os.path.join(os.path.dirname(pdf_path), os.path.splitext(os.path.basename(pdf_path))[0])

    # 如果保存路径不存在，则创建该路径
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 打开PDF文件
    doc = fitz.open(pdf_path)

    # 遍历PDF的每一页
    for page_number in range(len(doc)):
        # 获取页面对象
        page = doc.load_page(page_number)

        # 将PDF页面转换为图片（pix对象）
        pix = page.get_pixmap(dpi=300)  # 设置DPI为300

        # 定义图片的保存路径和文件名
        image_path = os.path.join(save_path, f'page_{page_number + 1}.png')

        # 保存图片
        pix.save(image_path)

    # 关闭文档对象
    doc.close()

print("PDF转换完成。")
