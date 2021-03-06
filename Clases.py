import json, time, os, urllib
from pip._vendor import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from twocaptcha import TwoCaptcha

#lista_patentes=['CKFL14', 'KXPS43', 'PHSS63', 'XF7651', 'JLWF50', 'CZCX24', 'TC2442', 'CPLH89', 'LTZ011', 'HWLF62', 'CBKV63', 'LYCH67', 'HKTW30', 'DFBG70', 'BI0875', 'LDY042', 'FTD049', 'WF5936', 'CFSC19', 'HPKP41', 'VE7020', 'BWDR40', 'BFDL17', 'PS7532', 'BXDY16', 'BBRL36', 'BPRV37', 'ZW9270', 'YH8274', 'DSBX73', 'SD4437', 'VD5486', 'TJ2248', 'ZD4101', 'GPR092', 'LFB012', 'YW4448', 'FP7732', 'DJLR32', 'SV7591', 'LG7679', 'KSWB78', 'HHYW27', 'WL0100', 'GYD099', 'KK8693', 'JPYK29', 'KXPP51', 'GLKD79', 'UY6416', 'ED6761', 'JFKK59', 'WG2532', 'KW7915', 'BGD021', 'FKRR71', 'JCBV97', 'JXD084', 'GY8298', 'KRLC41', 'YR0403', 'BWSR23', 'YG2586', 'XC4499', 'DYJP22', 'GTRR68', 'CGFY25', 'ZB7546', 'FXKK99', 'LRCW17', 'KJWK97', 'JPKS44', 'DHSL81', 'BHZK99', 'UE0649', 'FSHR31', 'LHGH69', 'LSXB75', 'HYJ025', 'GGCF74', 'PG5945', 'KGZB62', 'HRTB99', 'DHV013', 'GPF070', 'GCZK17', 'SU9716', 'CBYB72', 'CWWR43', 'LKDZ91', 'CKVS68', 'LV2755', 'GGGB47', 'EE8342', 'DZDZ48', 'HKP045', 'LR2813', 'JRRJ13', 'WB3923', 'DLX035', 'KFPR52', 'BD6139', 'LXPX30', 'DPF068', 'GGFZ69', 'CRLT12', 'CFVB55', 'JXBW26', 'HDJY17', 'JDYG86', 'FHRF34', 'BZKK47', 'KTCH36', 'KXJD90', 'KGT040', 'DJGH61', 'WK0220', 'LPJH14', 'CPTH49', 'WK0637', 'CCJC40', 'WK7854', 'FLSS16', 'WB3994', 'WW4000', 'SD2996', 'LLSX48', 'FDK014', 'HPDW71', 'KVLY79', 'HJHT22', 'FYJJ29', 'LCCY83', 'ZX1227', 'WL4499', 'DBVH42', 'JWVT67', 'WB7258', 'DYCF71', 'NR0364', 'FBGG46', 'CVPP53', 'GXYT43', 'BVKH13', 'CYXZ34', 'KK8337', 'GDJK17', 'VR9229', 'NF2417', 'DX7389', 'FPLX76', 'RT2943', 'ZY4092', 'HKCB50', 'CGXZ27', 'VV9606', 'YT5012', 'XG5973', 'KGHX97', 'YV7398', 'FKGJ96', 'KKZJ39', 'DBTZ25', 'HKTV27', 'CCGH83', 'GYS092', 'UT8872', 'DDBD17', 'DSZG88', 'DBDK99', 'KTHV37', 'CPRK17', 'HTVT12', 'KS0852', 'CKGK80', 'QL0885', 'LS2484', 'KWSP28', 'JFKW46', 'WK9995', 'LLPX65', 'UN0384', 'DPJG58', 'LHDB85', 'LTPF27', 'KGH047', 'FDRG49', 'RW5289', 'BCR031', 'LSWW93', 'GSZB46', 'LTVJ41', 'BXJB48', 'HHSL37', 'JD0509', 'HYBP90', 'UG6239', 'BXSP64', 'PC6312', 'KT1046', 'BSTL76', 'KTPF65', 'CLZK25', 'KCPW61', 'RP8576', 'VZ6997', 'KLBJ58', 'WY4231', 'KH4878', 'DVGY65', 'LXBL35', 'BGS065', 'JXFL75', 'BYYL42', 'JCLL52', 'KZTS68', 'DZZX64', 'XF4131', 'FSKZ53', 'NE9952', 'JWTZ94', 'JYXJ49', 'YT2598', 'KRTG35', 'JKHV11', 'WZ5936', 'DXZZ71', 'FBTD79', 'ZY4313', 'JWGD90', 'JHTP61', 'XD1946', 'UH7384', 'LSTS13', 'CTWX77', 'FLBS46', 'LLZD13', 'JZTZ44', 'HJFT18', 'GBY078', 'TG5204', 'KTRY76', 'GCFH23', 'NC5093', 'WU9402', 'CTVF29', 'RR1601', 'GRZ045', 'KTDP50', 'DN5078', 'LFZ060', 'GWHP33', 'BCJP46', 'CJZZ41', 'SX5531', 'ZL3706', 'WE9030', 'CSJC87', 'HJZ073', 'OW0214', 'HWFL68', 'HFBF78', 'LHKW76', 'GXDX66', 'DJZJ56', 'TJ2673', 'WE9401', 'GN8893', 'VH8584', 'FVTT87', 'BFLH77', 'GZ7035', 'FLC060', 'LFRF19', 'DS9370', 'DD5495', 'JWSS57', 'XP0825', 'DPC062', 'JRW071', 'LS8370', 'LBGB61', 'NV3646', 'LVYZ15', 'FLGH58', 'HSW078', 'DYTF21', 'JHDW92', 'KKVG27', 'CSXS77', 'CLCP61', 'XF7794', 'BDF019', 'FXPX64', 'BSZW75', 'LB8361', 'KXGP72', 'PJ1416', 'KZJC56', 'AA3565', 'HRVP22', 'RR4674', 'DHLV93', 'MY6693', 'GFRD40', 'BSB024', 'FZTJ81', 'SP2634', 'LS4566', 'KJZR11', 'QR0929', 'CBKZ44', 'TD1370', 'VF4896', 'YA9953', 'IK0753', 'QP0935', 'BBZG92', 'XA7060', 'KJ4524', 'UF9103', 'FTLL26', 'FP8987', 'DX3050', 'KR0684', 'XJ1326', 'HCZX54', 'FJPV89', 'EC7118', 'KWVZ74', 'IB0282', 'HFVW64', 'NU3439', 'EP9151', 'JXGW98', 'BBLK74', 'LBPW42', 'DBLZ57', 'LN4084', 'JXYK14', 'LWBP37', 'OP0628', 'EL9722', 'LFHP14', 'KDW077', 'HLDS80', 'WH4542', 'JC0535', 'JKHW96', 'JLFK64', 'RE7838', 'PBDT23', 'UW3781', 'JXXT73', 'BXZP30', 'DPPJ10', 'JZRD97', 'BFGG68', 'YW1975', 'LPFW92', 'WZ4398', 'GHSW85', 'YP3098', 'KPJP44', 'QZ0357', 'WV7713', 'CCDV39', 'GWC067', 'VZ9141', 'VL0805', 'CSJR94', 'XL0398', 'CVSV95', 'NB4250', 'DGJX11', 'WN0756', 'VB8209', 'KTGR27', 'DTBP86', 'DHXB95', 'RB3899', 'DS3203', 'CLCJ66', 'DBTX65', 'XT0586', 'DXKR65', 'BHDK99', 'DS5662', 'FRLF55', 'SZ4763', 'BZSB71', 'FDPX24', 'GXDW96', 'FJVY60', 'HTRY57', 'RA9997', 'BGRY62', 'CTSX30', 'LRXY83', 'VJ5558', 'UE2005', 'HYYC59', 'BZZR24', 'ZL3357', 'KFKY18', 'FVBR57', 'UE7845', 'CBWL83', 'CHBJ12', 'BHBC32', 'BFWK67', 'LN8359', 'WR6936', 'CFBG91', 'LTTT95', 'LDVZ20', 'JCHB87', 'TN6728', 'VZ5287', 'KLYV97', 'DZ7000', 'OL0621', 'RY7521', 'BVVH25', 'FVGT37', 'NZ8785', 'HHBH58', 'JRLT56', 'BCDL51', 'YC9293', 'LWSR61', 'HGV013', 'KXYB57', 'CKHB27', 'LP5630', 'KSKV71', 'UE6124', 'ZV1824', 'RX8578', 'KFFW76', 'KWYX70', 'XB0551', 'BHVF75', 'PL9456', 'KHZ033', 'RD8080', 'YR6392', 'KRYZ47', 'DHJB96', 'UE6142', 'OZ0565', 'ZX2244', 'YK4774', 'LSBC98', 'LYRK53', 'KJSD73', 'JFDV41', 'GXSB39', 'SJ7800', 'WX1399', 'BM0775', 'GRZR56', 'GJHH78', 'FZCS14', 'HTVB43', 'KYTF30', 'NN6666', 'UN9815', 'FZCV44', 'KR4288', 'RN7396', 'KTJB19', 'XB4500', 'YJ4950', 'OA0176', 'FYSG49', 'ZJ7904', 'DXLY69', 'FSW075', 'DSLV58', 'BYJS56', 'KRLZ71', 'BDCW12', 'YG4109', 'DWRD44', 'JFHB24', 'FGXT80', 'DVVT95', 'GWD085', 'HKZJ63', 'BDGH13', 'FBJJ18', 'DYTL17', 'DCJB81', 'WE5891', 'BWXH65', 'DR2031', 'KV1759', 'BJB066', 'YA4780', 'BJK033', 'DDRD35', 'BXXV72', 'CFRW98', 'HYCS13', 'VR6058', 'FHPJ20', 'BYKB85', 'GTBD52', 'FPDV84', 'LFGP43', 'HPPT36', 'BRKW37', 'QJ0489', 'YR6149', 'ON0383', 'NW3360', 'TP8146', 'FGTK52', 'AA4647', 'ML0930', 'LDYF27', 'GRKX56', 'CPDB38', 'GWKD92', 'VP9596', 'XZ8634', 'GDC053', 'CLBH87', 'BLJB62', 'HXZL78', 'YX0424', 'DT9796', 'KWZ077', 'ZK9520', 'JGPZ32', 'HJFP92', 'XF3677', 'JDT053', 'DYCP92', 'YX1980', 'WL4063', 'RY3475', 'VX3632', 'KB1729', 'GLTD30', 'KF7964', 'HZFY24', 'DYXF86', 'XH6463', 'KGZH15', 'KC9784', 'BJZB79', 'KN8117', 'LVLB84', 'JPLZ84', 'FPRX43', 'HPR093', 'GHVF48', 'JDSC31', 'VV4408', 'FZR039', 'LDHC61', 'LTBP58', 'YC9378', 'VV9929', 'JJRK66', 'FSGC26', 'CJTD86', 'ID0474', 'KW2877', 'LTGC17', 'PCSY12', 'KTST75', 'SC8081', 'DFDR93', 'DVWR56', 'JRXB32', 'DR2286', 'KGHB37', 'ZU1801', 'FHPS67', 'LSGT12', 'VF2339', 'KDLB19', 'BBRC52', 'DSCG32', 'LBB040', 'KGHV88', 'YN4779', 'HCGR27', 'FKZL28', 'QS0114', 'BR5709', 'XS8512', 'GPZH23', 'BKGL33', 'GDV053', 'JSWG76', 'GXGW96', 'BDCX70', 'XX7043', 'YC1023', 'KSXH28', 'KHHR23', 'NP7231', 'KHBT75', 'WE8528', 'LXBY69', 'NS0501', 'FJWY92', 'LRWD25', 'FDDT51', 'GSSV42', 'JPDB82', 'HKSD23', 'HHHH64', 'SN8762', 'RL0316', 'WD2584', 'EU6960', 'CKKW95', 'GHF080', 'JCLJ79', 'DV8862', 'HDZK26', 'LLXR82', 'JYXP21', 'FBJY24', 'JSDF86', 'TK3201', 'LZDV47', 'BVFG17', 'PCDX60', 'CSYK20', 'HVXD27', 'WD4418', 'ZE3757', 'DWLB53', 'FCPX10', 'KZ2331', 'ZS0673', 'BDSV35', 'KSHW34', 'PW5248', 'LRBH58', 'HRFV90', 'MN0965', 'CZJR43', 'WL0943', 'CJXB92', 'JU0893', 'BZ5920', 'CSTW59', 'JLTW73', 'WF1749', 'MK0928', 'LFZT82', 'DU6266', 'FYCS46', 'FKSK45', 'HTJZ64', 'FSX091', 'LGWB40', 'DBC085', 'JDS050', 'IZ0334', 'TW6504', 'XU7011', 'JDKX64', 'KSDL27', 'DT1283', 'GPVK42', 'KHYY66', 'GJRZ47', 'LFFR76', 'YD6860', 'BSBZ43', 'JWYH45', 'ZF8502', 'CA4909', 'GXVV43']
lista_patentes=['HKCB50']
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

            print(digito_verificador)

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

            print(digitos)

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

            print(digito_verificador)

            if(digito_verificador==digito_verificador_ingresado):
                return True
            else:
                return False

        except:
            return False


