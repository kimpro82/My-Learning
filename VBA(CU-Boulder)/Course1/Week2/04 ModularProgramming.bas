Option Explicit


Sub AnalyzeData()

    Call Remove9999
    Call EliminateText
    Range("A:A").SpecialCells(xlCellTypeBlanks).EntireRow.Delete
    Call RemoveOutliers
    Call CalculateStats

End Sub


Sub Remove9999()

    Dim i As Integer, nr As Integer
    
    nr = Selection.Rows.Count
    
    For i = 1 To nr
        If Selection.Cells(i, 1) = 9999 Then Selection.Cells(i, 1) = ""
    Next i

End Sub


Sub EliminateText()

    Dim i As Integer, nr As Integer

    nr = Selection.Rows.Count

    For i = 1 To nr
        If Not IsNumeric(Selection.Cells(i, 1)) Then
            Selection.Cells(i, 1) = ""
        End If
    Next i

End Sub


Sub RemoveOutliers()

    Dim q1 As Double, q3 As Double, IQR As Double, f1 As Double, f3 As Double
    Dim itm As Object

    q1 = WorksheetFunction.Percentile_Exc(Selection, 0.25)
    q3 = WorksheetFunction.Percentile_Exc(Selection, 0.75)

    IQR = q3 - q1

    f1 = q1 - 1.5 * IQR
    f3 = q3 + 1.5 * IQR

    For Each itm In Selection
        If itm < f1 Or itm > f3 Then
            itm.Delete
        End If
    Next

End Sub


Sub CalculateStats()

    Dim itm As Object, avg As Double, std As Double

    avg = WorksheetFunction.Average(Selection)
    std = WorksheetFunction.StDev_S(Selection)

    MsgBox ("Average is " & FormatNumber(avg, 2) & " and standard deviation is " & FormatNumber(std))

End Sub
