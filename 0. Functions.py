from twocaptcha import TwoCaptcha
import urllib, os

class Functions():
    def Solver(self,img,text):
        urllib.request.urlretrieve(img, f'captcha{text}.png')
        api_key = os.getenv('1abc234de56fab7c89012d34e56fa7b8', '2a2b5480b431e8976a70ebbf3d38f550')
        solver = TwoCaptcha(api_key)
        result=solver.normal(f'./captcha{text}.png')
        return result.get('code')

    def dvFormatoAA1000(patente_ingresada, digito_verificador_ingresado):

        try:
            caracteres = list(patente_ingresada)
            patente_letras = caracteres[0]+caracteres[1]
            patente_numeros = caracteres[2]+caracteres[3]+caracteres[4]+caracteres[5]
            digitos_letras = ''
            digito_verificador = ''

            tabla_digitos = ['AA 001', 'BA 002', 'CA 003','EA 004', 'FA 005', 'GA 006','HA 007', 'AB 008', 'CB 009','EB 010', 'FB 011', 'GB 012','HB 013', 'AC 014', 'BC 015','EC 016', 'FC 017', 'GC 018','HC 019', 'BD 020', 'ED 021','FD 022', 'GD 023', 'HD 024','AE 025', 'BE 026', 'CE 027','EE 028', 'FE 029', 'GE 030','HE 031', 'AF 032', 'BF 033','CF 034', 'EF 035', 'FF 036','GF 037', 'HF 038', 'AG 039','BG 040', 'CG 041', 'EG 042','FG 043', 'HG 044', 'AH 045','BH 046', 'CH 047', 'EH 048','FH 049', 'GH 050', 'HH 051','AJ 052', 'BJ 053', 'CJ 054','EJ 055', 'FJ 056', 'GJ 057','HJ 058', 'BK 059', 'CK 060','EK 061', 'FK 062', 'GK 063','HK 064', 'AL 065', 'BL 066','CL 067', 'EL 068', 'FL 069','GL 070', 'HL 071', 'AN 072','BN 073', 'CN 074', 'EN 075','FN 076', 'GN 077', 'HN 078','AP 079', 'BP 080', 'CP 081','EP 082', 'FP 083', 'GP 084','HP 085', 'AR 086', 'BR 087','CR 088', 'ER 089', 'FR 090','GR 091', 'HR 092', 'AS 093','BS 094', 'CS 095', 'ES 096','FS 097', 'GS 098', 'HS 099',
                    'AT 100', 'BT 101', 'CT 102','ET 103', 'FT 104', 'GT 105','HT 106', 'AU 107', 'BU 108','CU 109', 'EU 110', 'FU 111','GU 112', 'HU 113', 'AV 114','BV 115', 'CV 116', 'EV 117','FV 118', 'GV 119', 'HV 120','AX 121', 'BX 122', 'CX 123','EX 124', 'FX 125', 'GX 126','HX 127', 'BY 128', 'CY 129','EY 130', 'FY 131', 'GY 132','HY 133', 'AZ 134', 'BZ 135','CZ 136', 'EZ 137', 'FZ 138','GZ 139', 'DA 140', 'DB 141','DD 142', 'DE 143', 'DF 144','DG 145', 'DH 146', 'DI 147','DJ 148', 'DK 149', 'DL 150','DN 151', 'DP 152', 'DR 153','DS 154', 'DT 155', 'DU 156','DV 157', 'DX 158', 'DY 159','DZ 160', 'KA 161', 'KB 162','KC 163', 'KD 164', 'KE 165','KF 166', 'KG 167', 'KH 168','KJ 169', 'KK 170', 'KL 171','KN 172', 'KP 173', 'KR 174','KS 175', 'KT 176', 'KU 177','KV 178', 'KX 179', 'KY 180','KZ 181', 'LA 182', 'LB 183','LC 184', 'LD 185', 'LE 186','LF 187', 'LG 188', 'LH 189','LJ 190', 'LK 191', 'LL 192','LN 193', 'LP 194', 'LR 195','LS 196', 'LT 197', 'LU 198','LV 199', 'LX 200', 'LY 201',
                    'LZ 202', 'NA 203', 'NB 204','NC 205', 'ND 206', 'NE 207','NF 208', 'NG 209', 'NH 210','NJ 211', 'NK 212', 'NL 213','NN 214', 'NP 215', 'NR 216','NS 217', 'NT 218', 'NU 219','NV 220', 'NY 221', 'NZ 222','PA 223', 'PB 224', 'PC 225','PD 226', 'PE 227', 'PF 228','PG 229', 'PH 230', 'PJ 231','PK 232', 'PL 233', 'PN 234','PP 235', 'PS 236', 'PT 237','PU 238', 'PV 239', 'PX 240','PY 241', 'PZ 242', 'NX 243','RA 244', 'RB 245', 'RC 246','RD 247', 'RE 248', 'RF 249','RG 250', 'RH 251', 'RJ 252','RK 253', 'RL 254', 'RN 255','RP 256', 'RR 257', 'RS 258','RT 259', 'RU 260', 'RV 261','RX 262', 'RY 263', 'RZ 264','HZ 265', 'SA 266', 'SB 267','SC 268', 'SD 269', 'SE 270','SF 271', 'SG 272', 'SH 273','SJ 274', 'SK 275', 'SL 276','SN 277', 'SP 278', 'SR 279','SS 280', 'ST 281', 'SU 282','SV 283', 'SX 284', 'SY 285','SZ 286', 'TA 287', 'TB 288','TC 289', 'TD 290', 'TE 291','TF 292', 'TG 293', 'TH 294','TJ 295', 'TK 296', 'TL 297','TN 298', 'TP 299', 'TR 300',
                    'TS 301', 'TT 302', 'TU 303','TV 304', 'TX 305', 'TY 306','TZ 307', 'UA 308', 'UB 309','UC 310', 'UD 311', 'UE 312','UF 313', 'UG 314', 'UH 315','UJ 316', 'UK 317', 'UL 318','UN 319', 'UP 320', 'UR 321','US 322', 'UT 323', 'UU 324','UV 325', 'UX 326', 'UY 327','UZ 328', 'VA 329', 'VB 330','VC 331', 'VD 332', 'VE 333','VF 334', 'VG 335', 'VH 336','VJ 337', 'VK 338', 'VL 339','VN 340', 'VP 341', 'VR 342','VS 343', 'VT 344', 'VU 345','VV 346', 'VX 347', 'VY 348','VZ 349', 'XA 350', 'XB 351','XC 352', 'XD 353', 'XE 354','XF 355', 'XG 356', 'XH 357','XJ 358', 'XK 359', 'XL 360','XM 361', 'XN 362', 'XP 363','XQ 364', 'XR 365', 'XS 366','XT 367', 'XU 368', 'XV 369','XX 370', 'XY 371', 'XZ 372','YA 373', 'YB 374', 'JA 375','JB 376', 'JC 377', 'JD 378','JE 379', 'YC 380', 'YD 381','YE 382', 'YF 383', 'YG 384','YH 385', 'YJ 386', 'YK 387','YL 388', 'YN 389', 'YP 390','YR 391', 'YS 392', 'YT 393','YU 394', 'YV 395', 'YX 396','YY 397', 'YZ 398', 'ZA 399','ZB 400', 'ZC 401', 'ZD 402',
                    'ZE 403', 'ZF 404', 'ZG 405','ZH 406', 'ZI 407', 'ZJ 408','ZK 409', 'ZL 410', 'JF 411','JG 412', 'JH 413', 'ZN 414','ZP 415', 'ZR 416', 'ZS 417','ZT 418', 'ZU 419', 'ZV 420','ZX 421', 'ZY 422', 'ZZ 423','WA 430', 'WB 431', 'WC 432','WD 433', 'WE 434', 'WF 435','WG 436', 'WH 437', 'WJ 438','WK 439', 'WL 440', 'WN 441','WP 442', 'WR 443', 'WS 444','WT 445', 'WU 446', 'JJ 447','JK 448', 'WV 449', 'WW 450','WX 451', 'WY 452', 'WZ 453','ZW 454', 'YW 455', 'XW 456','UW 457', 'TW 458', 'SW 459','RW 460', 'PW 461', 'NW 462','LW 463', 'KW 464', 'MZ 465','MY 466', 'MX 467', 'MV 468','MU 469', 'MT 470', 'MS 471','JL 424', 'JN 425', 'JO 426','JP 427', 'JR 428', 'JS 429','JT 472', 'JU 473', 'JV 474','JW 475', 'JX 476', 'JY 477','JZ 478', 'MA 479', 'MB 480','MC 481', 'MD 482', 'ME 483','MF 484', 'MG 485', 'MH 486','MJ 487', 'MK 488', 'ML 489','MN 490', 'MP 491', 'MR 492','IA 493', 'IB 494', 'IC 495','ID 496', 'IE 497', 'IF 498','IG 499', 'IH 500', 'IJ 501',
                    'IK 502', 'IL 503', 'IN 504','IO 505', 'IP 506', 'IR 507','IS 508', 'IT 509', 'IU 510','IV 511', 'IW 512', 'IX 513','IY 514', 'IZ 515', 'QA 516','QB 517', 'QC 518', 'QD 519','QE 520', 'QF 521', 'QG 522','QH 523', 'QJ 524', 'QK 525','QL 526', 'QN 527', 'QO 528','QP 529', 'QR 530', 'QS 531','QT 532', 'QU 533', 'QV 534','QW 535', 'QX 536', 'QY 537','QZ 538', 'OA 539', 'OB 540','OC 541', 'OD 542', 'OE 543','OF 544', 'OG 545', 'OH 546','OJ 547', 'OK 548', 'OL 549','ON 550', 'OO 551', 'OP 552','OR 553', 'OS 554', 'OT 555','OU 556', 'OV 557', 'OW 558','OX 559', 'OY 560', 'OZ 561','AD 562', 'AI 563', 'AK 564','AM 565', 'AW 566', 'AY 567','BB 568', 'BI 569', 'BM 570','BO 571', 'BW 572', 'CC 573','CD 574', 'CI 575', 'CM 576','CO 577', 'CW 578', 'DC 579','DM 580', 'DO 581', 'DW 582']

            for i in tabla_digitos:
                if(i.split(' ')[0]==patente_letras):
                    digitos_letras = i.split(' ')[1]

            digitos = list(digitos_letras+patente_numeros)
            suma = int(digitos[0])*2+int(digitos[1])*7+int(digitos[2])*6+int(digitos[3])*5+int(digitos[4])*4+int(digitos[5])*3+int(digitos[6])*2
            resto_inicial = suma%11
            resto_final = 11-resto_inicial

            if(resto_final==11):
                digito_verificador='0'
            elif(resto_final==10):
                digito_verificador='K'
            else:
                digito_verificador=str(resto_final)

            if(str(digito_verificador)==digito_verificador_ingresado):
                return True
            
            else:
                return False

        except:
            return False

    def dvNuevoFormatoPPU(patente_ingresada, digito_verificador_ingresado):
        
        try:
            caracteres = list(patente_ingresada)
            patente_letras = caracteres[0]+caracteres[1]+caracteres[2]+caracteres[3]
            patente_numeros = caracteres[4]+caracteres[5]
            numero_asignado_letras = ''
            digito_verificador = ''

            tabla_digitos = ['B 1','C 2','D 3','F 4','G 5','H 6','J 7','K 8','L 9','P 0','R 2','S 3','T 4','V 5','W 6','X 7','Y 8','Z 9']

            for letra in patente_letras:
                for digito in tabla_digitos:
                    if(letra==digito.split(' ')[0]):
                        numero_asignado_letras = numero_asignado_letras+digito.split(' ')[1]

            digitos_aux = list(numero_asignado_letras+patente_numeros)
            digitos = []
            for i in digitos_aux:
                digitos.append(int(i))

            suma = digitos[0]*7+digitos[1]*6+digitos[2]*5+digitos[3]*4+digitos[4]*3+digitos[5]*2
            resto = suma%11

            if(resto==0):
                digito_verificador='0'
            else:
                resto = 11-resto
                if(resto==10):
                    digito_verificador='K'
                else:
                    digito_verificador=str(resto)

            if(digito_verificador==digito_verificador_ingresado):
                return True
            else:
                return False

        except:
            return False

    def dvNuevoFormatoPPUMotos(patente_ingresada, digito_verificador_ingresado):

        try:
            caracteres = list(patente_ingresada)
            patente_letras = caracteres[0]+caracteres[1]+caracteres[2]
            patente_numeros = caracteres[3]+caracteres[4]
            numero_asignado_letras = ''
            digito_verificador = ''

            tabla_digitos = ['B 1','C 2','D 3','F 4','G 5','H 6','J 7','K 8','L 9','P 0','R 2','S 3','T 4','V 5','W 6','X 7','Y 8','Z 9']

            for letra in patente_letras:
                for digito in tabla_digitos:
                    if(letra==digito.split(' ')[0]):
                        numero_asignado_letras = numero_asignado_letras+digito.split(' ')[1]

            digitos_aux = list(numero_asignado_letras+'0'+patente_numeros)
            digitos = []
            for i in digitos_aux:
                digitos.append(int(i))

            suma = digitos[0]*7+digitos[1]*6+digitos[2]*5+digitos[3]*4+digitos[4]*3+digitos[5]*2
            resto = suma%11

            if(resto==0):
                digito_verificador='0'
            else:
                resto = 11-resto
                if(resto==10):
                    digito_verificador='K'
                else:
                    digito_verificador=str(resto)

            if(digito_verificador==digito_verificador_ingresado):
                return True
            else:
                return False

        except:
            return False

if __name__ == '__main__':
    #True
    print(Functions.dvFormatoAA1000('WG2532', '2'))
    print(Functions.dvNuevoFormatoPPU('HCZX54','4'))
    print(Functions.dvNuevoFormatoPPUMotos('ZZZ99','2'))