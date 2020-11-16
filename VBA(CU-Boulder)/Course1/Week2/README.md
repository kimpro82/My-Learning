## Week 2 : User-Defined VBA Functions

### 01 UserDefinedFunction.bas
```VBA
Option Explicit

'Function 1
Function ConeVol(R As Double, h As Double) As Double
    'Dim R As Double 'Cause compile error : Duplicate declaration
    Dim pi As Double
    pi = 4 * Atn(1)
    ConeVol = pi * R ^ 2 * h / 3

End Function
```
```VBA
'Function 2
Function Efficiency(w As Double, s As Double) As Double

    Efficiency = (6.12 - w / 60000) * 0.92 ^ ((s - 55) / 60)

End Function
```

### 02 Add-in.bas
```VBA
'Add-in

'Save the file including user-defined function as "Excel Add-in" type

'Then saving location will be changed to \Microsoft\Addins
'(Not necessary to maintain this folder)

'Open a new file

'Option > Add-ins > Manage : Excel Add-ins
'> Call the file including user-defined function
```

### 03 BorrowingExcelFunctions.bas
```VBA
Option Explicit

'Function 1

Function Range2(rng As Range) As Double
'Can't find why 'range' starts with a lowercase letter

    Range2 = WorksheetFunction.Max(rng) - WorksheetFunction.Min(rng)
    'Naming as 'Range' can cause conflict with origin Range() in VBA

End Function
```

- There appears a conflict problem with declaring `range()` that has the same name with original VBA funtion `Range()`.  It isn't an error in itself yet, but makes us unable to call the original `Range()` properly so that finally leads errors. First, this error can be solved by changing the function's name, like `Range2()`.
- However, the autocomplete function in VBA seems to maintain the name `range()` only in lower case letters, so we need to also clear it. The below is a mothod to recover the original name `Range()`. I found it from the StackOverFlow page.  
☞ https://stackoverflow.com/questions/27425541/vba-automatically-changing-range-to-range.
```VBA
Dim Range As Range
```

```VBA
'Function 2

Function ConeVol2(R As Double, h As Double) As Double
    
    Dim pi As Double
    'pi = 4 * Atn(1) 'VBA doesn't have pi()
    pi = WorksheetFunction.pi() 'easier way than making pi() in VBA
    ConeVol2 = pi * R ^ 2 * h / 3

End Function
```

### 04 ModularProgramming.bas
```VBA
Option Explicit


Sub AnalyzeData()

    Call Remove9999
    Call EliminateText
    Range("A:A").SpecialCells(xlCellTypeBlanks).EntireRow.Delete
    Call RemoveOutliers
    Call CalculateStats

End Sub
```
```VBA
Sub Remove9999()

    Dim i As Integer, nr As Integer
    
    nr = Selection.Rows.Count
    
    For i = 1 To nr
        If Selection.Cells(i, 1) = 9999 Then Selection.Cells(i, 1) = ""
    Next i

End Sub
```
```VBA
Sub EliminateText()

    Dim i As Integer, nr As Integer

    nr = Selection.Rows.Count

    For i = 1 To nr
        If Not IsNumeric(Selection.Cells(i, 1)) Then
            Selection.Cells(i, 1) = ""
        End If
    Next i

End Sub
```
```VBA
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
```
```VBA
Sub CalculateStats()

    Dim itm As Object, avg As Double, std As Double

    avg = WorksheetFunction.Average(Selection)
    std = WorksheetFunction.StDev_S(Selection)

    MsgBox ("Average is " & FormatNumber(avg, 2) & " and standard deviation is " & FormatNumber(std))

End Sub
```

### 05 RunInAnotherFile.bas
```VBA
Option Explicit

Sub ApplicationRunExample()
    
    Application.Run "'RunMe.xlsm'!RunMe"

End Sub
```
```VBA
Sub ApplicationRunExample2()

    Dim FileName As String, aWB As Workbook

    FileName = Application.GetOpenFilename("Excel Files (*.xlsm), *.xlsm")
    Workbooks.Open FileName

    Set aWB = ActiveWorkbook
    Application.Run "'RunMe.xlsm'!RunMe" 'It can be changed something better ...
    aWB.Close SaveChanges:=False

End Sub
```