class Vehiculo:
    def __init__ (self, patente):
        self.__patente = patente
        self.__registro_transporte_publico = []
        self.__registro_revision_tecnica = []
        self.__registro_encargo_robo = []
        self.__vehiculosRematados = []
        self.__multasNoPagadas = []
        self.__infracciones_vespucio_norte = []
        self.__infracciones_vespucio_sur = []
        self.__infracciones_autopase = []
        self.__infracciones_costanera_norte = []
        self.__infracciones_nororiente = []
        self.__infracciones_vias_exclusivas = []
        self.__infracciones_lampa_santiago = []
        self.__infracciones_del_sol = []
        self.__infracciones_ruta_maipo = []
        self.__infracciones_los_libertadores = []
        self.__infracciones_el_pacifico = []

    def getPatente(self):
        return self.__patente

    def getRegistroTransportePublico(self):

        print('\nREGISTRO NACIONAL DE TRANSPORTE P??BLICO Y ESCOLAR\n')

        registro = self.__registro_transporte_publico

        if(self.__registro_transporte_publico==[]):
            print('El veh??culo de patente ', self.__patente, ' no pertenece al Registro Nacional de Servicios de Transporte P??blico de Pasajeros ni al Registro Nacional de Servicios de Transporte Remunerado de Escolares\n')
        else:
            print('Placa Patente:', registro[0])
            print('Fecha de Entrada RNT:',registro[1])
            print('Tipo de Servicio:',registro[2])
            print('Capacidad:',registro[3])
            print('Estado de Vehiculo:' ,registro[4])
            print('Region:',registro[5])
            print('A??o de fabricacion: ',registro[6])
            print('Cinturon de seguridad obligatorio: ',registro[7])
            print('Antig??edad del Vehiculo: ',registro[8])
            print('Marca:',registro[9])
            print('Modelo:',registro[10])
            print('Folio Servicio:',registro[11])
            print('Flota Asociada al Servicio:',registro[12])
            print('Nombre del Responsable del Servicio:',registro[13])
            print('Estado del Servicio:',registro[14])

        return self.__registro_transporte_publico

    def setRegistroTransportePublico(self, registroTransportePublico):
        self.__registro_transporte_publico = registroTransportePublico

    def getRegistroRevisionTecnica(self):

        print('\nREGISTRO DE REVISION TECNICA\n')

        registrosDeRevision = self.__registro_revision_tecnica

        titulos = ['Patente: ', 'Tipo: ', 'Marca: ', 'Modelo: ', 'A??o Fabricacion: ', 'Numero Motor: ', 'Numero Chasis: ', 'Numero Vin: ']
        indice_titulos = 0

        print('\nInformacion del Vehiculo: \n')

        if(registrosDeRevision[0]!=[]):
            for dato in registrosDeRevision[0]:
                print(titulos[indice_titulos] + dato)
                indice_titulos+=1
        else:
            print('El vehiculo de patente ', self.__patente, 'no posee informaci??n registrada.')

        print('\nInformacion de Revision Tecnica: \n')

        if(registrosDeRevision[1]!=[]):
            for indice_revision in range(0, len(registrosDeRevision[1])):
                print('Fecha: ', registrosDeRevision[1][indice_revision])
                print('Cod. Planta: ', registrosDeRevision[2][indice_revision])
                print('Planta: ', registrosDeRevision[3][indice_revision])
                print('Nro. Certificado: ', registrosDeRevision[4][indice_revision])
                print('Fecha Vec: ', registrosDeRevision[5][indice_revision])
                print('Estado: ', registrosDeRevision[6][indice_revision],'\n')
        else:
            print('El vehiculo de patente ', self.__patente, 'no posee informaci??n de revision tecnica registrada.')

        return self.__registro_revision_tecnica

    def setRegistroRevisionTecnica(self, registroRevisionTecnica):
        self.__registro_revision_tecnica = registroRevisionTecnica

    def getVehiculosRematados(self):
        remate=self.__vehiculosRematados
        print(remate)

    def setVehiculosRematados(self, vehiculosRematados):
        self.__vehiculosRematados = vehiculosRematados

    def getRegistroEncargoRobo(self):

        encargo = self.__registro_encargo_robo

        if(encargo[1] == []):
            print(encargo[0][0])
        
        else:
            print('\nEncargo robo: \n')
            print(encargo[0][0])
            print('Patente delantera: ', encargo[1][0])
            print('Patente trasera: ', encargo[1][1])
            print('VIN: ', encargo[1][2])
            print('Motor: ', encargo[1][3])

        return self.__registro_encargo_robo

    def setRegistroEncargoRobo(self, registroEncargoRobo):
        self.__registro_encargo_robo = registroEncargoRobo

    def getMultasNoPagadas(self):
            
            multas = self.__multasNoPagadas
            if multas!=[]:
                print('\nMultas no pagadas: \n')
                aux=[multas[i:i + 2] for i in range(0, len(multas), 2)]
                for i in aux:
                    i[1]=i[1].replace('               ','')
                    print(f'Juzgado Polic??a Local: {i[0]}\n\tRol Causa: {i[1]}')
            return self.__multasNoPagadas

    def setMultasNoPagadas(self, multasNoPagadas):
        self.__multasNoPagadas = multasNoPagadas

    def getInfraccionesVespucioNorte(self):

        if(self.__infracciones_vespucio_norte==[]):
            print('El vehiculo de patente ', self.__patente, 'no tiene infracciones en Vespucio Norte.')

        else:
            for detalle in self.__infracciones_vespucio_norte:
                print('\n')
                print('Numero boleta: ', detalle[0])
                print('Pago total: $', detalle[1])

                fecha_hora = detalle[2].split(' ')
                print('Fecha: ', fecha_hora[0])
                print('Hora: ', fecha_hora[1])

        return self.__infracciones_vespucio_norte

    def setInfraccionesVespucioNorte(self, infraccionesVespucioNorte):

        self.__infracciones_vespucio_norte = infraccionesVespucioNorte

    def getInfraccionesVespucioSur(self):

        if(self.__infracciones_vespucio_sur==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene infracciones en Vespucio Sur.')
        else:

            print('Infracciones Vespucio Sur: \n')

            for detalle in self.__infracciones_vespucio_sur:

                print('Fecha de infraccion: ',detalle[0])
                print('Categoria de infraccion: ', detalle[1])
                print('Estado de infraccion: ', detalle[2])

        return self.__infracciones_vespucio_sur

    def setInfraccionesVespucioSur(self, infraccionesVespucioSur):

        self.__infracciones_vespucio_sur = infraccionesVespucioSur

    def getInfraccionesAutopase(self):

        print('\nAutopase\n')

        if(self.__infracciones_autopase[0]==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene infracciones no facturadas en Autopase\n')

        else:
            print('Infracciones no facturadas: \n')
            for infraccion_no_facturada in self.__infracciones_autopase[0]:
                print('Rut: ', infraccion_no_facturada[0])
                print('Patente: ', infraccion_no_facturada[1])
                print('Fecha: ', infraccion_no_facturada[2])
                print('Total: ', infraccion_no_facturada[3], '\n')

        if(self.__infracciones_autopase[1]==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene infracciones facturadas en Autopase\n')

        else:
            print('Infracciones facturadas: \n')
            for infraccion_facturada in self.__infracciones_autopase[1]:
                print('Rut: ', infraccion_facturada[0])
                print('Patente: ', infraccion_facturada[1])
                print('Numero de boleta: ', infraccion_facturada[2])
                print('Cargo del mes: ', infraccion_facturada[3], '\n')

        if(self.__infracciones_autopase[2]==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene detalles de infracciones en Autopase\n')

        else:
            print('Detalles de boleta: \n')

            numero_boleta = ''
            condicion_boleta = True

            for detalle_infraccion in self.__infracciones_autopase[2]:

                if(condicion_boleta==True):
                    numero_boleta = detalle_infraccion[0]
                    condicion_boleta=False
                    pass

                else:
                    numero_boleta_aux = detalle_infraccion[0]
                    if(numero_boleta == numero_boleta_aux):
                        pass
                    else:
                        print('Siguiente boleta...\n')
                        condicion_boleta=True

                print('Numero de boleta: ', detalle_infraccion[0])
                print('Patente: ', detalle_infraccion[1])
                print('Fecha: ', detalle_infraccion[2])
                print('Hora: ', detalle_infraccion[3], '\n')

        return self.__infracciones_autopase

    def setInfraccionesAutopase(self, infraccionesAutopase):
        self.__infracciones_autopase = infraccionesAutopase

    def getInfraccionesCostaneraNorte(self):

        infracciones_Costanera_Norte = self.__infracciones_costanera_norte

        if(infracciones_Costanera_Norte==[[],[],[]]):
           print('El vehiculo de patente', self.__patente, 'no presenta infracciones en Costanera Norte')

        else:
            print('Infracciones en Costanera Norte \n')
            for detalles_cn in range(0, len(infracciones_Costanera_Norte[0])):
                print('Fecha: ', infracciones_Costanera_Norte[0][detalles_cn])
                print('Categoria: ', infracciones_Costanera_Norte[1][detalles_cn])
                print('Estado: ', infracciones_Costanera_Norte[2][detalles_cn], '\n')

        return self.__infracciones_costanera_norte

    def setInfraccionesCostaneraNorte(self, infraccionesCostaneraNorte):
        self.__infracciones_costanera_norte = infraccionesCostaneraNorte

    def getInfraccionesNororiente(self):

        infracciones_Nororiente = self.__infracciones_nororiente

        if(infracciones_Nororiente==[[],[],[],[],[],[]]):
            print('El vehiculo de patente ', self.__patente, 'no tiene infracciones en Nororiente')

        else:
            print('\nInfracciones Nororiente: \n')
            for i in range(0, len(infracciones_Nororiente[0])):
                print('Convenio: ', infracciones_Nororiente[0][i])
                print('Documento: ', infracciones_Nororiente[1][i])
                print('Deuda vencida: ', infracciones_Nororiente[2][i])
                print('Deuda por vencer: ', infracciones_Nororiente[3][i])
                print('Total Deuda: ', infracciones_Nororiente[4][i], '\n')

            print('Total a pagar: ', infracciones_Nororiente[5][0])

        return self.__infracciones_nororiente

    def setInfraccionesNororiente(self, infraccionesNororiente):
        self.__infracciones_nororiente = infraccionesNororiente

    def getInfraccionesViasExclusivas(self):

        infracciones_vias_exclusivas = self.__infracciones_vias_exclusivas
        if(infracciones_vias_exclusivas[3]==[]):
            print('El vehiculo de patente ', self.__patente, 'no tiene registro de infracciones en Vias Exclusivas')

        else:
            print('\nInfracciones Vias Exclusivas\n')
            for i in range(0, len(infracciones_vias_exclusivas[3])):
                print('Fecha: ', infracciones_vias_exclusivas[0][i])
                print('Lugar: ', infracciones_vias_exclusivas[1][i])
                print('Tipo: ', infracciones_vias_exclusivas[2][i])
                print('Juzgado de Policia Local: ', infracciones_vias_exclusivas[3][i], '\n')

        return self.__infracciones_vias_exclusivas

    def setInfraccionesViasExclusivas(self, infraccionesViasExclusivas):

        self.__infracciones_vias_exclusivas = infraccionesViasExclusivas
    
    def getInfraccionesLampaSantiago(self):

        infracciones = self.__infracciones_lampa_santiago

        if(infracciones==[]):
            print('El vehiculo de patente ', self.__patente, 'no registra infracciones en Lampa-Santiago')

        else:
            print('\nLampa Santiago: \n')
            for i in infracciones:
                print('Fecha: ', i[0])
                print('Hora: ', i[1])
                print('Punto Cobro: ', i[2])
                print('Categoria: ', i[3])
                print('Tipo Transito: ', i[4], '\n')

        return self.__infracciones_lampa_santiago

    def setInfraccionesLampaSantiago(self, infraccionesLampaSantiago):
        self.__infracciones_lampa_santiago = infraccionesLampaSantiago

    def getInfraccionesDelSol(self):
        infracciones_del_sol = self.__infracciones_del_sol

        if(infracciones_del_sol==[]):
            print('El vehiculo de patente ', self.__patente, 'no registra infracciones en "Del Sol"')

        else:
            print('\nInfracciones Del Sol:\n')

            indice = 0
            for i in infracciones_del_sol[0]:
                print('\nInfraccion ', indice+1, ':')
                print('Transito sin Tag Ruta: ', i[0])
                print('Patente: ', i[1])
                print('Vence: ', i[2])
                print('Total: ', i[3], '\n')
                
                print('\nDetalle: ')
                for k in infracciones_del_sol[1][indice]:

                    
                    print('\nPatente: ', k[0])
                    print('Nombre Concesionaria: ', k[1])
                    print('Hora de tr??nsito: ', k[2])
                    print('Fecha de tr??nsito: ', k[3])
                    print('Glosa Portico: ', k[4])
                    print('Fecha de Vencimiento: ', k[5])
                    print('Deuda: ', k[6],'\n')

                indice+=1

    def setInfraccionesDelSol(self, infraccionesDelSol):
        self.__infracciones_del_sol = infraccionesDelSol

    def getInfraccionesRutaMaipo(self):

        infraccionesRutaMaipo = self.__infracciones_ruta_maipo
        print('\nRuta Maipo\n')
        print('\nNo facturados\n')
        if(infraccionesRutaMaipo[0]==[]):
            print('El vehiculo de patente ', self.__patente, 'no tiene registros de tr??nsitos de m??s de 30 d??as no facturados\n')
        else:
            for i in range(0, len(infraccionesRutaMaipo[0][0])):
                print('Fecha de transito: ', infraccionesRutaMaipo[0][0][i])
                print('Cantidad de transitos: ',  infraccionesRutaMaipo[0][1][i])
                print('Tarifa: ', infraccionesRutaMaipo[0][2][i], '\n')
            print('\nTotal a pagar: ', infraccionesRutaMaipo[0][3], '\n')

        print('\nFacturados\n')
        if(infraccionesRutaMaipo[1]==[]):
            print('El vehiculo de patente, ', self.__patente, 'no tiene registros de tr??nsitos de m??s de 30 d??as facturados\n')

        else:
            for i in range(0, len(infraccionesRutaMaipo[1][0])):
                print('Numero de documento: ', infraccionesRutaMaipo[1][0][i])
                print('Fecha de emision: ', infraccionesRutaMaipo[1][1][i])
                print('Total a pagar: ', infraccionesRutaMaipo[1][2][i])

        return self.__infracciones_ruta_maipo

    def setInfraccionesRutaMaipo(self, infraccionesRutaMaipo):
        self.__infracciones_ruta_maipo = infraccionesRutaMaipo

    def getInfraccionesLosLibertadores(self):
        infracciones_los_libertadores = self.__infracciones_los_libertadores

        if(infracciones_los_libertadores==[]):
            print('El vehiculo de patente ', self.__patente, 'no registra infracciones en Los Libertadores')

        else:
            print('\nInfracciones Los Libertadores:\n')

            indice = 0
            for i in infracciones_los_libertadores[0]:
                print('\nInfraccion ', indice+1, ':')
                print('Transito sin Tag Ruta: ', i[0])
                print('Patente: ', i[1])
                print('Vence: ', i[2])
                print('Total: ', i[3], '\n')
                
                print('\nDetalle: ')
                for k in infracciones_los_libertadores[1][indice]:

                    
                    print('\nPatente: ', k[0])
                    print('Nombre Concesionaria: ', k[1])
                    print('Hora de tr??nsito: ', k[2])
                    print('Fecha de tr??nsito: ', k[3])
                    print('Glosa Portico: ', k[4])
                    print('Fecha de Vencimiento: ', k[5])
                    print('Deuda: ', k[6],'\n')

                indice+=1

    def setInfraccionesLosLibertadores(self, infraccionesLosLibertadores):
        self.__infracciones_los_libertadores = infraccionesLosLibertadores

    def getInfraccionesElPacifico(self):
        infracciones_del_pacifico = self.__infracciones_el_pacifico

        if(infracciones_del_pacifico==[]):
            print('El vehiculo de patente ', self.__patente, 'no registra infracciones en "El Pac??fico"')

        else:
            print('\nInfracciones El Pac??fico:\n')

            indice = 0
            for i in infracciones_del_pacifico[0]:
                print('\nInfraccion ', indice+1, ':')
                print('Transito sin Tag Ruta: ', i[0])
                print('Patente: ', i[1])
                print('Vence: ', i[2])
                print('Total: ', i[3], '\n')
                
                print('\nDetalle: ')
                for k in infracciones_del_pacifico[1][indice]:

                    
                    print('\nPatente: ', k[0])
                    print('Nombre Concesionaria: ', k[1])
                    print('Hora de tr??nsito: ', k[2])
                    print('Fecha de tr??nsito: ', k[3])
                    print('Glosa Portico: ', k[4])
                    print('Fecha de Vencimiento: ', k[5])
                    print('Deuda: ', k[6],'\n')

                indice+=1

    def setInfraccionesElPacifico(self, infraccionesElPacifico):
        self.__infracciones_el_pacifico = infraccionesElPacifico

class TransportePublico:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def resultado(self):
        cookies = {
            'ASP.NET_SessionId': '0sla4exrmtiuesonv2pvmhqf',
            '_ga': 'GA1.2.1806332623.1637258376',
            '_gid': 'GA1.2.1544212551.1637804958',    
        }

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Origin': 'http://apps.mtt.cl',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://apps.mtt.cl/consultaweb/',
            'Accept-Language': 'es-ES,es;q=0.9',
            }


        data = {
        '__VIEWSTATE': '/wEPDwUKMTc0MTY3NTE3MQ9kFgJmD2QWAgIDD2QWAgIBD2QWAgIBD2QWAgIBD2QWAgIFDw8WBB4EVGV4dAWFAjxpbWcgc3JjPSdodHRwOi8vYXBwcy5tdHQuY2wvd3d3L2ltZ3MvcGxhY2FfbHVwYS5wbmcnIC8+PGJyIC8+PHN0cm9uZz5FbCB2ZWjDrWN1bG8gZW4gY29uc3VsdGEgbm8gcGVydGVuZWNlIGFsIFJlZ2lzdHJvIE5hY2lvbmFsIGRlIFNlcnZpY2lvcyBkZSBUcmFuc3BvcnRlIFDDumJsaWNvIGRlIFBhc2FqZXJvcyBuaSBhbCBSZWdpc3RybyBOYWNpb25hbCBkZSBTZXJ2aWNpb3MgZGUgVHJhbnNwb3J0ZSBSZW11bmVyYWRvIGRlIEVzY29sYXJlczwvc3Ryb25nPh4HVmlzaWJsZWdkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUgY3RsMDAkTWFpbkNvbnRlbnQkaW1nQnRuQ29uc3VsdGHi2oH8N/l6WPK18/lBTVqKUyDl6cjAz/FPHWG90t6r+g==',
        '__VIEWSTATEGENERATOR': '522DF3F1',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__EVENTVALIDATION': '/wEdAASTj8RE1t+b0rmqH5lXzbQHIKnzPnVFgXAZ20CcrnWXzeHx18AZ0epHV1po9+JEZeBnTMb45aJIIeXNdhdxmB5y16hbBVTD9sA1Df7Tv3JDHwkxYnhJbQWRrG6M43r0Y20=',
        'ctl00$MainContent$ppu': self.__patenteVehiculo,
        'ctl00$MainContent$btn_buscar': 'Buscar'
        }

        try:
            response = requests.post('http://apps.mtt.cl/consultaweb/', headers=headers, cookies=cookies, data=data, verify=False)

            soup = BeautifulSoup(response.text, 'html.parser')
            table=soup.find_all("table", id='MainContent_tablaDatos')
            registro_aux = ''
            for palabra in table:

                try:
                    registro_aux = registro_aux+palabra.text.replace('\n', ' ')
                except:
                    registro_aux = registro_aux+palabra.text

            registro_array = registro_aux.split('   ')

            for i in registro_array:
                if((i.isupper()==True) or (i=='') or (i=='  ')):
                    registro_array.remove(i)

            registro_array.remove(registro_array[len(registro_array)-1])
            registro_array.remove(registro_array[len(registro_array)-1])

            registro_array_final = []

            registro_array_final.append(registro_array[0].split(' ')[2])
            registro_array_final.append(registro_array[1].split(' ')[4])

            registro_indice_2 = registro_array[2].split(' ')
            cont_bucle = 0
            while(cont_bucle<3):
                registro_indice_2.remove(registro_indice_2[0])
                cont_bucle+=1

            tipo_transporte = ''
            for i in registro_indice_2:
                tipo_transporte = tipo_transporte+' '+i
            registro_array_final.append(tipo_transporte.strip())

            registro_array_final.append(registro_array[3].split(' ')[1])
            registro_array_final.append(registro_array[4].split(' ')[3])
            registro_array_final.append(registro_array[5].split(' ')[1])
            registro_array_final.append(registro_array[6].split(' ')[3])
            registro_array_final.append(registro_array[7].split(' ')[4])
            registro_array_final.append(registro_array[8].split(' ')[3])

            registro_indice_9 = registro_array[9].split(' ')
            registro_indice_9.remove(registro_indice_9[0])

            marca_transporte = ''
            for i in registro_indice_9:
                marca_transporte = marca_transporte+' '+i
            registro_array_final.append(marca_transporte.strip())

            registro_indice_10 = registro_array[10].split(' ')
            registro_indice_10.remove(registro_indice_10[0])

            modelo_transporte = ''
            for i in registro_indice_10:
                modelo_transporte=modelo_transporte+' '+i
            registro_array_final.append(modelo_transporte.strip())

            registro_array_final.append(registro_array[11].split(' ')[2])
            registro_array_final.append(registro_array[12].split(' ')[4])

            registro_indice_13 = registro_array[13].split(' ')
            cont_bucle = 0
            while(cont_bucle<5):
                registro_indice_13.remove(registro_indice_13[0])
                cont_bucle+=1

            nombre_responsable = ''
            for i in registro_indice_13:
                nombre_responsable=nombre_responsable+' '+i
            registro_array_final.append(nombre_responsable.strip())

            registro_array_final.append(registro_array[14].split(' ')[3])

            return registro_array_final
        except:
            return []

class RevisionTecnica:
    def __init__(self, patenteVehiculo, API_KEY, page_url):
        self.__patenteVehiculo = patenteVehiculo
        self.__API_KEY = API_KEY
        self.__page_url = page_url

    def resultado(self):
        #soup = BeautifulSoup(driver.page_source, 'html.parser')
        #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
        sitekey = '6LctMP8SAAAAANBvpGMjkMm5bBJ7TY-7X9UuGAaq'
        u1 = f"https://2captcha.com/in.php?key={self.__API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={self.__page_url}&json=1"
        r1 = requests.get(u1)
        rid = r1.json().get("request")
        u2 = f"https://2captcha.com/res.php?key={self.__API_KEY}&action=get&id={int(rid)}&json=1"
        time.sleep(5)
        while True:
            r2 = requests.get(u2)
            if r2.json().get("status") == 1:
                form_tokon = r2.json().get("request")
                break
            time.sleep(5)

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://www.prt.cl',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.prt.cl/Paginas/RevisionTecnica.aspx',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': 'Iq601Ta4fJGLhgkDHTJBOkqcUPBHIqu88qsauJlotK5C8nJnoJv+6DsYXNn9YYkpNoLKf8k7tul7AD420ptaKveliplDcWaOESiUKOT64GthfNBU+GlFjX5GhXW4W0aUKbC2DVO3MnB0lPXjG+WdlUuWtK6NqAJr5+CRbsVaihh3L6OueqVEZkrcFr0ytvgtBi6gATZgmLcNAMVDnFX8epyXQKQtfcxP8jOr6j/4rnUju2iHsuVUAmWBO+QwZpo2sFZkL/cFg/vbjdR6Wr04fQ3hbAaAKNrpgPdY/9T2uB8DD4scFHhRH2IwgMYFgsy9tUANEMLG4sKLcQuX3+3NdBc4YHYFIf7aTur0eQT68C9Z9xocQj2frfsIWXAxXo9g6PTIawOYdkezOf7+rq4yIHIsRQActtxvLax2u/QtYTYIlQ5o26YnaVW7bZjUsoJ/iXIdmENbTkm/94eN8w/kB+JdDrGZRS8mi6gmgfx3RAzOhnFC6gUQu6+z0brWvIXnf03Mcg==',
            '__VIEWSTATEGENERATOR': '4F717C3B',
            '__EVENTVALIDATION': 'qxLAMNT9rltV6gVzxoPJtyrO5UOBnCx/6RiNSQl2d9NSqeox2pP+gXMGDu4Vs0V3mKmV+MhiWu7mZ3rLYHwpxyaWEXdTs6GwVbqEeSlIeJ2jmyX2j7IFVeZz+p5VK8mrGnU05qAOlnGuMibqG2Mj71Jw2w7tKb3NkWBu5U9J/O5AMJudnwQ35rmWpc+wp7VPiy0T9bdAFa5zvH4n9HyJNRBtMpLOzt3uUTb/NHNL9QP4DtzTIL/GhOFlavFP4ZFOYZjQ1g==',
            'ctl00$ContentPlaceHolder1$hddPPU': '',
            'ctl00$ContentPlaceHolder1$hddPRT': '',
            'ctl00$ContentPlaceHolder1$hddDIRPRT': '',
            'ctl00$ContentPlaceHolder1$patenteInput': self.__patenteVehiculo,
            'ctl00$ContentPlaceHolder1$buscar.x': '36',
            'ctl00$ContentPlaceHolder1$buscar.y': '23',
            'g-recaptcha-response': form_tokon,
            'ctl00$ContentPlaceHolder1$MyAccordion_AccordionExtender_ClientState': '0'
        }

        try:
            response = requests.post('http://www.prt.cl/Paginas/RevisionTecnica.aspx', headers=headers, data=data, verify=False)

            soup = BeautifulSoup(response.text, 'html.parser')
            datoVehiculos = []
            infoRevision_Fecha, infoRevision_CodPlanta,infoRevision_Planta,infoRevision_NroCertificado,infoRevision_FechaVec, infoRevision_Estado= [],[],[],[],[],[]
            infoVehiculo = soup.find_all('span', id='ContentPlaceHolder1_lblDatosVehiculo')
            infoRevision = soup.find_all('span', id='ContentPlaceHolder1_lblHistorico')

            for i in infoVehiculo:
                for z in i.find_all('span'):

                    if('Nota :' not in z.text):
                        datoVehiculos.append(z.text)

            for i in infoRevision:
                for z in i.find_all('td')[0::6]:
                    infoRevision_Fecha.append(z.text)

                for z in i.find_all('td')[1::6]:
                    infoRevision_CodPlanta.append(z.text)

                for z in i.find_all('td')[2::6]:
                    infoRevision_Planta.append(z.text)

                for z in i.find_all('td')[3::6]:
                    infoRevision_NroCertificado.append(z.text.split('(g)')[0])

                for z in i.find_all('td')[4::6]:
                    infoRevision_FechaVec.append(z.text)

                for z in i.find_all('td')[5::6]:
                    infoRevision_Estado.append(z.text)

            return [datoVehiculos, infoRevision_Fecha, infoRevision_CodPlanta,infoRevision_Planta,infoRevision_NroCertificado,infoRevision_FechaVec, infoRevision_Estado]
        except:
            return [[],[],[],[],[],[],[]]

class EncargoRobo:
    def __init__(self, patenteVehiculo, API_KEY, page_url):
        self.__patenteVehiculo = patenteVehiculo
        self.__API_KEY = API_KEY
        self.__page_url = page_url

    def Solver(self, driver, API_KEY, page_url):
        soup = BeautifulSoup(driver.page_source, 'html.parser') 
        sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
        #sitekey = '6LctMP8SAAAAANBvpGMjkMm5bBJ7TY-7X9UuGAaq'
        u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={page_url}&json=1"
        r1 = requests.get(u1)
        rid = r1.json().get("request")
        u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
        time.sleep(5)
        while True:
            r2 = requests.get(u2)
            if r2.json().get("status") == 1:
                form_tokon = r2.json().get("request")
                break
            time.sleep(5)
        wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
        driver.execute_script(wirte_tokon_js)
        time.sleep(3)

    def resultado(self):

        if __name__ == '__main__':
            driver = webdriver.Chrome()
            driver.get(self.__page_url)
            driver.find_element_by_xpath('//*[@id="txt_placa_patente"]').send_keys(self.__patenteVehiculo)
            self.Solver(driver, self.__API_KEY, self.__page_url)
            btt=driver.find_element_by_xpath('//*[@id="btn_consultar"]')
            btt.click()
            time.sleep(5)
            print(driver.page_source, file=open("robo.html", "w"))
            '''
            with open("robo.html") as fp:
                soup = BeautifulSoup(fp, 'html.parser')
            '''
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            #print(soup)
            content=soup.find_all('div', class_='modal-content')
            informacion = [] 
            estado = [] 
            for i in content:
                for z in i.find_all('label', id='lbl_Vehiculo'):
                    mensaje=z.text
                    informacion.append(z.text)

                for z in i.find_all('td', align='left'):
                    estado.append(z.text)

            #driver.close()
        return [informacion, estado]

class Vehiculos_rematados:
    def __init__(self,  API_KEY, APIKEY_2CAPTCHA, patente, page):
        self.API_KEY = API_KEY
        self.APIKEY_2CAPTCHA = APIKEY_2CAPTCHA
        self.patente = patente
        self.page = page

    def resultado(self):
        sitekey='6Lc03YYUAAAAAL0m-kzq5mX0LuAXU9qIYl5cZITc'
        numeros=int(''.join(filter(str.isdigit, self.patente)))
        letras = (self.patente.strip(str(numeros)))
        api_key = os.getenv(self.APIKEY_2CAPTCHA, self.API_KEY)
        solver = TwoCaptcha(api_key)
        options = webdriver.ChromeOptions()
        # options.add_argument('--proxy-server=%s' % PROXY[0])
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--lang=es")
        driver = webdriver.Chrome()
        driver.get(self.page)
        driver.find_element_by_xpath('//*[@id="masterContenido_txtLetras"]').send_keys(letras)
        driver.find_element_by_xpath('//*[@id="masterContenido_txtNumeros"]').send_keys(numeros)
        try:
            result = solver.recaptcha(sitekey=sitekey,url=driver.current_url)
        except:
            print('error')
        else:
            result=str(result.get('code'))
        driver.find_element_by_xpath('//*[@id="masterContenido_chkCondiciones"]').click()
        driver.find_element_by_xpath('//*[@id="masterContenido_btnLnkConsultar"]').click()
        soup=BeautifulSoup(driver.page_source,'html.parser')
        #print(driver.page_source, file=open('4rematados.html','w'))
        table = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/main/section/form/div[3]/div/div/table/tbody/tr/td/div/table[3]/tbody')
        a = []
        for i in table:
            a.append(i.text)

        return a

class Multas_No_Pagadas:
    def __init__(self, patente, API_KEY):
        self.patente = patente
        self.API_KEY = API_KEY

    def Solver(self,driver):
        page_url='http://consultamultas.srcei.cl/ConsultaMultas/buscarConsultaMultasExterna.do'
        sitekey = '6Ld_vfsSAAAAAGbw9u9u1V2x8pqV_3Y5AS4h9mW1'
        u1 = f"https://2captcha.com/in.php?key={self.API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={page_url}&json=1"
        r1 = requests.get(u1)
        rid = r1.json().get("request")
        u2 = f"https://2captcha.com/res.php?key={self.API_KEY}&action=get&id={int(rid)}&json=1"
        time.sleep(5)
        while True:
            r2 = requests.get(u2)
            if r2.json().get("status") == 1:
                form_tokon = r2.json().get("request")
                break
            time.sleep(5)
        wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
        driver.execute_script(wirte_tokon_js)
        time.sleep(3)

    def resultado(self):
        x= 'http://consultamultas.srcei.cl/ConsultaMultas/consultaMultasExterna.do'
        driver=webdriver.Chrome()
        driver.get(x)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[7]/td[2]/span/input').send_keys(self.patente)
        self.Solver(driver)
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[8]/td/table/tbody/tr[2]/td/a').click()
        multasNoPagadas=[]
        cont=0
        try:
            soup=BeautifulSoup(driver.page_source,'html.parser')
            for i in soup.find_all("table",class_="grilla"):
                for j in i.find_all("td"):
                    if cont==0:
                        multasNoPagadas.append(j.text)
                        #print(j.text)
                cont+=1

                
        except:
            pass


        return multasNoPagadas

class VespucioNorte:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):

        infraccionesVespucioNorte = []

        cookies = {
            '_ga': 'GA1.2.1222882760.1637102421',
            '_gid': 'GA1.2.75323150.1638659755',
            'ASP.NET_SessionId': '1md502mphs2isqh4mvztxoks',
            '__RequestVerificationToken': 'FEleRsgHGbuM1DCVKdY59FpL9OOnRnk2j_nsfRNjMw2rZJc68ASJWziBeDr6U5L46fHaqVq3XTz-tVIU6xx60FrCCrsSlb-QpObZQps1Jdg1',
            '_gat': '1',
        }

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://www.vespucionorte.cl',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.vespucionorte.cl/Home/CirculasteSinTag',
            'Accept-Language': 'es-ES,es;q=0.9',
        }

        data = {
            'patente': self.__patenteVehiculo
        }

        try:
            lista=[]
            lista2=[]

            dict={}
            response = requests.post('https://www.vespucionorte.cl/Ajax/GetInfractores', headers=headers, cookies=cookies, data=data)

            response=json.loads(response.text)
            for i in response['tablaTransitosFact']:
                lista.append(str(i['numeroBoleta']).strip('00000000'))
                lista2.append(i['totalBoleta'])
            for i in lista:
                dict[i]=[]
                dict[i].append(str(lista2[lista.index(i)]).strip('0000000000000'))
            for i in response['tablaDetalleTransito']:
                dict[str(i['numeroBoleta']).strip('00000000')].append(i['fechaTransito']+' '+i['horaTransito'])

            for key in dict:
                numb_boleta = key
                total_boleta = dict[key][0]
                fecha_hora = dict[key][1]
                infraccionesVespucioNorte.append([numb_boleta, total_boleta, fecha_hora])

            return infraccionesVespucioNorte

        except:
            return []

