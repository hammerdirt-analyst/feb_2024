# imported methods from iqaasl
import pandas as pd
def convert_pixel_to_cm(file_name: str = None)-> ():
    im = PILImage.open(file_name)
    width, height = im.size
    dpi = im.info.get("dpi", (72, 72))
    width_cm = width / dpi[0] * 2.54
    height_cm = height / dpi[1] * 2.54
    
    return width_cm, height_cm

def combine_survey_files(list_of_files):

    files = []
    for afile in list_of_files:
        files.append(pd.read_csv(afile))
    return pd.concat(files)