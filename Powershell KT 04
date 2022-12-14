#############################################################
#                       marten laane                        #
#                         14.12.22                          #
#                     Powershell KT 04                      #
#                                                           #
# Skript küsib kasutajalt, mis XML fail on                  #
# Skript siis võtab selle XML faili sisu                    #
# Skript iga reaga võtab nime muutujasse                    #
# Muutujat kasutatakse tekstifailide ja kataloogide jaoks   #
#############################################################

$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath

$1input = read-host "mis on failinimi? (.xml)"


if ($1input -notmatch "$_.xml")
{
    DO
    {
        write-host "vale fail"
        $1input = read-host "kuule see sitt on vale failinimi, pane natuke oigem siia"
    }
   Until ($1input -match "$_.xml")
}

$xml = [xml](Get-Content $dir\$1input)
$rows = $xml.customers.customer

foreach ($row in $rows)
{
    $muutuja = $row.full_name
    New-Item $dir\customers\$muutuja -ItemType Directory
    new-item $dir\customers\$muutuja\$muutuja.txt
    $row >> $dir\customers\$muutuja\$muutuja.txt
}