class VespucioSur:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
        page_url ='https://web.costaneranorte.cl/circulaste-sin-tag/consultar-transitos-sin-tag/'

        def Solver(url):
            #soup = BeautifulSoup(driver.page_source, 'html.parser') 
            #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
            sitekey = '6Lfchk8UAAAAAMPIv-l8SB4CfG385t6a5UfR08vt'
            u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&json=1"
            r1 = requests.get(u1)
            print(r1.json())
            rid = r1.json().get("request")
            u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
            time.sleep(5)
            while True:
                r2 = requests.get(u2)
                print(r2.json())
                if r2.json().get("status") == 1:
                    form_tokon = r2.json().get("request")
                    break
                time.sleep(5)
            return form_tokon

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Opera GX";v="81", " Not;A Brand";v="99", "Chromium";v="95"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'https://oficina.vespuciosur.cl',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'object',
            'Referer': 'https://oficina.vespuciosur.cl/tags/VerificaInfraccion.aspx',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {
            '__VIEWSTATE': '/wEPDwUJODk5Njg1MjM4D2QWAgIBD2QWAgIDDzwrAA0AZBgBBQlHcmlkVmlldzEPZ2QDiTKwJd6tbi3bDalwny11bDci1w==',
            '__VIEWSTATEGENERATOR': '99B6AABA',
            '__EVENTVALIDATION': '/wEWAwKpo6u1BQKeluy/BgKM54rGBrNpLVRtfVH7j2QrJsFQY7Ss+rwV',
            'txtpatente': self.__patenteVehiculo,
            'g-recaptcha-response': f'{str(Solver(page_url))}',
            'Button1': 'Consultar'
        }

        response = requests.post('https://oficina.vespuciosur.cl/tags/VerificaInfraccion.aspx', headers=headers, data=data)
        print(response.text, file=open("costaneraSur.html", "w"))
        soup = BeautifulSoup(response.text, 'html.parser')
        tabla = soup.find_all('table')

        fechas_infracciones = []
        categoria_infracciones = []
        estado_infracciones = []
        contador_VespucioSur = 0

        infraccionesVespucioSur = []

        for detalle in tabla:
            for fecha in detalle.find_all('td')[0::3]:
                fechas_infracciones.append(fecha.text)
                contador_VespucioSur+=1

            for categoria in detalle.find_all('td')[1::3]:
                categoria_infracciones.append(categoria.text)

            for estado in detalle.find_all('td')[2::3]:
                estado_infracciones.append(estado.text)

        for i in range(0, contador_VespucioSur):
            infraccion = []
            infraccion.append(fechas_infracciones[i])
            infraccion.append(categoria_infracciones[i])
            infraccion.append(estado_infracciones[i])
            infraccionesVespucioSur.append(infraccion)

        return infraccionesVespucioSur

