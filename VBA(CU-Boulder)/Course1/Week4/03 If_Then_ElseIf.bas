Option Explicit


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
