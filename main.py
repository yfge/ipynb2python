import os
import sys
import nbformat




def extract_python_code_from_ipynb(ipynb_file, output_file):
   # 读取ipynb文件
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)
   
   # 提取python代码
    python_code = ""
    for cell in nb.cells:
        if cell.cell_type == 'code':
            python_code += cell.source + '\n\n'
    
    # 保存为文档
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(python_code)


def main():
    # 从命令行第一个参数获取文件夹路径
    folder = sys.argv[1]
    ipynb_files = []
    # 从命令行第二个参数获取输出文件夹路径
    output_folder = sys.argv[2]

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".ipynb"):
                
                
                ipynb_file = os.path.join(root, file)
                python_folder = os.path.join(output_folder, root.split("/")[-1])
                if not os.path.exists(python_folder):
                    os.makedirs(python_folder)
                
                output_file = os.path.join(python_folder, file.replace(".ipynb", ".py"))

                try:
                    extract_python_code_from_ipynb(ipynb_file,  output_file.replace(".ipynb", ".py"))
                except Exception as e:
                    print(f"Error: {ipynb_file}")
                    print(e)
                print(ipynb_file)


    # 读取ipynb文件
    # 将ipynb文件转换为py文件

if __name__ == '__main__':
    main()