class Autopase:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()

        API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
        page_url = 'https://www.autopase.cl/circulaste_sin_tag/consulta_infracciones'


        def Solver(driver, url):
            #soup = BeautifulSoup(driver.page_source, 'html.parser')
            #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
            sitekey = '6LdkAAgTAAAAAGaG1OjDMAn4q-zvgrArJDrIuPif'
            u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&json=1"
            r1 = requests.get(u1)
            rid = r1.json().get("request")
            u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
            time.sleep(5)
            while True:
                r2 = requests.get(u2)
                if r2.json().get("status") == 1:
                    form_tokon = r2.json().get("request")
                    break
                time.sleep(5)
            print("captcha solved")
            wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
            driver.execute_script(wirte_tokon_js)

        driver.get(page_url)
        driver.find_element_by_xpath('//*[@id="sInputRadio1"]').click()
        driver.find_element_by_xpath('//*[@id="sInput"]').send_keys(self.__patenteVehiculo)
        Solver(driver,page_url)
        driver.find_element_by_xpath('//*[@id="Pagar"]').click()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #tablaVentana = soup.find_all('table', id='tabla_ventana')
        noFac = soup.find_all('table', id='tabla_nofacturados')
        Fac = soup.find_all('table', id='tabla_facturados')
        Det = soup.find_all('div', role='dialog', class_=True,style=True, attrs={'aria-hidden': 'true'})
    
        noFacturados = []
        Facturados = []
        aux_Detalle = []
        Detalle = []

        all_rut_1 = []
        all_patente_1 = []
        all_fecha_1 = []
        all_total_1 = []
        contador_Autopase1 = 0

        all_rut_2 = []
        all_patente_2 = []
        all_numero_boleta_2 = []
        all_cargo_mes_2 = []
        contador_Autopase2=0

        all_patente_3 = []
        all_fecha_3= []
        all_hora_3 = []
        contador_Autopase3=0

        for detalle_1 in noFac:
            for rut_1 in detalle_1.find_all('td')[0::4]:
                all_rut_1.append(rut_1.text)
                contador_Autopase1+=1
            for patente_1 in detalle_1.find_all('td')[1::4]:
                 all_patente_1.append(patente_1.text)
            for fecha_1 in detalle_1.find_all('td')[2::4]:
                all_fecha_1.append(fecha_1.text)
            for total_1 in detalle_1.find_all('td')[3::4]:
                all_total_1.append(total_1.text)

        if(len(all_rut_1)!=len(all_total_1)):
            pass

        else:
            for i_detalle_1 in range(0, contador_Autopase1):
                aux_noFacturado = []
                aux_noFacturado.append(all_rut_1[i_detalle_1])
                aux_noFacturado.append(all_patente_1[i_detalle_1])
                aux_noFacturado.append(all_fecha_1[i_detalle_1])
                aux_noFacturado.append(all_total_1[i_detalle_1])
                noFacturados.append(aux_noFacturado)

        for detalle_2 in Fac:
            
            for rut_2 in detalle_2.find_all('td', rowspan=False, class_=False)[0::6]:
                all_rut_2.append(rut_2.text)
                contador_Autopase2+=1
            for patente_2 in detalle_2.find_all('td', rowspan=False, class_=False)[1::6]:
                all_patente_2.append(patente_2.text)
            for numero_boleta_2 in detalle_2.find_all('td', rowspan=False, class_=False)[3::6]:
                all_numero_boleta_2.append(numero_boleta_2.text)
            for cargo_mes_2 in detalle_2.find_all('td', rowspan=False, class_=False)[4::6]:
                all_cargo_mes_2.append(cargo_mes_2.text)

        if(len(all_rut_2)!=len(all_cargo_mes_2)):
            pass

        else:
            for i_detalle_2 in range(0, contador_Autopase2):
                aux_Facturado = []
                aux_Facturado.append(all_rut_2[i_detalle_2])
                aux_Facturado.append(all_patente_2[i_detalle_2])
                aux_Facturado.append(all_numero_boleta_2[i_detalle_2])
                aux_Facturado.append(all_cargo_mes_2[i_detalle_2])
                Facturados.append(aux_Facturado)

        cont_numb_boleta_2 = 0

        for detalle_3 in Det:
            
            aux_all_patente_3=[]
            aux_all_fecha_3=[]
            aux_all_hora_3=[]
            contador_Autopase3+=1

            for patente_3 in detalle_3.find_all('td')[0::3]:
                if(patente_3.text.replace('Patente','-')=='-'):
                    pass
                else:
                    aux_all_patente_3.append(patente_3.text)
            for fecha_3 in detalle_3.find_all('td')[1::3]:
                if(fecha_3.text.replace('Fecha','-')=='-'):
                    pass
                else:
                    aux_all_fecha_3.append(fecha_3.text)
            for hora_3 in detalle_3.find_all('td')[2::3]:
                if(hora_3.text.replace('Hora','-')=='-'):
                    pass
                else:
                    aux_all_hora_3.append(hora_3.text)

            all_patente_3.append(aux_all_patente_3)
            all_fecha_3.append(aux_all_hora_3)
            all_hora_3.append(aux_all_hora_3)


            aux_Detalle.append([all_numero_boleta_2[cont_numb_boleta_2] ,aux_all_patente_3, aux_all_fecha_3, aux_all_hora_3])
            cont_numb_boleta_2+=1

        if(len(all_patente_3)!=len(all_hora_3)):
            pass

        else:

            for i_detalle_3 in aux_Detalle:
                
                #aux_Detalle_final.append(i_detalle_3[0])
                for detalles in range(0, len(i_detalle_3[1])):
                    aux_Detalle_final = []
                    #aux_Detalle_final.append([i_detalle_3[0], i_detalle_3[1][detalles], i_detalle_3[2][detalles], i_detalle_3[3][detalles]])
                    aux_Detalle_final.append(i_detalle_3[0])
                    aux_Detalle_final.append(i_detalle_3[1][detalles])
                    aux_Detalle_final.append(i_detalle_3[2][detalles])
                    aux_Detalle_final.append(i_detalle_3[3][detalles])

                    Detalle.append(aux_Detalle_final)

        return [noFacturados, Facturados, Detalle]

