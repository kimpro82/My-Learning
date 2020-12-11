Option Explicit


Sub SelectionCells()

    Dim x As Double, y As Double

    x = Selection.Cells(2, 2)
    y = x ^ 2

    Range("A1") = y

End Sub


Sub SelectionCount()

    Dim nr As Integer, nc As Integer

    nr = Selection.Rows.Count
    nc = Selection.Columns.Count

    MsgBox ("Your selection has " & nr & " rows and " & nc & " columns.")

End Sub


Sub ActiveCellOffset()

    Dim x As Double, y As Double, z As Double

    x = InputBox("Enter a number :")
    y = ActiveCell
    z = x + y

    ActiveCell.Offset(2, 2) = z

End Sub


Sub ActiveCellOffset2() 'the same with the above

    Dim x As Double

    x = InputBox("Enter a number :")
    
    ActiveCell.Offset(2, 2) = ActiveCell + x

End Sub
