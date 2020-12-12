Option Explicit


Sub MessageIfEven()

    Dim x As Integer
    x = InputBox("Please enter a number.")

    If x Mod 2 = 0 Then
        MsgBox ("Your number is even.")
    End If

End Sub


Sub ReplaceBlankWithZero()

    If ActiveCell = "" Then
        ActiveCell = 0
    End If

End Sub
