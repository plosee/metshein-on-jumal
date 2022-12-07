$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath

$MyOUs = Import-csv $dir\AD_Kasutajad.csv -Delimiter ","

$existingOUs = Get-ADOrganizationalUnit -filter * 
$existingUsers = Get-ADUser -filter *

$ParentPath = "DC=LAANE,DC=LOCAL"

foreach ($OU in $MyOUs){

  $DN = "OU="+$OU.Osakond+","+$ParentPath

  $Eesnimi = $OU.Eesnimi
  $Perenimi = $OU.Perekonnanimi

  $Name = $OU.Osakond
  $User = $Eesnimi+"."+$Perenimi
  $Email = $Eesnimi.substring(0,1)+$Perenimi+"@"+"LAANE.LOCAL" #Tehniliselt peaks olema JPere@LAANE.LOCAL

  
  $UserPath = $DN #cn=Justin.Adams,OU=Haldus,DC=laane,DC=local
  
  $userpath

  $splat = @{

     SamaccountName = "$($User)" 
     name = "$($User)"
     Path = "$($Userpath)" 
     Userprincipalname = "$($Email)" 
     AccountPassword = (ConvertTo-securestring "Cool2Pass!" -AsPlainText -force) 
     enabled = $true
     PasswordNeverExpires = $true 
     Givenname = $OU.Eesnimi
     Surname = $OU.Perekonnanimi
     
     }


  if ($existingOUs.DistinguishedName -contains $DN) { write-host $OU.name "$DN elksisteerib HAHhhAAhahah" }
  else { New-ADOrganizationalUnit -Name $Name -Path $ParentPath }
     
  
  if ($existingUsers.SamAccountName -contains $User) { write-host $OU.user "User $User eksisteeberib hahahahsfhHhfhFHh" }
  else {New-ADUser @splat}


}
