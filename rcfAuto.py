from ultralytics.data.annotator import auto_annotate
import numpy as np

#Modelo Yolo de detecção
yolo_model= 'runs/detect/train/weights/best.pt'

# Função de conversão de pixels para centímetros
def convert_pixel_cm(value):
    return value * 0.0264583333

def rounded(x):
    cont = x - int(x)
    cont = cont * 10
    x = int(x) + int(cont)/10
    
    return x*10

def get_min_max_coordinates(mask):
    x_values = [point[0] for point in mask]
    y_values = [point[1] for point in mask]
    
    x_min = min(x_values)
    x_max = max(x_values)
    y_min = min(y_values)
    y_max = max(y_values)
    
    return x_min, x_max, y_min, y_max

def calculate_diameter(mask):
    x_min, x_max, y_min, y_max = get_min_max_coordinates(mask[0])
    sum = (x_max - x_min) + (y_max - y_min)
    return sum / 2

def reconhecimento():
    mask, class_id = auto_annotate(data = 'foto.jpg',det_model = yolo_model, sam_model = 'sam_b.pt')

    diameter = calculate_diameter(mask)
    diameter = convert_pixel_cm(diameter)
    diameter = rounded(diameter)
    print(f"Diametro da fruta: {diameter} mm")

    if(class_id == 0):
        return int(diameter)
    elif(class_id == 1):
        return int(diameter) + 128
    else:
        return 0
    
def main():
    return reconhecimento()