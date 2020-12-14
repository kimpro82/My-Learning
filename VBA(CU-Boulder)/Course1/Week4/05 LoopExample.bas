Option Explicit


Sub ValidateInput()

    Dim P As Double

    Do
        P = InputBox("Enter percent conversion :")
        If P >= 0 And P <= 100 Then Exit Do
        'also can write "0 <= P <= 100"
        MsgBox ("Percentage must be between 0 and 100")
    Loop

End Sub


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
