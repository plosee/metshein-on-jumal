
function mata{
     <#
    .SYNOPSIS
        arvutab pindala ringil
    .DESCRIPTION
        arvutab pindala ringil
    .EXAMPLE
        arvutab pindala ringil
    .EXAMPLE
        arvutab pindala ringil
    #>
        param(
        
            # Esimese parameetri kirjeldus
            $r
         )



    $s = [Math]::PI*[Math]::Pow($r, 2)
    $s
    

    }


function matat2($nimi){
    $nime = $nimi.tolower()
    $nima = $nime.replace("ö", "o").replace("ä", "a").replace("õ", "o").replace("ü", "u")
    (Get-Culture).TextInfo.ToTitleCase($nima.tolower())
    
    }
    
matat2("õüöä")
