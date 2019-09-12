# configs
$mypath = (Get-Item -Path ".\").FullName
$stubsdest = "$mypath\stubs"
$rhinobase = "C:\Program Files\Rhino WIP"
$rhinoplugins = "$rhinobase\Plug-ins"
$rhinosystem = "$rhinobase\System"

cd "builder\bin\Release x64"

./pystubsbuilder.exe --dest=$stubsdest --search=$rhinosystem "$rhinosystem\Eto.dll"
./pystubsbuilder.exe --dest=$stubsdest --search=$rhinosystem "$rhinosystem\RhinoCommon.dll"
./pystubsbuilder.exe --dest=$stubsdest --search=$rhinosystem "$rhinoplugins\Grasshopper\Grasshopper.dll"
./pystubsbuilder.exe --dest=$stubsdest --search=$rhinosystem "$rhinoplugins\Grasshopper\GH_IO.dll"
./pystubsbuilder.exe --dest=$stubsdest --search=$rhinosystem "$rhinoplugins\Grasshopper\GH_Util.dll"

# back to where started
cd $mypath