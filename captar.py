#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  snapshot.py
# 
#  Copyright 2017 tavares <tavares@tavares-Inspiron-5558>
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 
# 
import cv2
import time
 
def main(args):
 
    camera_port = 0
  
    nFrames = 30
  
    camera = cv2.VideoCapture(camera_port)
     
    file = "/home/marcos/imagenTeste.png"
         
    print "Digite <ESC> para sair / <s> para Salvar"   
     
    emLoop= True
      
    while(emLoop):
     
        retval, img = camera.read()
        cv2.imshow('Foto',img)
     
        k = cv2.waitKey(100)
     
        if k == 27:
            emLoop= False
         
        elif k == ord('s'):
            cv2.imwrite(file,img)
            emLoop= False
     
    cv2.destroyAllWindows()
    camera.release()
    return 0
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