class CostaneraNorte:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
        page_url ='https://web.costaneranorte.cl/circulaste-sin-tag/consultar-transitos-sin-tag/'

        def Solver(url):
            #soup = BeautifulSoup(driver.page_source, 'html.parser') 
            #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
            sitekey = '6Lfchk8UAAAAAMPIv-l8SB4CfG385t6a5UfR08vt'
            u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&json=1"
            r1 = requests.get(u1)
            print(r1.json())
            rid = r1.json().get("request")
            u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
            time.sleep(5)
            while True:
                r2 = requests.get(u2)
                print(r2.json())
                if r2.json().get("status") == 1:
                    form_tokon = r2.json().get("request")
                    break
                time.sleep(5)
            wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
            driver.execute_script(wirte_tokon_js)
            time.sleep(3)
            print("captcha solved")


        link='https://www.costaneranorte.cl/infraccion/VerificaInfraccion.aspx'
        #patente
        driver=webdriver.Chrome()
        driver.get(link)
        driver.find_element_by_xpath('//*[@id="txtpatente"]').send_keys(self.__patenteVehiculo)
        Solver(link)
        driver.find_element_by_xpath('//*[@id="Button1"]').click()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        fechas,categorias,estados=[],[],[]
        tabla_CostaneraNorte = soup.find_all('table')

        for detalles_CostaneraNorte in tabla_CostaneraNorte:
            for fecha_actual in detalles_CostaneraNorte.find_all('td')[0::3]:
                fechas.append(fecha_actual.text)
            for categoria_actual in detalles_CostaneraNorte.find_all('td')[1::3]:
                categorias.append(categoria_actual.text)
            for estado_actual in detalles_CostaneraNorte.find_all('td')[2::3]:
                estados.append(estado_actual.text)

        return [fechas, categorias, estados]

