Option Explicit

Sub ApplicationRunExample()
    
    Application.Run "'RunMe.xlsm'!RunMe"

End Sub


Sub ApplicationRunExample2()

    Dim FileName As String, aWB As Workbook

    FileName = Application.GetOpenFilename("Excel Files (*.xlsm), *.xlsm")
    Workbooks.Open FileName

    Set aWB = ActiveWorkbook
    Application.Run "'RunMe.xlsm'!RunMe" 'It can be changed something better ...
    aWB.Close SaveChanges:=False

End Sub
