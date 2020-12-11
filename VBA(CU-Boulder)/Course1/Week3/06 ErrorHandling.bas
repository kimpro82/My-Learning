Option Explicit


Sub ErrorHandling()

    Dim x As Double

    x = InputBox("Please enter volume in gallons :")
    MsgBox (x & " gallons is equal to " & FormatNumber(x / 7.48, 2) & " cubic feet.")

End Sub


Sub ErrorHandling2()

    Dim x As Double

On Error GoTo Here  'a kind of bookmark

    x = InputBox("Please enter volume in gallons :")
    MsgBox (x & " gallons is equal to " & FormatNumber(x / 7.48, 2) & " cubic feet.")

    Exit Sub    'avoid running Here when it works well

Here:
    MsgBox ("There was an error!")

End Sub
