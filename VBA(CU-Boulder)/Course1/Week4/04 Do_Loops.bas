Option Explicit


Sub DoLoop()

    Dim x As Double
    x = 20
    
    Do
        x = Sqr(x)
        If x < 1.1 Then Exit Do
        x = x ^ 1.5
    Loop

    MsgBox x

End Sub


Sub DoWhile()

    Dim i As Integer, ilim As Integer
    i = 4
    ilim = 25

    Do While i < ilim
        i = i + 1
    Loop

    MsgBox i

End Sub


Sub LoopUntil()

    Dim i As Integer, ilim As Integer
    'If do not define i, i becomes 0 automatically.
    ilim = 25

    Do
        i = i + 1
    Loop Until i > ilim

    MsgBox i

End Sub
