## Week 4 : Programming structures in VBA


### 01 If_Then.bas

```VBA
Option Explicit
```

```VBA
Sub MessageIfEven()

    Dim x As Integer
    x = InputBox("Please enter a number.")

    If x Mod 2 = 0 Then
        MsgBox ("Your number is even.")
    End If

End Sub
```

```VBA
Sub ReplaceBlankWithZero()

    If ActiveCell = "" Then
        ActiveCell = 0
    End If

End Sub
```


### 02 If_Then_Else.bas

```VBA
Option Explicit
```

```VBA
Sub AddOrSubtractTwenty()

    If ActiveCell > 0 Then
        ActiveCell = ActiveCell + 20
    Else
        ActiveCell = ActiveCell - 20
    End If

End Sub
```

```VBA
Function bizbuz(x As Integer) As String
'"As String" makes this function not to return "0"

    If x Mod 3 = 0 Then

        If x Mod 5 = 0 Then
            bizbuz = "bizbuz"
        Else
            bizbuz = "biz"
        
        End If

    Else

        If x Mod 5 = 0 Then
            bizbuz = "buz"
        End If

    End If

End Function
```


### 03 If_Then_ElseIf.bas

```VBA
Option Explicit
```

```VBA
Function grade(score As Double) As String

    If score >= 90 Then
        grade = "A"
    ElseIf score >= 80 Then
        grade = "B"
    ElseIf score >= 70 Then
        grade = "C"
    ElseIf score >= 60 Then
        grade = "D"
    Else
        grade = "F"
    End If

End Function
```


### 04 Do_Loops.bas

```VBA
Option Explicit
```

```VBA
Sub DoLoop()

    Dim x As Double
    x = 20
    
    Do
        x = Sqr(x)
        If x < 1.1 Then Exit Do
        x = x ^ 1.5
    Loop

    MsgBox x

End Sub
```
> 1.08800974666585

```VBA
Sub DoWhile()

    Dim i As Integer, ilim As Integer
    i = 4
    ilim = 25

    Do While i < ilim
        i = i + 1
    Loop

    MsgBox i

End Sub
```
> 25

```VBA
Sub LoopUntil()

    Dim i As Integer, ilim As Integer
    'If do not define i, i becomes 0 automatically.
    ilim = 25

    Do
        i = i + 1
    Loop Until i > ilim

    MsgBox i

End Sub
```
> 26


### 05 Loop_Examples.bas

```VBA
Option Explicit
```

```VBA
Sub ValidateInput()

    Dim P As Double

    Do
        P = InputBox("Enter percent conversion :")
        If P >= 0 And P <= 100 Then Exit Do
        'also can write "0 <= P <= 100"
        MsgBox ("Percentage must be between 0 and 100")
    Loop

End Sub
```

```VBA
Sub GuessingGame()

    Dim n As Integer, G As Integer
    n = WorksheetFunction.RandBetween(1, 10)

    Do
        G = InputBox("What's the random number between 1 and 10?")
        If G = n Then Exit Do
        MsgBox ("Guess again!")
    Loop

    MsgBox ("Congratulations! You guessed the number!")

End Sub
```


### 06 For_Next.bas

```VBA
Option Explicit
```

```VBA
Function Divisible(n As Integer) As Integer

    Dim i As Integer, c As Integer

    For i = 1 To n
        If i Mod 3 = 0 Or i Mod 5 = 0 Then
            c = c + 1
        End If
    Next i

    Divisible = c

End Function
```

```VBA
Sub CountFives()

    Dim nr As Integer, i As Integer, c As Integer
    nr = Selection.Rows.Count

    For i = 1 To nr
        If Selection.Cells(i, 1) = 5 Then c = c + 1
    Next i 'i goes nr + 1

    MsgBox ("There are " & c & " fivs in your selection.")

End Sub
```
