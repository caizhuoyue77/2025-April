import os
import shutil

def match_and_cleanup(directory: str) -> None:
    """
    遍历给定目录，匹配子文件夹和JSON文件名。如果没有匹配的文件夹或JSON文件，删除它们。
    
    参数:
    directory (str): 要遍历的主目录路径
    """
    try:
        # 获取主目录下的所有文件和文件夹
        all_items = os.listdir(directory)
        
        # 将子文件夹和json文件分开
        subfolders = [item for item in all_items if os.path.isdir(os.path.join(directory, item))]
        json_files = [item for item in all_items if item.endswith('.json')]

        # 将文件名去掉扩展名后进行匹配
        json_file_names = [os.path.splitext(json_file)[0] for json_file in json_files]

        # 遍历子文件夹
        for folder in subfolders:
            # 如果文件夹名不在json文件名列表中，删除文件夹
            if folder not in json_file_names:
                folder_path = os.path.join(directory, folder)
                shutil.rmtree(folder_path)  # 递归删除文件夹
                print(f"已删除未匹配的文件夹: {folder}")

        # 遍历json文件
        for json_file in json_files:
            json_name = os.path.splitext(json_file)[0]  # 去掉扩展名
            # 如果json文件名不在子文件夹列表中，删除json文件
            if json_name not in subfolders:
                json_file_path = os.path.join(directory, json_file)
                os.remove(json_file_path)  # 删除文件
                print(f"已删除未匹配的JSON文件: {json_file}")

    except FileNotFoundError as fnf_error:
        print(f"目录未找到: {fnf_error}")
    except PermissionError as perm_error:
        print(f"权限不足: {perm_error}")
    except Exception as e:
        print(f"出现错误: {e}")

def process_all_subdirectories(main_directory: str) -> None:
    """
    遍历主目录下的所有子文件夹，对每个子文件夹调用 match_and_cleanup。
    
    参数:
    main_directory (str): 主目录路径
    """
    try:
        # 获取主目录下的所有文件和文件夹
        subdirs = [os.path.join(main_directory, item) for item in os.listdir(main_directory) if os.path.isdir(os.path.join(main_directory, item))]
        
        # 遍历每个子文件夹，执行匹配和清理操作
        for subdir in subdirs:
            print(f"处理文件夹: {subdir}")
            match_and_cleanup(subdir)
    
    except FileNotFoundError as fnf_error:
        print(f"主目录未找到: {fnf_error}")
    except PermissionError as perm_error:
        print(f"权限不足: {perm_error}")
    except Exception as e:
        print(f"出现错误: {e}")

if __name__ == "__main__":
    # 你要遍历的主目录路径
    root_directory = "/Users/caizhuoyue/Desktop/热血毕业/RapidAPIHub-sample/tools"
    process_all_subdirectories(root_directory)