# configs
$mypath = (Get-Item -Path ".\").FullName
$stubsdest = "$mypath\stubs"
$rhinobase = "C:\Program Files\Rhino 7"
$rhinoplugins = "$rhinobase\Plug-ins"
$rhinosystem = "$rhinobase\System"

cd "builder\bin"

./PyStubbler.exe --search=$rhinosystem "$rhinosystem\Eto.dll"
./PyStubbler.exe --search=$rhinosystem "$rhinosystem\RhinoCommon.dll"
./PyStubbler.exe --search=$rhinosystem "$rhinoplugins\Grasshopper\Grasshopper.dll"
./PyStubbler.exe --search=$rhinosystem "$rhinoplugins\Grasshopper\GH_IO.dll"
./PyStubbler.exe --search=$rhinosystem "$rhinoplugins\Grasshopper\GH_Util.dll"

# back to where started
cd $mypath