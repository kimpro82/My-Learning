## Week 1 : Macro recording, VBA procedures, and debugging

### 01 Hello.bas
```VBA
Sub Test()
    MsgBox "Hello"
End Sub
```

### 02 Selection.bas
```VBA
Sub Test2()
    Selection.Interior.ColorIndex = 7
End Sub
```

### 03 Comment.bas
```VBA
Sub Test3()
    MsgBox Selection.Interior.ColorIndex
    'This is a comment
End Sub
```

### 04 RecordingMacro.bas
```VBA
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
```
```VBA
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
```

### 05 SquareNumber.bas
```VBA
Sub SquareNumber()
    Dim x As Double, y As Double
    x = InputBox("Enter a number :")
    y = x ^ 2
    MsgBox ("The square of your number is " & y & ".")
End Sub
```

### 06 Function.bas
```VBA
Function Savings(P As Double, i As Double, n As Integer) As Double
    Savings = P * (1 + i) ^ n
End Function
```
```VBA
Function GR()
    GR = (Sqr(5) - 1) / 2
End Function
```

### 07 Call.bas
```VBA
Sub DeleteRows(n1 As Integer, n2 As Integer)
    Rows(n1 & ":" & n2).EntireRow.Select
    Selection.Delete Shift:=xlUp
End Sub

Sub RunDeleteRows()
    Call DeleteRows(11, 12)
End Sub
```

### 08 OptionExplicit.bas
```VBA
Option Explicit
'오류 있으면 실행 안 됨

Sub OptionExplicit()
    Dim Variable As Integer
    Variable = 10
    MsgBox Variable + 2
    MsgBox Variable + 4
    MsgBox Variable + 6
End Sub
```

### 09 Scope.bas
```VBA
Option Explicit

Sub Sphere()
    Dim R As Double, Area As Double, Volume As Double, pi As Double
    pi = 4 * Atn(1)
    R = InputBox("Please enter radius: ")
    Area = 4 * pi * R ^ 2
    MsgBox ("Surface area of the sphere is :" & FormatNumber(Area, 1) & ".")
    Volume = SphereVolume(R)
    MsgBox ("Volume of the sphere is " & FormatNumber(Volume, 1) & ".")
End Sub

Function SphereVolume(rad As Double) As Double
    Dim pi As Double ' 없으면 실행 안 됨. 위의 pi는 지역변수이기 때문에
    pi = 4 * Atn(1)
    SphereVolume = 4 / 3 * pi * rad ^ 3
End Function

'Public pi As Double 을 선언하고 시작해도 된다
```

### 10 Static.bas
```VBA
Option Explicit

Sub NonStaticExample()
    Dim d As Integer
    d = d + 1
    MsgBox d
End Sub

Sub StaticExample(Optional reset As Boolean)
    Static d As Integer
    If reset Then d = 0
    d = d + 1
    MsgBox d
End Sub

Sub ResetStatic()
    StaticExample (True)
End Sub
```

### 11 Debugging.bas
```VBA
Option Explicit

Sub Debugging()
'This Sub calculates the exponential of a number using the Taylor series expansion
    Dim i As Integer, s As Double, x As Double
    x = 2.1
    For i = 0 To 12
        s = s + x ^ i / MyFactorial(i)
        Debug.Assert s < 5
    Next i
    MsgBox ("The exponential of " & x & " is " & FormatNumber(s, 3))
End Sub

Function MyFactorial(x As Integer) As Long
    Dim k As Integer, f As Long
    f = 1
    For k = 1 To x
        f = f * k
    Next k
    MyFactorial = f
End Function
```
