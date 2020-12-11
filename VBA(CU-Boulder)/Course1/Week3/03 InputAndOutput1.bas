Option Explicit


Sub SquareRoot()

    Dim x As Double, y As Double

    x = InputBox("Enter a number :")
    y = Sqr(x)  'Get only the positive square root of x

    MsgBox ("The square root of your number is " & y & ".")

End Sub


Sub SquareRoot2()

    Dim x As Double, y As Double

    x = InputBox("Enter a number :")
    y = Sqr(x)  'Get only the positive square root of x

    ActiveCell = FormatNumber(y, 2) '2 ← numDigitsAfterDecimal as Integer

End Sub


Sub SquareRoot3()

    Dim x As Double, y As Double

    x = InputBox("Enter a number :")
    y = Sqr(x)  'Get only the positive square root of x

    Range("C3") = FormatNumber(y, 2)

End Sub


Sub SquareRoot4()

    Dim x As Double, y As Double

    x = Range("A1")
    y = Sqr(x)  'Get only the positive square root of x

    MsgBox ("The square root of your number is " & y & ".")

End Sub
