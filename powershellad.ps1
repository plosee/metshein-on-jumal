#sama kataloog, mis skriptil
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath

$users = import-csv $dir\AD_Kasutajad.csv | format-table

$parentou = 'DC=LAANE,DC=LOCAL'
$adfilter = Get-ADOrganizationalUnit -filter "distinguishedname -like '*'"
foreach ($user in $users)

{

    $enimi = $user.Eesnimi
    $pnimi = $user.Perekonnanimi
    $okond += $user.Osakond
    

    if ($adfilter -ne $okond)   {
    New-ADOrganizationalUnit -name $okond -path $parentou
    }
}
