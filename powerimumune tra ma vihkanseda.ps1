$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath

$MyOUs = Import-csv $dir\kasutajad.csv -Delimiter ","

$existingOUs = Get-ADOrganizationalUnit -filter * 
$existingUsers = Get-ADUser -filter *

$ParentPath = "DC=LAANE,DC=LOCAL"

foreach ($OU in $MyOUs){

  
  $DN = "OU="+$OU.Osakond+","+$ParentPath
  $USERDN = "CN="+$OU.Eesnimi+"."+$OU.Perekonnanimi+","+"OU="+$OU.Osakond+$ParentPath #CN=Jaanus.Pere,OU=Personal,DC=LAANE,DC=LOCAL

  $Eesnimi = $OU.Eesnimi
  $Perenimi = $OU.Perekonnanimi

  $Name = $OU.Osakond 
  $User = $Eesnimi+"."+$Perenimi
  $Email = $Eesnimi.substring(0,1)+$Perenimi+"@"+"LAANE.LOCAL" #Tehniliselt peaks olema JPere@LAANE.LOCAL

  $ChildPath = "OU=" + $User + ","+ "CN=" + $Name
  $UserPath = $ChildPath + $ParentPath


  #check for OU in existing list
  if ($existingOUs.DistinguishedName -contains $DN) { write-host $OU.name "$DN elksisteerib HAHhhAAhahah" }
  else { New-ADOrganizationalUnit -Name $Name -Path $ParentPath }
     
  
  if ($existingUsers.distinguishedname -contains $USERDN) { write-host $OU.user "User $User eksisteeberib hahahahsfhHhfhFHh" }
  else { New-ADUser -SamaccountName $User -name $User -Path $UserPath -EmailAddress $Email -AccountPassword (ConvertTo-securestring "Cool2Pass!" -AsPlainText -force) -enabled $true -PasswordNeverExpires $true }

}
