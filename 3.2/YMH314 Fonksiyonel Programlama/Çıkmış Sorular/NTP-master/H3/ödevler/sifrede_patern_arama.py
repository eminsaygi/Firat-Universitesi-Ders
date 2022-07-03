#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
100 adet 8 karakterli rastgele oluşturulan şifreler içinde yanyana iki rakam olanları bulur
"""

#sifre listesi
liste=['3e!qpdRS', '64Ql8hl#', 'Y!Bj9qcn', 'MR!p6NSy', '!7afF%4!', 'ycdZ*Z4K', 'sk*#P9dG', 'hZ7hjL#6', '#J3iO!oh', '!4%hGtjE', 'c6jPMs%5', '?ELt8!zz', '0DO#eFGx', 'JtJ?b3uY', 'WP5v#Q38', '!phv3?JJ', '55TpT!*S', 'vZzrP3*0', 'vZd#Q6v?', 'BEn#V1!I', '0ZQU?22h', '4I*n3IJV', 'YJz2%JZ?', 'D*xn259e', 'E#lHht0M', 'Q7DO#0cY', '*Memzh*2', 'WuW?Hp96', 'PeH*O06a', 'yRcXbQ6#', '?aTQ7?T0', 'jBL%6#cr', 'ba*AZ7Xd', '#m7UUNwz', '4s!zaEGf', '7Ev*q%tL', '1M7*etiB', 'oo!BEi4?', '8ov71K*R', 'tH7m1#ys', '5Gzs2!#i', 'BByGe9*u', 'V5nIW?As', '9H?ehNxf', '%?vWYH1E', 'M8kuUfP*', '6DWyo?aV', '*Cs09Df#', 'kJ7!0Jqn', '*QpNTP97', 'Y8UY#a3s', '*ul922HX', '3Uj*CXcN', '%5GFvYgy', 'OI08trp#', 'ub0Ea4N%', '5%Fm0B4X', 'mT*64F#%', 'ZpaGKr*4', '9KRhzY#5', '?zkH86Br', 'Zwz6fX?S', 'y*Ii8gM3', 'gOn#G98z', 'W7#PkpMD', 'V#!t28bo', 'UExen7j!', 'w%y!wC83', 'l64O#C#n', 'WV2PyM!%', '91H*axTX', 'Dt!G#Xj8', '!q5FoTld', 'rc9!5Ory', '4OmVi%O3', 'pV68uEg?', 'a*1DL03N', 'B3aNGk!u', '0HrtuxG#', 'l5OmAd%B', 'wuA97O!c', 'pV6xD?AN', '7MBtne*o', '#VQfu3d7', 'ZN!W?iJ3', 'Eo554lT?', 'jsdA?3dS', 'VoNA2?a?', '8aG?39Ol', 'BFW#rin6', '?*Hq4gab', '9!O1xtEC', 'Vxf0s!f7', 'CTSa#0jz', 'Yk?o4Md3', '7cRei1W?', '#6SoSatD', '*PAbbn9M', '%i2c?3ZP', 'SLuf*#a2']

for s in liste:
    for x in s:
        #Karakter digitse ve stringin son karakteri değilse bir sonraki karakteri kontrol et
        if x.isdigit() and (s.index(x)< len (s)-1 ):
            if s[s.index(x)+1].isdigit():
                #Bir sonraki karakterde digits ise ekrana bas ve break ile çık
                print s, "yanyana 2 rakam var"
                break
            