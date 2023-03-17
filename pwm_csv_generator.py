import numpy as np

T_rise = 70e-9
T_fall = 30e-9
T_dead = 520e-9

if __name__ == "__main__":
    file_ref = input("参照する時系列データを入力 :")
    f_carr = float(input("キャリア周波数(Hz) :"))
    T = 1.0/f_carr
    T_trans = max((T_rise, T_fall))

    ref_dat = np.loadtxt(file_ref, delimiter=",").T
    x_ref = ref_dat[1]
    t_ref = ref_dat[0]
    t_end = t_ref[-1]

    OUT_HS = []
    OUT_LS = []
    t = t_ref[0]
    i = 0
    cnt = 0

    while t < t_end:
        while t > t_ref[i]:
            i += 1
        
        if (T_trans+T_dead)/T < x_ref[i] < (T-T_trans-T_dead)/T:
            OUT_HS.extend([[t+T*x_ref[i], 1], [t+T*x_ref[i]+T_fall, 0], [t+T-T_rise-T_dead, 0], [t+T, 1]])
            OUT_LS.extend([[t+T*x_ref[i]+T_dead, 0], [t+T*x_ref[i]+T_rise+T_dead, 1], [t+T-T_fall, 1], [t+T, 0]])
        
        elif (T_trans+T_dead)/T >= x_ref[i]:
            if len(OUT_HS) > 0:
                OUT_HS[-1][1] = 0
                OUT_LS[-1][1] = 1
            else:
                OUT_HS.append([t, 0])
                OUT_LS.append([t, 1])

            OUT_HS.append([t+T, 0])
            OUT_LS.append([t+T, 1])
        
        elif x_ref[i] >= (T-T_trans-T_dead)/T:
            if len(OUT_HS) > 0:
                OUT_HS[-1][1] = 1
                OUT_LS[-1][1] = 0
            else:
                OUT_HS.append([t, 1])
                OUT_LS.append([t, 0])

            OUT_HS.append([t+T, 1])
            OUT_LS.append([t+T, 0])
        
        t += T

    np.savetxt("out_HS.csv", OUT_HS, delimiter=",")
    np.savetxt("out_LS.csv", OUT_LS, delimiter=",")