class Nororiente:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):

        API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
        APIKEY_2CAPTCHA="1abc234de56fab7c89012d34e56fa7b8"
        api_key = os.getenv(APIKEY_2CAPTCHA, API_KEY)
        solver= TwoCaptcha(api_key)
        sitekey='6LeGGUsUAAAAAGA45yjoGkJ__EKeRqa-KipeYSW-'
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--lang=es")
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.costaneranorte.cl/LoginNoFrecuente.html')
        driver.find_element_by_xpath('//*[@id="PATENTE"]').send_keys(self.__patenteVehiculo)
        driver.find_element_by_xpath('/html/body/div/section/div/div[2]/form/a').click()
        #print(str(driver.current_url))
        try:
            result=solver.recaptcha(sitekey=sitekey,
                                    url=driver.current_url)
        except:
            print('error')
        else:
            result=str(result.get('code'))
        driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{result}";')
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/a').click()
        soup=BeautifulSoup(driver.page_source,'html.parser')
        table=soup.find_all('table', id='TablaConvenioDeuda')
        convenios, documentos, deudas_vencidas, deudas_por_vencer, total_deudas, importes_a_pagar = [],[],[],[],[],[]
        for i in table:
            for convenio in i.find_all('td')[0::6]:
                if(convenio.text=='\xa0'):
                    pass
                else:
                    convenios.append(convenio.text)
            for documento in i.find_all('td')[1::6]:
                if(documento.text=='\xa0'):
                    pass
                else:
                    documentos.append(documento.text)
            for deuda_vencida in i.find_all('td')[2::6]:
                if(deuda_vencida.text=='\xa0'):
                    pass
                else:
                    deudas_vencidas.append(deuda_vencida.text)
            for deuda_por_vencer in i.find_all('td')[3::6]:
                if(deuda_por_vencer.text=='\xa0' or not(any(char.isdigit() for char in deuda_por_vencer.text))):
                    pass
                else:
                    deudas_por_vencer.append(deuda_por_vencer.text)
            for total_deuda in i.find_all('td')[4::6]:
                if(total_deuda.text=='\xa0'):
                    pass
                else:
                    total_deudas.append(total_deuda.text)
            for importe_a_pagar in i.find_all('td')[5::6]:
                if(importe_a_pagar.text=='\n\n'):
                    pass
                else:
                    importes_a_pagar.append(importe_a_pagar.text)

        return [convenios, documentos, deudas_vencidas, deudas_por_vencer, total_deudas, importes_a_pagar]            
