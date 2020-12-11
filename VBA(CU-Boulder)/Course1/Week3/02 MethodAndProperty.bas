Option Explicit


Sub Method1()

    MsgBox Range("B2:C6").Range("B2")
    'Refers relatively from the fixed cell

End Sub


Sub Method2()

    MsgBox Selection.Range("B2")
    'Refers relatively from the selected cell

End Sub


Sub Method3()

    MsgBox Cells(3, 2)

End Sub


Sub Method4()

    MsgBox Selection.Cells(3, 2)
    'Refers relatively from the selected cell

End Sub


Sub Method5()

    Selection.Cells(3, 2).Select
    'Changes the selected cell

End Sub


Sub Method6()

    Selection.Cells(2, 3).Activate
    'Changes the active cell (different from changing a selected cell)

End Sub


Sub Method7()

    MsgBox ActiveCell.Offset(1, 1)
    'Finds the relatively located value from the active cell
    'Doesn't affect the current active cell and the selected area

End Sub


Sub Method8()

    ActiveCell.Offset(-2, 1).Select
    'Finds the relatively located value from the active cell
    'Changes the seleted cell's location

End Sub


Sub Property1()

    Dim nr As Integer, nc As Integer

    nr = Range("a1:c5").Rows.Count
    nc = Range("a1:c5").Columns.Count
    'Just count row or columns's number, no matter if the cells have values

    MsgBox (nr & " " & nc)

End Sub


Sub Property2()

    Dim rowindex As Integer, col As String

    rowindex = InputBox("Enter row number:")
    col = InputBox("Enter column letter:")

    MsgBox Range(col & rowindex)
    'Returns the value of the ranged cell

End Sub
