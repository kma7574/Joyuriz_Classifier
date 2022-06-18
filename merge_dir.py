import os
import shutil
import time

def read_all_file(path):
    output = os.listdir(path)  # 파일이름들 모음 naver_0000.jpg
    file_list = []

    for i in output:
        if os.path.isdir(path+"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)

    return file_list

def copy_all_file(file_list, new_path, title):
    try:
        os.mkdir(new_path)
    except:
        pass
    for src_path in file_list:
        file = src_path.split("/")[-1]
        shutil.copyfile(src_path, new_path+"/"+title+file)
        print("파일 {} 작업 완료".format(title+file)) # 작업한 파일명 출력
        
        
start_time = time.time() # 작업 시작 시간 

src_path1 = "./AutoCrawler/download/아이즈원 김채원" # 기존 폴더 경로
src_path2 = "./AutoCrawler/download/르세라핌 김채원"
new_path = "./AutoCrawler/download/kcw" # 옮길 폴더 경로

file_list1 = read_all_file(src_path1)
copy_all_file(file_list1, new_path, 'izone')
file_list2 = read_all_file(src_path2)
copy_all_file(file_list2, new_path, 'lesserafim')

print("=" * 40)
print("러닝 타임 : {}".format(time.time() - start_time)) # 총 소요시간 계산