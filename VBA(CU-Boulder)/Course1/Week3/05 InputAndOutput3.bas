Option Explicit


Sub Test()

    Dim x As Integer, rng As String, y As Integer, z As Integer

    x = InputBox("Please enter a value to add to the vlaue in cell A1 :")
    y = Range("A1")
    z = x + y

    rng = InputBox("Please enter cell to place result in :")
        'also available to enter range
    Range(rng) = z

End Sub
