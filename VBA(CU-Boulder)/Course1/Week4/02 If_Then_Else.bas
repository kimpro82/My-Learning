Option Explicit


Sub AddOrSubtractTwenty()

    If ActiveCell > 0 Then
        ActiveCell = ActiveCell + 20
    Else
        ActiveCell = ActiveCell - 20
    End If

End Sub


Function bizbuz(x As Integer) As String
'"As String" makes this function not to return "0"

    If x Mod 3 = 0 Then

        If x Mod 5 = 0 Then
            bizbuz = "bizbuz"
        Else
            bizbuz = "biz"
        
        End If

    Else

        If x Mod 5 = 0 Then
            bizbuz = "buz"
        End If

    End If

End Function