class ViasExclusivas:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        driver.get('http://rrvv.fiscalizacion.cl')
        driver.find_element_by_xpath('//*[@id="patente"]').send_keys(self.__patenteVehiculo)
        idf=driver.find_element_by_xpath('//*[@id="captcha_widget"]/div[3]/img')
        img= idf.get_attribute('src')
        code = Functions().Solver(img,'Vias_exclusivas')
        driver.find_element_by_xpath('//*[@id="captcha_response"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="bBuscarPatente"]').click()
        time.sleep(2)
        tr_cont= 2
        td_cont= 1
        fechas = []
        lugares = []
        tipos = []
        juzgados = []

        while(True):
            try:
                fechas.append(driver.find_element_by_xpath('/html/body/div[1]/div/font/div[3]/div[2]/div[2]/form/div[1]/table/tbody/tr['+str(tr_cont)+']/td['+str(td_cont)+']').text)
                td_cont+=1
                lugares.append(driver.find_element_by_xpath('/html/body/div[1]/div/font/div[3]/div[2]/div[2]/form/div[1]/table/tbody/tr['+str(tr_cont)+']/td['+str(td_cont)+']').text)
                td_cont+=1
                tipos.append(driver.find_element_by_xpath('/html/body/div[1]/div/font/div[3]/div[2]/div[2]/form/div[1]/table/tbody/tr['+str(tr_cont)+']/td['+str(td_cont)+']').text)
                td_cont+=1
                juzgados.append(driver.find_element_by_xpath('/html/body/div[1]/div/font/div[3]/div[2]/div[2]/form/div[1]/table/tbody/tr['+str(tr_cont)+']/td['+str(td_cont)+']').text)
                td_cont=1
                tr_cont+=1

            except:
                break
        
        if(len(fechas)!=len(juzgados)):
            fechas.remove(fechas[len(fechas)-1])

        if(len(lugares)!=len(juzgados)):
            lugares.remove(lugares[len(lugares)-1])

        if(len(tipos)!=len(tipos)):
            tipos.remove(tipos[len(tipos)-1])
        
        return [fechas, lugares, tipos, juzgados]

class LampaSantiago:
    def __init__(self, patenteVehiculo, dv):
        self.__patenteVehiculo = patenteVehiculo
        self.__dv = dv

    def getInfracciones(self):
        driver = webdriver.Chrome()
        #patente,dv=patente.split('-')[0],patente.split('-')[1]
        driver.get('https://www.autoviasantiagolampa.cl/oficina-virtual/consultar-transito-sin-tag')
        idf=driver.find_element_by_xpath('//*[@id="imagen_captcha"]')
        img= idf.get_attribute('src')
        result=Functions().Solver(img,'lampa_santiago')
        driver.find_element_by_xpath('//*[@id="solicitar_contrasena_plate"]').send_keys(self.__patenteVehiculo)
        driver.find_element_by_xpath('//*[@id="solicitar_contrasena_plate_dv"]').send_keys(self.__dv)
        driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(result)
        driver.find_element_by_xpath('//*[@id="transitos_sin_sesion_form"]/div[3]/div/button').click()
        table=driver.find_element_by_xpath('/html/body/div/div[3]').text
        data=[]
        if ('usted no posee' not in table):
            soup=BeautifulSoup(driver.page_source,'html.parser')
            rows=((soup.find('table',class_='table table-bordered dataTable no-footer',role='grid')).find('tbody')).find_all('tr')
            for row in rows:
                cols=row.find_all('th')
                cols=[ele.text for ele in cols]
                data.append([ele for ele in cols if ele])

            return data

        else:
            return []

class DelSol:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        primary_link = 'http://www.autopistadelsol.cl/pago/valida'
        link1 = 'https://boton.unired.cl/BotonPago/IniciaFlujoOnline?u='
        Dato1={'patente':self.__patenteVehiculo}
        response=requests.post(primary_link,data=Dato1)
        soup=BeautifulSoup(response.text,'html.parser')
        for i in soup.find_all('input',value=True):
            link2=i['value']
        c_link=link1+str(link2)
        print(c_link)
        driver.get(c_link)
        while True:
            try:
                driver.find_element_by_xpath('/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[1]/div[2]/label/span').click()
                break
            except:
                time.sleep(1)
        driver.find_element_by_xpath('/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[1]/div[2]/label/span').click()
        cajaDeuda = driver.find_elements_by_xpath(
            '/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[2]/div')
        info=''
        for i in cajaDeuda:
            info = info+i.text

        driver.close()

        if('No existen' in info):
            return []

        else:

            string1_new = info.split('\n')
            array = []
            aux_array = []
            for i in string1_new:
                if('Transito sin Tag' in i):
                    array.append(aux_array)
                    aux_array = []
                    aux_array.append(i)
                else:
                    aux_array.append(i)

            array.append(aux_array)
            array.remove(array[0])
            
            indice = 0
            array_datos = []
            aux_array_datos = []
            array_detalles = []
            aux_array_detalles = []
            aux_array_detalles_2 = []

            for i in array:
                while(indice<5):
                    aux_array_datos.append(i[indice])
                    indice+=1

                array_datos.append(aux_array_datos)
                aux_array_datos = []

                while(True):
                    try:
                        aux_array_detalles.append(i[indice])
                        indice+=1
                    except:
                        indice=0
                        array_detalles.append(aux_array_detalles)
                        aux_array_detalles = []
                        break

            for i in array_datos:
                len_array_datos = len(array_datos)

                for j in range(0, len_array_datos):
                    if('Transito' in i[j]):
                        i[j] = (i[j].split('Ruta')[1]).strip()

                    if('Vence' in i[j]):
                        i.pop(j)
                        len_array_datos-=1

            for i in array_detalles:
                len_array_i = len(i)

                for j in range(0, len_array_i):
                    try:
                        k = i[j].split(':', 1)[1]
                    except:
                        k = i[j]

                    if(':' in k):
                        k = k.split(' ')

                    if(len(k)==2 and not('-' in k)):
                        aux_array_detalles.append(k[1])
                        aux_array_detalles.append(k[0])
                    else:
                        aux_array_detalles.append(k)

                aux_array_detalles_2.append(aux_array_detalles)
                aux_array_detalles = []

            array_detalles_final = []

            for i in aux_array_detalles_2:
                array_i = []
                aux_array_i = []

                for j in i:
                    if(j==self.__patenteVehiculo):
                        array_i.append(aux_array_i)
                        aux_array_i = []
                        aux_array_i.append(j) 
                    
                    else:
                        aux_array_i.append(j)

                array_i.append(aux_array_i)
                array_i.remove(array_i[0])
                array_detalles_final.append(array_i)

            return [array_datos, array_detalles_final]

