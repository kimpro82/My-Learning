Sub DeleteRows(n1 As Integer, n2 As Integer)
    Rows(n1 & ":" & n2).EntireRow.Select
    Selection.Delete Shift:=xlUp
End Sub

Sub RunDeleteRows()
    Call DeleteRows(11, 12)
End Sub
