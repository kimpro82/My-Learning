## Week 3 : Exchanging Information Between Excel and VBA


### 01 Introduction.bas

```VBA
Option Explicit
```

```VBA
Sub ClearCells()
    
    Selection.Clear

End Sub
```

```VBA
Sub CopyCells()

    Range("A1:A4").Copy Range("C1:C4")

End Sub
```

```VBA
Sub RangeTest()

    MsgBox Range("A1")

End Sub
```

```VBA
Sub RangeTest2()

    Range("A1").Interior.ColorIndex = 50

End Sub
```


### 02 MethodAndProperty.bas

```VBA
Option Explicit
```

##### Method

```VBA
Sub Method1()

    MsgBox Range("B2:C6").Range("B2")
    'Refers relatively from the fixed cell

End Sub
```

```VBA
Sub Method2()

    MsgBox Selection.Range("B2")
    'Refers relatively from the selected cell

End Sub
```

```VBA
Sub Method3()

    MsgBox Cells(3, 2)

End Sub
```

```VBA
Sub Method4()

    MsgBox Selection.Cells(3, 2)
    'Refers relatively from the selected cell

End Sub
```

```VBA
Sub Method5()

    Selection.Cells(3, 2).Select
    'Changes the selected cell

End Sub
```

```VBA
Sub Method6()

    Selection.Cells(2, 3).Activate
    'Changes the active cell (different from changing a selected cell)

End Sub
```

```VBA
Sub Method7()

    MsgBox ActiveCell.Offset(1, 1)
    'Finds the relatively located value from the active cell
    'Doesn't affect the current active cell and the selected area

End Sub
```

```VBA
Sub Method8()

    ActiveCell.Offset(-2, 1).Select
    'Finds the relatively located value from the active cell
    'Changes the seleted cell's location

End Sub
```

##### Property

```VBA
Sub Property1()

    Dim nr As Integer, nc As Integer

    nr = Range("a1:c5").Rows.Count
    nc = Range("a1:c5").Columns.Count
    'Just count row or columns's number, no matter if the cells have values

    MsgBox (nr & " " & nc)

End Sub
```

```VBA
Sub Property2()

    Dim rowindex As Integer, col As String

    rowindex = InputBox("Enter row number:")
    col = InputBox("Enter column letter:")

    MsgBox Range(col & rowindex)
    'Returns the value of the ranged cell

End Sub
```


### 03 InputAndOutput1.bas

```VBA
Option Explicit
```

```VBA
Sub SquareRoot()

    Dim x As Double, y As Double

    x = InputBox("Enter a number :")
    y = Sqr(x)  'Get only the positive square root of x

    MsgBox ("The square root of your number is " & y & ".")

End Sub
```

```VBA
Sub SquareRoot2()

    Dim x As Double, y As Double

    x = InputBox("Enter a number :")
    y = Sqr(x)  'Get only the positive square root of x

    ActiveCell = FormatNumber(y, 2) '2 ← numDigitsAfterDecimal as Integer

End Sub
```

```VBA
Sub SquareRoot3()

    Dim x As Double, y As Double

    x = InputBox("Enter a number :")
    y = Sqr(x)  'Get only the positive square root of x

    Range("C3") = FormatNumber(y, 2)

End Sub
```

```VBA
Sub SquareRoot4()

    Dim x As Double, y As Double

    x = Range("A1")
    y = Sqr(x)  'Get only the positive square root of x

    MsgBox ("The square root of your number is " & y & ".")

End Sub
```


### 04 InputAndOutput2.bas

```VBA
Option Explicit
```

```VBA
Sub SelectionCells()

    Dim x As Double, y As Double

    x = Selection.Cells(2, 2)
    y = x ^ 2

    Range("A1") = y

End Sub
```

```VBA
Sub SelectionCount()

    Dim nr As Integer, nc As Integer

    nr = Selection.Rows.Count
    nc = Selection.Columns.Count

    MsgBox ("Your selection has " & nr & " rows and " & nc & " columns.")

End Sub
```

```VBA
Sub ActiveCellOffset()

    Dim x As Double, y As Double, z As Double

    x = InputBox("Enter a number :")
    y = ActiveCell
    z = x + y

    ActiveCell.Offset(2, 2) = z

End Sub
```

```VBA
Sub ActiveCellOffset2() 'the same with the above

    Dim x As Double

    x = InputBox("Enter a number :")
    
    ActiveCell.Offset(2, 2) = ActiveCell + x

End Sub
```


### 05 InputAndOutput3.bas

```VBA
Option Explicit
```

```VBA
Sub Test()

    Dim x As Integer, rng As String, y As Integer, z As Integer

    x = InputBox("Please enter a value to add to the vlaue in cell A1 :")
    y = Range("A1")
    z = x + y

    rng = InputBox("Please enter cell to place result in :")
        'also available to enter range
    Range(rng) = z

End Sub
```


### 06 ErrorHandling.bas

```VBA
Option Explicit
```

```VBA
Sub ErrorHandling()

    Dim x As Double

    x = InputBox("Please enter volume in gallons :")
    MsgBox (x & " gallons is equal to " & FormatNumber(x / 7.48, 2) & " cubic feet.")

End Sub
```

```VBA
Sub ErrorHandling2()

    Dim x As Double

On Error GoTo Here  'a kind of bookmark

    x = InputBox("Please enter volume in gallons :")
    MsgBox (x & " gallons is equal to " & FormatNumber(x / 7.48, 2) & " cubic feet.")

    Exit Sub    'avoid running Here when it works well

Here:
    MsgBox ("There was an error!")

End Sub
```
