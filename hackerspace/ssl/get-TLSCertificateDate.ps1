 function get-TLSCertificateDate {
   param(
     [Parameter(Mandatory=$true,ValueFromPipelineByPropertyName=$true,ValueFromPipeline=$true)]
     $ComputerName,
     
     [Parameter(ValueFromPipelineByPropertyName=$true)]
     [int]$Port = 443
   )
       $ProtocolName = "Tls11"
       $Socket = New-Object System.Net.Sockets.Socket([System.Net.Sockets.SocketType]::Stream, [System.Net.Sockets.ProtocolType]::Tcp)
       $Socket.Connect($ComputerName, $Port)
         $NetStream = New-Object System.Net.Sockets.NetworkStream($Socket, $true)
         $SslStream = New-Object System.Net.Security.SslStream($NetStream, $true)
         $SslStream.AuthenticateAsClient($ComputerName,  $null, $ProtocolName, $false )
         [System.Security.Cryptography.X509Certificates.X509Certificate2]$RemoteCertificate = [System.Security.Cryptography.X509Certificates.X509Certificate2]$SslStream.RemoteCertificate
         $SslStream.Close()
		 $startDate = [datetime]$RemoteCertificate.GetEffectiveDateString()
		 $endDate =  [datetime]$RemoteCertificate.GetExpirationDateString()
		 $now = $(get-date)
		 if ( $startDate -gt $now){
			Write-host "Certificate is not yet valid"
			return 0
		 }
		 if ( $endDate -lt $now){
			Write-host "Certificate is not valid anymore"
			return 0
		 }
		 $ExpireIn = (NEW-TIMESPAN -Start $now -End $endDate).days
		 if ($ExpireIn -gt 30 ){
			Write-host "[+]Certificate expire in $ExpireIn Days" -ForegroundColor green
			return 1
		 }else {
			Write-host "[+]Warning Certificate expire in $ExpireIn Days" -ForegroundColor red
			return 0
		 }
}
 