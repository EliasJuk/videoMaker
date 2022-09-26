import cv2  # pip install opencv-python 
import os 
from os.path import isfile, join

class VideoMaker():
  def __init__(self):
    # CONSTANTES
    self.frame_array=[]
    self.files = []

    # DIRETORIOS
    local = os.getcwd()
    directory= local + '/'                # Diretório raiz
    pathIn=directory+'img/'               # Diretório onde ficam as imagens
    pathOut=directory+'output/video.mp4'  # Saida - onde ficam os videos

    # CONFIGURAÇÔES
    fps=1
    time=20 # DURAÇÃO DE CADA IMAGEM NO VIDEO
    
    # INICIALIZAÇÃO
    self.convert_pictures_to_video(pathIn, pathOut, fps, time)

  def convert_pictures_to_video(self, pathIn, pathOut, fps, time):
    # ACESSA A PASTA COM AS IMAGENS E ARMAZENA O NOME EM UM ARRAY
    for file in os.listdir(pathIn):
      if isfile(join(pathIn,file)):
        self.files.append(file)

    # LER AS IMAGENS
    for i in range (len(self.files)):
      filename=pathIn+self.files[i]

      # LER AS IMAGENS
      img=cv2.imread(filename)
      # img=cv2.resize(img,(1400,1000))
      height, width, layers = img.shape
      size=(width,height)

      # FRAME ARRAY
      for k in range (time):
        self.frame_array.append(img)
    

    out=cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps,size)

    for i in range(len(self.frame_array)):
      out.write(self.frame_array[i])

    out.release()
    print('Video criado com SUCESSO!')


if __name__ == '__main__':
  app = VideoMaker()