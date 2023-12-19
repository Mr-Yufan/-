import os

def rename_pdfs(folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 过滤出PDF文件
    pdf_files = [file for file in files if file.endswith('.xxx')]

    # 对PDF文件进行重新编号
    for i, pdf_file in enumerate(pdf_files, 1):
        # 构建新的文件名
        new_name = f"{i:03d}.xxx"
        # 构建文件的完整路径
        old_path = os.path.join(folder_path, pdf_file)
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件
        os.rename(old_path, new_path)

        print(f"文件已重命名: {pdf_file} -> {new_name}")

# 指定文件夹路径
folder_path = '//Users/xuyufan/Desktop/未命名文件夹'

# 调用函数进行文件重命名
rename_pdfs(folder_path)