#falta caso donde haya m??s de uno facturado y m??s de uno no facturado
class RutaMaipo:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        
        driver = webdriver.Chrome()
        driver.get('https://www.rutamaipo.cl/taginterurbano/pasaste-sin-tag')
        driver.find_element_by_xpath('//*[@id="patente"]').send_keys(self.__patenteVehiculo)
        driver.find_element_by_xpath('//*[@id="consultar_sintag"]').click()
        time.sleep(2)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div/button').click()
        except:
            pass

        try: 
            #'HKTW30'
            table1=driver.find_element_by_xpath('/html/body/div/main/div[1]/section/div[2]/div/form').text
            facturados = table1.split('\n')

            if(facturados[len(facturados)-2]=='$S/I'):
                facturados = []

            else:
                total = facturados[len(facturados)-2]
                cont_bucle = 0
                while(cont_bucle<5):
                    facturados.remove(facturados[0])
                    cont_bucle+=1

                cont_bucle=0
                while(cont_bucle<5):
                    facturados.remove(facturados[len(facturados)-1])
                    cont_bucle+=1

            facturados_final = [[],[],[], total]
            for i in facturados:
                facturados_final[0].append(i.split(' ')[0])
                facturados_final[1].append(i.split(' ')[1])
                facturados_final[2].append(i.split(' ')[2])

        except:
            facturados_final=[]
        
        try:
            #WT8329
            table2=driver.find_element_by_xpath('/html/body/div/main/div[1]/section/div[2]/div/div[2]').text
            noFacturados = table2.split('\n')
            noFacturados.remove(noFacturados[len(noFacturados)-1])

            cont_bucle = 0
            while(cont_bucle<4):
                noFacturados.remove(noFacturados[0])
                cont_bucle+=1

            noFacturados_final=[[],[],[]]
            for i in noFacturados:
                noFacturados_final[0].append(i.split(' ')[0])
                noFacturados_final[1].append(i.split(' ')[1])
                noFacturados_final[2].append(i.split(' ')[2])

        except:
            noFacturados_final=[]



        return [facturados_final,noFacturados_final]
        
class LosLibertadores:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        primary_link='https://www.autopistaloslibertadores.cl/pago/valida'
        link1='https://boton.unired.cl/BotonPago/IniciaFlujoOnline?u='
        datos={'patente':self.__patenteVehiculo}
        response=requests.post(primary_link,data=datos)
        soup=BeautifulSoup(response.text,'html.parser')
        for i in soup.find_all('input',value=True):
            link2=i['value']
        c_link=link1+str(link2)
        driver.get(c_link)
        while True:
            try:
                driver.find_element_by_xpath('/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[1]/div[2]/label/span').click()
                break
            except:
                time.sleep(1)
        driver.find_element_by_xpath('/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[1]/div[2]/label/span').click()
        cajaDeuda = driver.find_elements_by_xpath(
            '/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[2]/div')
        info=''
        for i in cajaDeuda:
            info = info+i.text

        driver.close()

        if('No existen' in info):
            return []

        else:

            string1_new = info.split('\n')
            array = []
            aux_array = []
            for i in string1_new:
                if('Transito sin Tag' in i):
                    array.append(aux_array)
                    aux_array = []
                    aux_array.append(i)
                else:
                    aux_array.append(i)

            array.append(aux_array)
            array.remove(array[0])
            
            indice = 0
            array_datos = []
            aux_array_datos = []
            array_detalles = []
            aux_array_detalles = []
            aux_array_detalles_2 = []

            for i in array:
                while(indice<5):
                    aux_array_datos.append(i[indice])
                    indice+=1

                array_datos.append(aux_array_datos)
                aux_array_datos = []

                while(True):
                    try:
                        aux_array_detalles.append(i[indice])
                        indice+=1
                    except:
                        indice=0
                        array_detalles.append(aux_array_detalles)
                        aux_array_detalles = []
                        break

            for i in array_datos:
                len_array_datos = len(array_datos)

                for j in range(0, len_array_datos):
                    if('Transito' in i[j]):
                        i[j] = (i[j].split('Ruta')[1]).strip()

                    if('Vence' in i[j]):
                        i.pop(j)
                        len_array_datos-=1

            for i in array_detalles:
                len_array_i = len(i)

                for j in range(0, len_array_i):
                    try:
                        k = i[j].split(':', 1)[1]
                    except:
                        k = i[j]

                    if(':' in k):
                        k = k.split(' ')

                    if(len(k)==2 and not('-' in k)):
                        aux_array_detalles.append(k[1])
                        aux_array_detalles.append(k[0])
                    else:
                        aux_array_detalles.append(k)

                aux_array_detalles_2.append(aux_array_detalles)
                aux_array_detalles = []

            array_detalles_final = []

            for i in aux_array_detalles_2:
                array_i = []
                aux_array_i = []

                for j in i:
                    if(j==self.__patenteVehiculo):
                        array_i.append(aux_array_i)
                        aux_array_i = []
                        aux_array_i.append(j) 
                    
                    else:
                        aux_array_i.append(j)

                array_i.append(aux_array_i)
                array_i.remove(array_i[0])
                array_detalles_final.append(array_i)

            print(array_datos)
            print(array_detalles_final)

            return [array_datos, array_detalles_final]

class ElPacifico:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        primary_link = 'http://www.rutasdelpacifico.cl/pago/valida'
        link1 = 'https://boton.unired.cl/BotonPago/IniciaFlujoOnline?u='
        datos={'patente':self.__patenteVehiculo}
        response=requests.post(primary_link,data=datos)
        soup=BeautifulSoup(response.text,'html.parser')
        for i in soup.find_all('input',value=True):
            link2=i['value']
        c_link=link1+str(link2)
        driver.get(c_link)
        while True:
            try:
                driver.find_element_by_xpath('/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[1]/div[2]/label/span').click()
                break
            except:
                time.sleep(1)
        driver.find_element_by_xpath('/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[1]/div[2]/label/span').click()
        cajaDeuda = driver.find_elements_by_xpath(
            '/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[2]/div')
        info=''
        for i in cajaDeuda:
            info = info+i.text

        driver.close()

        if('No existen' in info):
            return []

        else:

            string1_new = info.split('\n')
            array = []
            aux_array = []
            for i in string1_new:
                if('Transito sin Tag' in i):
                    array.append(aux_array)
                    aux_array = []
                    aux_array.append(i)
                else:
                    aux_array.append(i)

            array.append(aux_array)
            array.remove(array[0])
            
            indice = 0
            array_datos = []
            aux_array_datos = []
            array_detalles = []
            aux_array_detalles = []
            aux_array_detalles_2 = []

            for i in array:
                while(indice<5):
                    aux_array_datos.append(i[indice])
                    indice+=1

                array_datos.append(aux_array_datos)
                aux_array_datos = []

                while(True):
                    try:
                        aux_array_detalles.append(i[indice])
                        indice+=1
                    except:
                        indice=0
                        array_detalles.append(aux_array_detalles)
                        aux_array_detalles = []
                        break

            for i in array_datos:
                len_array_datos = len(array_datos)

                for j in range(0, len_array_datos):
                    if('Transito' in i[j]):
                        i[j] = (i[j].split('Ruta')[1]).strip()

                    if('Vence' in i[j]):
                        i.pop(j)
                        len_array_datos-=1

            for i in array_detalles:
                len_array_i = len(i)

                for j in range(0, len_array_i):
                    try:
                        k = i[j].split(':', 1)[1]
                    except:
                        k = i[j]

                    if(':' in k):
                        k = k.split(' ')

                    if(len(k)==2 and not('-' in k)):
                        aux_array_detalles.append(k[1])
                        aux_array_detalles.append(k[0])
                    else:
                        aux_array_detalles.append(k)

                aux_array_detalles_2.append(aux_array_detalles)
                aux_array_detalles = []

            array_detalles_final = []

            for i in aux_array_detalles_2:
                array_i = []
                aux_array_i = []

                for j in i:
                    if(j==self.__patenteVehiculo):
                        array_i.append(aux_array_i)
                        aux_array_i = []
                        aux_array_i.append(j) 
                    
                    else:
                        aux_array_i.append(j)

                array_i.append(aux_array_i)
                array_i.remove(array_i[0])
                array_detalles_final.append(array_i)

            print(array_datos)
            print(array_detalles_final)

            return [array_datos, array_detalles_final]

while(True):

    patente = input('Ingrese patente: ')
    patente_aux = list(patente)
    dv = input('Ingrese d??gito verificador: ')
    cont_numeros = 0
    condicion_continuar=False

    if(len(patente_aux)==6):
        for caracter in patente_aux:
            try:
                aux = int(caracter)
                cont_numeros+=1
            except:
                pass

        if(cont_numeros==4):
            value = Functions.dvFormatoAA1000(patente, dv)
            condicion_continuar = True

        elif(cont_numeros==2):
            value = Functions.dvNuevoFormatoPPU(patente, dv)
            condicion_continuar = True
        
        else:
            print('Error al ingresar la patente y/o el d??gito verificador\nVuelva a intentarlo\n\n')

    elif(len(patente_aux)==5):
        value = Functions.dvNuevoFormatoPPUMotos(patente, dv)
        condicion_continuar = True

    else:
        print('Error al ingresar la patente y/o el d??gito verificador\nVuelva a intentarlo\n\n')

    if(condicion_continuar==True):
        if(value==True):
            break

        else:
            print('Error al ingresar la patente y/o el d??gito verificador\nVuelva a intentarlo\n\n')
    
#auto=Vehiculo(patente)
#auto.setInfraccionesNororiente(Nororiente(auto.getPatente()).getInfracciones())
#auto.getInfraccionesNororiente()


    

# Para obtener Registro de Transporte Publico
# auto.setRegistroTransportePublico(TransportePublico(auto.getPatente()).resultado())
# auto.getRegistroTransportePublico()

# Para obtener Revision Tecnica
#auto.setRegistroRevisionTecnica(RevisionTecnica(auto.getPatente(),"2a2b5480b431e8976a70ebbf3d38f550",'http://www.prt.cl/Paginas/RevisionTecnica.aspx').resultado())
#auto.getRegistroRevisionTecnica()

# Para obtener Encargo Robo
# auto.setRegistroEncargoRobo(EncargoRobo(auto.getPatente(), "2a2b5480b431e8976a70ebbf3d38f550", 'https://www.autoseguro.gob.cl').resultado())
# auto.getRegistroEncargoRobo()

# auto.setInfraccionesLampaSantiago(LampaSantiago(auto.getPatente(), '2').getInfracciones())
# auto.getInfraccionesLampaSantiago()
