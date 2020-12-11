Option Explicit


Sub ClearCells()
    
    Selection.Clear

End Sub


Sub CopyCells()

    Range("A1:A4").Copy Range("C1:C4")

End Sub


Sub RangeTest()

    MsgBox Range("A1")

End Sub


Sub RangeTest2()

    Range("A1").Interior.ColorIndex = 50

End Sub
