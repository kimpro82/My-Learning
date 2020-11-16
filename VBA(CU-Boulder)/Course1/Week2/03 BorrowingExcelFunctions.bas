Option Explicit

'Function 1

Function Range2(rng As Range) As Double
'Can't find why 'range' starts with a lowercase letter

    Range2 = WorksheetFunction.Max(rng) - WorksheetFunction.Min(rng)
    'Naming as 'Range' can cause conflict with origin Range() in VBA

End Function


'Function 2

Function ConeVol2(R As Double, h As Double) As Double
    
    Dim pi As Double
    'pi = 4 * Atn(1) 'VBA doesn't have pi()
    pi = WorksheetFunction.pi() 'easier way than making pi() in VBA
    ConeVol2 = pi * R ^ 2 * h / 3

End Function
