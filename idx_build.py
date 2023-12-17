import os


def generate_splits(root_dir):
    """
    生成splits文件
    :param root_dir: 根目录
    """
    with open("splits.txt", "w") as splits_file:
        for subdir_name in os.listdir(root_dir):
            subdir_path = os.path.join(root_dir, subdir_name)

            # 检查是否是目录
            if os.path.isdir(subdir_path):
                for idx, image_name in enumerate(os.listdir(subdir_path), start=1):
                    image_path = os.path.join(subdir_path, image_name)

                    # 将信息写入splits文件
                    splits_file.write(f"{subdir_name}#{idx}#{image_path}\n")


# 示例用法
root_directory = "data"
generate_splits(root_directory)








