from ultralytics import YOLO
import cv2

# Inicializa o modelo já treinado da YOLO
model = YOLO('runs/detect/train/weights/best.pt')

# Arredonda o número em 2 casas depois do ponto
def arredonda(x):
    cont = x - int(x)
    cont = cont * 10
    x = int(x) + int(cont)/10
    
    return x


# Converte o valor em pixel para centimetros
def converte_pixel_cm(valor):
    return valor * 0.0264583333 # Valor de 1(um) pixel em cm 

# Calcula o diametro da fruta em centimetros
def calcula_tam(xMin, xMax):
    xMin = converte_pixel_cm(xMin)
    xMax = converte_pixel_cm(xMax)
    return xMax - xMin

def reconhecimento():
    # Inicializa a webcam
    #webcam = cv2.VideoCapture(0)

    # Verifica se a webcam inicializou corretamente
    if True:
        #valid, frame = webcam.read()
        #cv2.imwrite('foto.jpg', frame)

        # Pega o resultado da detetcção com a foto tirada pela webcam
        results_img = model.predict(source='limao.jpg',  # image or video; single value or a list; URL, PIL (RGB), CV2 (BGR), ...
                            conf=0.25,
                            iou=0.7,  # Non-Maximum Supression (NMS)
                            imgsz=640,
                            show=False,
                            save=False,
                            save_txt=False,  # Save bbox coordenation
                            save_conf=False,  # save_txt must be True
                            save_crop=False, # Save cropped prediction boxes
                            stream=False  # Do inference now (False) or after (True)
                            )

        # Usa o resultado para pega as coordenadas e o Id da detecção
        for det in results_img[0].boxes:
        # det é agora uma única detecção com atributos que pode ser utilizados.
            xmin, ymin, xmax, ymax = det.xyxy[0] # Coordenadas
            conf = det.conf[0] # Confidence
            classId = det.cls[0] # ID da fruta detectada
            tam = calcula_tam(xmin,xmax)
            tam = arredonda(tam)
            print(tam)
        
        if 'classId' in locals():
            # ClassId 0.0 = Laranja, ClassId 1.0 = Limão
            if(classId == 0.0):
                tam *= 10
                return tam
            elif(classId == 1.0):
                tam *= 10
                return tam + 128
            else:
                return 0 #Caso nao seja nenhuma das duas frutas

def main():
    return reconhecimento()

# Libera a webcam
#webcam.release()
cv2.destroyAllWindows()
