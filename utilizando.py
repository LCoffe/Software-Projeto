from ultralytics import YOLO
import cv2

# Arredonda o número em 2 casas depois do ponto
def arredonda(x):
    cont = x - int(x)
    cont = cont * 100 
    if(int(cont % 10) > 5):
        cont = (int(cont) - int(cont%10)) + 10
        cont = cont / 100
        x = int(x) + cont
    else:
        cont = int(cont)/100
        x = int(x) + cont
    
    return x


# Converte o valor em pixel para centimetros
def converte_pixel_cm(valor):
    return valor * 0.0264583333 # Valor de 1(um) pixel em cm 

# Calcula o diametro da fruta em centimetros
def calcula_tam(xMin, xMax):
    xMin = converte_pixel_cm(xMin)
    xMax = converte_pixel_cm(xMax)
    return xMax - xMin

# Inicializa o modelo já treinado da YOLO
model = YOLO('runs/detect/train/weights/best.pt')
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
                        save=True,
                        save_txt=True,  # Save bbox coordenation
                        save_conf=True,  # save_txt must be True
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
    
    if 'classId' in locals():
        # ClassId 0.0 = Laranja, ClassId 1.0 = Limão
        if(classId == 0.0):
            mensagem = f'A Laranja tem {tam} cm de diâmetro'
            print(mensagem)
        elif(classId == 1.0):
            mensagem = f'O Limão tem {tam} cm de diâmetro'
            print(mensagem)

        

# Libera a webcam
#webcam.release()
cv2.destroyAllWindows()
