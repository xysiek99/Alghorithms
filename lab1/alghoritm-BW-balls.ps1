$black = Read-Host "Number of black balls"
$blackNum = [int]::Parse($black)
$white = Read-Host "Number of white balls"
$whiteNum = [int]::Parse($white)

$all = $blackNum + $whiteNum
$condition = ($blackNum % 2)

if ($condition -eq 1) {
        Write-Host "Left: $($all)"
        Write-Host "Black: $($blackNum)"
        Write-Host "White: $($whiteNum)"
        Write-Host "***************************************"

    while (($all -ge 2) -and ($whiteNum -ge 0) -and ($blackNum -ge 1)) {
        $randWhite = 2 - (Get-Random -Minimum 0 -Maximum 3)
        Write-Host "RANDOM WHITE: $randWhite"

        if (($randWhite -eq 1) -and ($whiteNum -ge 1)) {
            $whiteNum -= 1
            $all -= 1
        }
       
        if (($randWhite -eq 0) -and ($blackNum -gt 1)) {
            $blackNum -= 2
            $all -= 2
        }
       
        if (($randWhite -eq 2) -and ($whiteNum -gt 1)) {
            $whiteNum -= 2
            $all -= 2
        }
       
        Write-Host "Left: $($all)"
        Write-Host "Black: $($blackNum)"
        Write-Host "White: $($whiteNum)"
        Write-Host "***************************************"
    }

} else {
    Write-Host "Incorrect input"
}