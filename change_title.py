import os

  
def change_title(person):
    file_path = 'face_crop/'
    file_name = os.listdir(file_path+'face_'+person)
    i = 1
    
    for name in file_name:
        src = os.path.join(file_path, 'face_'+person + '/' + name)
        dst = 'face_'+person + '/' + person + str(i) + '.jpg'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)
        i += 1
        
change_title('cyn')
change_title('jyr')
change_title('kcw')