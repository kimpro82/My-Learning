Option Explicit

'Function 1
Function ConeVol(R As Double, h As Double) As Double
    'Dim R As Double 'Cause compile error : Duplicate declaration
    Dim pi As Double
    pi = 4 * Atn(1)
    ConeVol = pi * R ^ 2 * h / 3

End Function


'Function 2
Function Efficiency(w As Double, s As Double) As Double

    Efficiency = (6.12 - w / 60000) * 0.92 ^ ((s - 55) / 60)

End Function
