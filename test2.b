10 LET M0 = 9        ; number to find the sqrt of
20 LET M1 = 1        ; initial guess
30 LET M2 = 0        ; scratch
40 LET M3 = 0        ; old value
50 LET M4 = 0        ; delta
60 LET M5 = 0        ; threshold (tolerance)
70 LET M5 = 1
80 LET M4 = 10       ; loop start
90 LET M3 = M1
100 LET M2 = M0 / M1
110 LET M1 = (M1 + M2) / 2
120 LET M4 = M3 - M1
130 IF M4 < 0 GOTO 140
135 GOTO 150
140 LET M4 = 0 - M4
150 IF M4 > M5 GOTO 80
160 PRINT M1
