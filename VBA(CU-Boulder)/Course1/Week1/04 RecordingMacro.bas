Sub 매크로1()
'
' 매크로1 매크로
'

'
    Range("B4:B6").Select
    Selection.Font.Bold = True
    Range("C4:C5").Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 65535
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
End Sub


Sub 매크로2()
'
' 매크로2 매크로
'

'
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 65535
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
    ActiveCell.Offset(1, 0).Range("A1:C1").Select
    Selection.Font.Italic = True
End Sub
