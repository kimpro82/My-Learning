Option Explicit

Sub Debugging()
'This Sub calculates the exponential of a number using the Taylor series expansion
    Dim i As Integer, s As Double, x As Double
    x = 2.1
    For i = 0 To 12
        s = s + x ^ i / MyFactorial(i)
        Debug.Assert s < 5
    Next i
    MsgBox ("The exponential of " & x & " is " & FormatNumber(s, 3))
End Sub

Function MyFactorial(x As Integer) As Long
    Dim k As Integer, f As Long
    f = 1
    For k = 1 To x
        f = f * k
    Next k
    MyFactorial = f
End Function
