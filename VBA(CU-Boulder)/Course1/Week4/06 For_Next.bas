Option Explicit


Function Divisible(n As Integer) As Integer

    Dim i As Integer, c As Integer

    For i = 1 To n
        If i Mod 3 = 0 Or i Mod 5 = 0 Then
            c = c + 1
        End If
    Next i

    Divisible = c

End Function


Sub CountFives()

    Dim nr As Integer, i As Integer, c As Integer
    nr = Selection.Rows.Count

    For i = 1 To nr
        If Selection.Cells(i, 1) = 5 Then c = c + 1
    Next i 'i goes nr + 1

    MsgBox ("There are " & c & " fivs in your selection.")

End Sub
