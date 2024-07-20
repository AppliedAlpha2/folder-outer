import os
import shutil

# 현재 작업 디렉토리를 가져옵니다.
current_dir = os.getcwd()

# 현재 디렉토리 안의 모든 파일과 폴더를 검사합니다.
for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    
    # 폴더인 경우
    if os.path.isdir(item_path):
        # 하위 폴더의 모든 파일을 현재 디렉토리로 이동합니다.
        for root, dirs, files in os.walk(item_path):
            for file in files:
                file_path = os.path.join(root, file)
                shutil.move(file_path, current_dir)
        
        # 빈 폴더를 삭제합니다.
        shutil.rmtree(item_path)

print(">>> 모든 파일이 현재 폴더로 이동되고 하위 폴더가 삭제되었습니다.")