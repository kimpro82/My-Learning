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
