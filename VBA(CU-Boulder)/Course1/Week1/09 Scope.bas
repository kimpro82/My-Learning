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
