import os
import pandas as pd

def search(dirname, result):
    filenames = os.listdir(dirname)  # ['face_cyn', 'face_jyr', 'face_kcw']
    for filename in filenames:
        lower = os.path.join(dirname, filename)
        if os.path.isdir(lower):
            search(lower, result)
        else:
            result.append(lower)
            
def labeling(paths):
    _label = []
    for path in paths:
        p = path.split('\\')[-1]
        if p.startswith('cyn'):
            _label.append(0)
        elif p.startswith('kcw'):
            _label.append(1)
        elif p.startswith('jyr'):
            _label.append(2)
        else:
            _label.append(3)
    return _label

all_path = []
search('./face_crop/', all_path)
label = labeling(all_path)

df_label = pd.DataFrame({'path' : all_path, 'label': label})